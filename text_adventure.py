import pygame
import sys
from textwrap import fill

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
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


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Adventure Game")

# This function displays the text on screen with parameters
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# loop function that starts that begins the intro state, press keys to go to other states
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
                    if event.key == pygame.K_1:
                        game_state = "room2"
                    elif event.key == pygame.K_2:
                        game_state = "room3"
                elif game_state == "room2":
                    if event.key == pygame.K_BACKSPACE:
                        game_state = "room1"
                elif game_state == "room3":
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
        elif game_state == "room2":
            draw_text("You are in Room 2. Press BACKSPACE to go back.", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif game_state == "room3":
            draw_text("You are in Room 3. Press BACKSPACE to go back.", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()
