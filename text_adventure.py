import pygame
import sys
from textwrap import fill

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 24)

# Dialogue
text_intro_1 = 'Tall shapes loom out of the dense fog that surrounds everything.'
text_intro_2 = 'The muddy ground underfoot gives way to slick, wet cobblestones.'
text_intro_3 = 'The tall shapes become recognizable as village dwellings.'
text_intro_4 = 'The windows of each house stare out from pools of blackness.'
text_intro_5 = 'No sound cuts the silence except for mournful sobbing that echoes through the streets from a distance.'

fight_rats_1 = 'As you approach the eerily looming wood frame house you hear a faint scratching sound'
fight_rats_2 = 'As you push open a ruined front door a group of rats leap out at you!'

house_villagers_1 = 'As you approach one of the few houses with faint lights in their windows you hear the muffled sounds of hushed conversation on the other side of the door.'
house_villagers_2 = 'The conversation quiets as you knock, clearly the inhabitants are not interested in conversation.'

house_zombies_1 = 'The gentle drifting mist gives way to a boarded up home.'
house_zombies_2 = 'As you approach the barricades you hear a crash and then with an explosion of wood the door shatters outward and you stand face to face with a zombie.'
house_zombies_3 = 'Looks like you need to defend yourself'

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Adventure Game")

# This function displays the text on screen with parameters
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# loop function that begins the intro state, press keys to go to other states
def game_loop():
    game_state = "intro"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game_state == "intro":
                    game_state = "room1"
                elif game_state == "room1":
                    if event.key == pygame.K_1:  # if player presses 1
                        game_state = "room2"
                    elif event.key == pygame.K_2: # if player presses 2
                        game_state = "room3"
                    elif event.key == pygame.K_3: # if player presses 3
                        game_state = "room4"
                # press backspace to go to room 1
                elif game_state == "room2":
                    if event.key == pygame.K_BACKSPACE:
                        game_state = "room1"
                        
                elif game_state == "room3":
                    if event.key == pygame.K_BACKSPACE:
                        game_state = "room1"

                elif game_state == "room4":
                    if event.key == pygame.K_BACKSPACE:
                        game_state = "room1"

        screen.fill(BLACK)

        if game_state == "intro":
            draw_text("Welcome to the Text Adventure Pi!", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text("Press any key to continue...", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            
        elif game_state == "room1":
            draw_text(text_intro_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            draw_text(text_intro_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 20)
            draw_text(text_intro_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 40)
            draw_text(text_intro_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 60)
            draw_text(text_intro_5, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 80)

            draw_text('What will you do?', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 120)

            draw_text("1. Fight Rats", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text("2. Go to a House with Villagers", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            draw_text("3. Go to a House with Zombies", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)

        # fight rats option
        elif game_state == "room2":
            draw_text(fight_rats_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(fight_rats_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)

        # house with villagers option    
        elif game_state == "room3":
            draw_text(house_villagers_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(house_villagers_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)

        # house with zombies option
        elif game_state == "room4":
            draw_text(house_zombies_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(house_zombies_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
            draw_text(house_zombies_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

        pygame.display.flip()
