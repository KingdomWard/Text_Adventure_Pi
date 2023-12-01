import pygame
import sys
import psutil
import threading
import time
import config

from mainmenu import main_menu
from text_adventure import game_loop

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module

# Music playback function
def play_music():
    pygame.mixer.music.load("music/medievaltrack.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # Music will loop indefinitely

    while True:
        if config.is_game_paused:  # Use config module variable
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

            time.sleep(1)  # Sleep to prevent high CPU usage

# Function to calculate and display CPU usage
def calculate_cpu_usage(initial_cpu_times):
    final_cpu_times = psutil.cpu_times(percpu=True)

    total_usage = 0
    num_cores = len(initial_cpu_times)
    for i, (initial, final) in enumerate(zip(initial_cpu_times, final_cpu_times)):
        cpu_usage = {k: getattr(final, k) - getattr(initial, k) for k in final._fields}
        core_total_cpu_time = sum(cpu_usage.values())
        if core_total_cpu_time > 0:  # Prevent division by zero
            core_usage_percentage = (core_total_cpu_time / sum(cpu_usage.values())) * 100
            print(f"CPU usage for Core {i+1}: {core_usage_percentage:.2f}%")
            total_usage += core_usage_percentage

    # Calculate and display the average CPU usage
    average_usage = total_usage / num_cores if num_cores > 0 else 0
    print(f"Average CPU usage: {average_usage:.2f}%")



def main():
    # Start the music thread
    music_thread = threading.Thread(target=play_music, daemon=True)
    music_thread.start()

    global is_game_paused

    while True:
        menu_result = main_menu()

        if menu_result == "start":
            # Start recording CPU usage
            initial_cpu_times = psutil.cpu_times(percpu=True)

            # Run the game loop
            config.is_game_paused = False  # Use config module variable
            game_loop()

            # Calculate and display CPU usage
            calculate_cpu_usage(initial_cpu_times)

        elif menu_result == "quit":
            break

if __name__ == "__main__":
    initial_CPU = psutil.cpu_times()
    initial_process_CPU = psutil.Process().cpu_times()
    start_time = time.time()

    main()

    # Collect CPU usage data
    end_time = time.time()
    final_CPU = psutil.cpu_times()
    final_process_cpu = psutil.Process().cpu_times()

    total_cpu_time = sum(final_CPU) - sum(initial_CPU)
    process_cpu_time = (final_process_cpu.user - initial_process_CPU.user) + \
                        (final_process_cpu.system - initial_process_CPU.system)
    cpu_usage_percentage = (process_cpu_time / total_cpu_time) * 100
    print(f"CPU usage percentage:  {cpu_usage_percentage:2f}%")
    print(f"Completion time: {end_time - start_time}")
