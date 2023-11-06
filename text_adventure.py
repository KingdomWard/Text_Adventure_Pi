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
#images for scenes
intro_image = pygame.image.load("Text_Adventure_Pi/images/intro text image (muddy foggy village).jpeg")
fight_rats_image = pygame.image.load("Text_Adventure_Pi/images/fight rats.jpeg")
house_villagers_image = pygame.image.load("Text_Adventure_Pi/images/house villagers.jpeg")
house_zombies_images = pygame.image.load("Text_Adventure_Pi/images/house zombie.jpeg")
title_screen_image = pygame.image.load("Text_Adventure_Pi/images/title screen.jpeg")
dead_end_image = pygame.image.load("Text_Adventure_Pi/images/dead end.jpeg")
map = pygame.image.load("Text_Adventure_Pi/images/Barovia-Map.webp")
map1 = pygame.image.load("Text_Adventure_Pi/images/Town map.jpg")

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

local_tavern_1 = 'A single shaft of light thrusts illumination into the main square, its brightness looking like a solid pillar in the heavy fog.'
local_tavern_2 = 'Above the gaping doorway, a sign hangs precariously askew, proclaiming this to be the Blood on the Vine tavern.'

enter_tavern_1 = 'You enter the rather large building, this once finely appointed tavern has grown shoddy over the years.'
enter_tavern_2 = 'A blazing fire in the hearth gives scant warmth to the few huddled souls within.'
enter_tavern_3 = 'They include three colorfully dressed individuals, a bearded older barkeep, and a young man who sits by himself at a corner table.'

large_mansion_1 = 'A weary-looking mansion squats behind a rusting iron fence. The iron gates are twisted and torn.'
large_mansion_2 = 'The right gate lies cast aside, while the left swings lazily in the wind. The stuttering squeal and clang of the gate repeats with mindless precision.'
large_mansion_3 = 'Weeds choke the grounds and press with menace upon the house itself.'
large_mansion_4 = 'Yet, against the walls, the growth has been tramped down to create a path all about the domain.'
large_mansion_5 = 'Heavy claw markings have stripped the once-beautiful finish of the walls. Great black marks tell of the fires that have assailed the mansion.'
large_mansion_6 = 'Not a pane nor a shard of glass stands in any window. All the windows are barred with planks, each one marked with stains of evil omen.'

approach_mansion_door_1 = 'As you approach the door you notice a well trampled ring around the house with both wolf and human footprints.'
approach_mansion_door_2 = 'As you inspect the tracks you notice one of the curtains shift as if someone was peeking at you from inside the house.'
approach_mansion_door_3 = 'You quickly approach the door and knock and hear a woman from behind the door say, “Go away, we have no want of you here.”'

lady_mansion_1 = '"Swear to me you have no allegiance to that monster (Vampire name), I have no patience for liars.”'
lady_mansion_2 = 'You quickly and quietly assure her that you have no ties to anyone named (Vampire name).'
lady_mansion_3 = 'After a moment you hear the turning of locks in the large wooden door and with a slow creak the door opens.'

