import pygame
import sys
from mainmenu import main_menu
from text_adventure import game_loop

# initialize the game
pygame.init()

def main():
    while True:
        menu_result = main_menu()
        
        if menu_result == "start":
            game_loop()
            
        elif menu_result == "quit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
