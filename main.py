import pygame
import sys
import psutil
import matplotlib.pyplot as plt
from mainmenu import main_menu
from text_adventure import game_loop
import time


initial_CPU = psutil.cpu_times()
initial_process_CPU = psutil.Process().cpu_times()
start_time = time.time()
# initialize the game
pygame.init()

def main():

    while True:
        menu_result = main_menu()

        if menu_result == "start":
            game_loop()


        elif menu_result == "quit":
            break  # Break out of the loop to plot data





if __name__ == "__main__":
    main()
        # Collect CPU usage data
end_time = time.time()
final_CPU = psutil.cpu_times()
final_process_cpu = psutil.Process().cpu_times()    

        # Collect CPU usage data
end_time = time.time()
final_CPU = psutil.cpu_times()
final_process_cpu = psutil.Process().cpu_times()

total_cpu_time = sum(final_CPU) - sum(initial_CPU)
process_cpu_time = (final_process_cpu.user - initial_process_CPU.user) + \
                   (final_process_cpu.system - initial_process_CPU.system)
cpu_usage_percentage = (process_cpu_time / total_cpu_time) * 100
print(f"CPU usage percentage:  {cpu_usage_percentage:2f}%")

         
