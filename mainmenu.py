import pygame
import sys

# Initialize Pygame
pygame.init()

# variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# this creates the window and applies the height and weight
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Adventure Game")

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

        screen.fill(BLACK)

        draw_text("Text Adventure Pi", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text("Press ENTER to Start", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text("Press Esc to Quit", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

        pygame.display.flip()
