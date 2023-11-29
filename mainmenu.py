import pygame
import sys

# Initialize Pygame
pygame.init()

# variables
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
FONT2 = pygame.font.Font("Font/BigelowRules-Regular.ttf", 54)
# this creates the window and applies the height and weight
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Adventure Game")

title_screen_image = pygame.image.load("images/title screen.jpeg")

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "start"
                if event.key == pygame.K_ESCAPE:
                    return "quit"

        #screen.fill(BLACK)
        screen.blit(title_screen_image, (180,-100))
        draw_text("Text Adventure Pi", FONT2, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 -60)
        draw_text("Press ENTER to Start", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        draw_text("Press ESC to Quit", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130)

        pygame.display.flip()