inside_mansion_1 = 'The interior of the mansion is well furnished, yet the fixtures show signs of great wear.'
inside_mansion_2 = 'Noticeable oddities are the boarded-up windows and the presence of holy symbols in every room.'
inside_mansion_3 = 'The burgomaster is in a side drawing room on the floor, lying in a simple wooden coffin surrounded by wilting flowers and a faint odor of decay.'
inside_mansion_4 = '“My name is Ireena Kolyana,” the woman says as you enter.'
inside_mansion_5 = 'You notice that under the fringes of her scarf two sets of small puncture wounds mark her neck.'



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
                    game_state = "room1"            # title screen
                elif game_state == "room1":
                    if event.key == pygame.K_1:
                        game_state = "room2"        #fight rats
                    elif event.key == pygame.K_2:
                        game_state = "room3"        #house with villagers
                    elif event.key == pygame.K_3:
                        game_state = "room4"        # house with zombies

                elif game_state == "room2":
                    if event.key == pygame.K_RETURN:
                        game_state = "DeadEnd"
                elif game_state =="DeadEnd":
                    if event.key == pygame.K_RETURN:
                        game_state = "Map1"
                elif game_state == "Map1":
                    if event.key == pygame.K_1:
                        game_state = "room1"

                elif game_state == "room4":
                    if event.key == pygame.K_RETURN:
                        game_state = "room 2-0"  # Transition state between 1 and 2   ##door aproach

                elif game_state == "room 2-0":
                    if event.key == pygame.K_1:
                        game_state = "room 2-1"  # If the player presses 1, go to local tavern
                    elif event.key == pygame.K_2:
                        game_state = "room 2-2"  # If the player presses 2, go to the mansion
                
                elif game_state == "room 2-1": # LOCAL TAVERN
                    if event.key == pygame.K_RETURN: # ENTER go inside local tavern
                        game_state = "room 2-1-0" # 1 to approach barkeep, 2 to approach dressed indivual, 3 to approach young man
                
                elif game_state == "room 2-2": # MANSION CHOICE
                    if event.key == pygame.K_RETURN: # ENTER to approach mansion door
                        game_state = "room 2-2-0"
                
                elif game_state == "room 2-2-0":
                    if event.key == pygame.K_1: # 1 to talk to lady behind mansion door
                        game_state = "room 2-2-1"
                
                elif game_state == "room 2-2-1":
                    if event.key == pygame.K_RETURN:
                        game_state = "room 2-2-2"
                
                elif game_state == "room 2-2-2":
                    if event.key == pygame.K_1:
                        game_state = "room 2-2-3"

        screen.fill(BLACK)

        if game_state == "intro":
            screen.blit(title_screen_image, (180,-100))

            draw_text("Welcome to the Text Adventure Pi!", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
            draw_text("Press any key to continue...", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            
        elif game_state == "DeadEnd":
            screen.blit(dead_end_image, (180,-200))
            draw_text("Press Enter to Respawn", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)

        elif game_state == "Map1":
            screen.blit(map1,(180,0))
            draw_text("Please Choose Location", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)
            draw_text("1. Town", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 150)
        elif game_state == "room1":
            screen.blit(intro_image, (180,-200))
            draw_text(text_intro_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            draw_text(text_intro_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
            draw_text(text_intro_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140)
            draw_text(text_intro_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 160)
            draw_text(text_intro_5, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180)

            draw_text('What will you do?', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 220)

            draw_text("1. Fight Rats", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 125)
            draw_text("2. Go to a House with Villagers", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 150)
            draw_text("3. Go to a House with Zombies", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)

        # fight rats option
        elif game_state == "room2":
            screen.blit(fight_rats_image, (180,-200))
            draw_text(fight_rats_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 150)
            draw_text(fight_rats_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)

        # house with villagers option    
        elif game_state == "room3":
            screen.blit(house_villagers_image, (180,-200))
            draw_text(house_villagers_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 150)
            draw_text(house_villagers_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)

        # house with zombies option
        elif game_state == "room4":
            screen.blit(house_zombies_images, (180,-200))
            draw_text(house_zombies_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 150)
            draw_text(house_zombies_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)
            draw_text(house_zombies_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 200)
            draw_text("press ENTER to fight the zombies", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 250)
        
        # transition state
        elif game_state == "room 2-0":
            draw_text("You won the fight! What will you do now?", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT// 1.5 - 100)
            draw_text("1. Approach the local tavern", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 55)
            draw_text("2. Approach the large mansion", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 20)
        
        elif game_state == "room 2-1":
            draw_text(local_tavern_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 150)
            draw_text(local_tavern_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 175)
            draw_text("Press ENTER to go inside", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 200)
        
        elif game_state == "room 2-1-0":
            draw_text(enter_tavern_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 100)
            draw_text(enter_tavern_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 75)
            draw_text(enter_tavern_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 50)
            draw_text("1. Approach the Barkeep", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 10)
            draw_text("2. Approach the colorfully dressed individual", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 45)
            draw_text("3. Approach the young man", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 70)

        elif game_state == "room 2-2":
            draw_text(large_mansion_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(large_mansion_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 175)
            draw_text(large_mansion_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(large_mansion_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text(large_mansion_5, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 100)
            draw_text(large_mansion_6, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 75)
            draw_text("Press ENTER to approach the door", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)
        
        elif game_state == "room 2-2-0":
            draw_text(approach_mansion_door_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(approach_mansion_door_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 175)
            draw_text(approach_mansion_door_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text("1. [“Please, I’m lost and need any help I can get!”]", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 30)
        
        elif game_state == "room 2-2-1":
            draw_text(lady_mansion_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(lady_mansion_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(lady_mansion_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text("Press ENTER to go inside", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 30)

        elif game_state == "room 2-2-2":    
            draw_text(inside_mansion_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(inside_mansion_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(inside_mansion_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text(inside_mansion_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 80)
            draw_text(inside_mansion_5, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 40)
            draw_text('1. [What is this place?]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)

            # left off to talking to lady inside mansion

        pygame.display.flip()
