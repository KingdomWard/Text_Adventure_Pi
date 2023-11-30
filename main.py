import pygame
import sys
import psutil
from mainmenu import main_menu
from text_adventure import game_loop
import time

initial_CPU = psutil.cpu_times()
initial_process_CPU = psutil.Process().cpu_times()
start_time = time.time()
# Initialize Pygame
pygame.init()

def main():
    while True:
        menu_result = main_menu()

        if menu_result == "start":
            # Start recording CPU usage
            initial_cpu_times = psutil.cpu_times(percpu=True)

            # Run the game loop
            game_loop()

            # End recording CPU usage
            final_cpu_times = psutil.cpu_times(percpu=True)

            # Calculate and display CPU usage for each core and average
            total_usage = 0
            num_cores = len(initial_cpu_times)
            for i, (initial, final) in enumerate(zip(initial_cpu_times, final_cpu_times)):
                cpu_usage = {k: getattr(final, k) - getattr(initial, k) for k in final._fields}
                core_total_cpu_time = sum(cpu_usage.values())
                core_usage_percentage = (core_total_cpu_time / psutil.cpu_count())
                print(f"CPU usage for Core {i+1}: {core_usage_percentage:.6f}%")
                total_usage += core_usage_percentage

            # Calculate and display the average CPU usage
            average_usage = total_usage / num_cores
            print(f"Average CPU usage: {average_usage:.6f}%")

        elif menu_result == "quit":
            break

if __name__ == "__main__":
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