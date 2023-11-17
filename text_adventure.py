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

talk_to_woman_1 = '“My name is Ireena Kolyana,” the woman says as you enter.'
talk_to_woman_2 = 'You notice that under the fringes of her scarf two sets of small puncture wounds mark her neck.'

what_is_place_1 = '“You, my dear traveler, have found yourself in Barovia, a land lost to time and under the control of a terrible monster.”'

scarf_1 = 'She pulls the scarf up on her neck and hesitantly replies, “Yes, by the name of Strahd."'
scarf_2 = '"He is the baron of these lands and he is a powerful vampire, his magic is what controls the mists around this land."'
scarf_3 = '"While he lives they exist and none of us can leave.”'

slay_monster_1 = '“The only way out is to slay the monster, but that is much easier said than done."'
slay_monster_2 = '"He has his focus set on the few townspeople left with sense."'
slay_monster_3 = '"We have been besieged here for the past two weeks."'
slay_monster_4 = '"Every night we are attacked and must defend ourselves from wolves and ghouls alike."'

accomplished_1 = 'She sighs and looks at you hesitantly, “the only way is to slay him but I know not how that can be accomplished."'
accomplished_2 = '"There is a larger village deeper into the woods and if someone did know they would be there.”'

nod_1 = '“Please,” she says, grabbing you by your sleeve, “take us with you, I do not think it is safe to stay here any longer.”'
nod_2 = 'You nod your head and prepare to leave.'

moors_intro_1 = 'As you follow the road deeper into the rocky grassland of the Moors the stone road becomes more and more dilapidated,'
moors_intro_2 = 'eventually becoming nothing more than a set of wagon tracks etched into packed dirt.'
moors_intro_3 = 'Finally at what could pass for a crossroads.'
moors_intro_4 = 'Before you there are two more dirt packed roads leading off to the north and West.'
moors_intro_5 = 'To the East the road becomes significantly nicer and in the distance on the side of a distant mountain you see an ominous castle peeking out of the mists.'

moors_north_1 = 'The land smoothes out back into hilly forests and ahead of you you begin to notice the smoke rising from a large settlement.'

mountain_slope_intro_1 = 'The road fades away under a covering of snow, but it takes you far enough to see the facade of some kind of temple carved into the sheer mountainside ahead.'
mountain_slope_intro_2 = 'The front of the structure is fifty feet high and has six alcoves containing twenty-foot-tall statues.'
mountain_slope_intro_3 = ' Each statue is carved from a single block of amber and depicts a faceless, hooded figure, its hands pressed together in a gesture of prayer.'
mountain_slope_intro_4 = 'Between the two innermost statues is a twenty-foot-tall archway with a staircase leading down.'

down_stairs_1 = 'Icy steps descend ten feet to a time-ravaged hallway with arrow slits in the walls.'
down_stairs_2 = 'Beyond the hall lies a vast, sepulchral darkness.'

overlook_1 = 'A twenty-foot-wide balcony of black marble with a shattered railing overlooks a vast temple.'
overlook_2 = 'Black marble staircases at each end of the balcony descend thirty feet to the temple floor.'
overlook_3 = 'The vaulted ceiling is thirty feet above the balcony. The walls and ceiling are covered in an amber glaze, lending the gloom a golden sheen.'
overlook_4 = 'A set of amber doors stand destroyed on the west end of the room and a collection of skeletons loom in the corner.'

empty_barracks_1 = 'Shattered bits of wood cover the floor of this frigid, twenty-foot-square room.'

guard_room_1 ='Two arrow slits are carved into the west wall of this 10-foot-high, twenty-foot-square room.'
guard_room_2 = 'Slumped in the northeast corner is askelton wearing a blue wizard’s robe clutching a wand to its chest.'

temple_secrets_1 = 'Four black marble columns support the vaulting ceiling of the temple, at the north end of which stands a forty-foot-tall statue of a cowled figure in flowing robes.'
temple_secrets_2 = 'The statue’s stony hands are outstretched as if in the midst of casting a spell. Its face is a void of utter blackness.'
temple_secrets_3 = 'The ominous statue stands between two black marble balconies, one of which has partially collapsed and fallen on the temples black marble floor, in front of an open doorway.'
temple_secrets_4 = 'The walls of the temple are sheathed in amber, and the doors leading from it are made of amber as well.'
temple_secrets_5 = 'Arched hallways coated with amber lead away from the temple to the west and east.'
temple_secrets_6 = 'Flanking these exits are alcoves that hold white marble statues of robed human wizards with pointed hats and golden staffs.'
temple_secrets_7 = 'One of them has toppled over and lies shattered on the floor.'

investigate_statues_1 = 'You approach the toppled statue in the center of the room and inspect the ruined remains.'
investigate_statues_2 = 'As you move through the rubble you hear the grinding of stone on marble and turn to see two statues have come to life!'

fight_statues_1 = 'Upon their defeat you hear another instance of stone grinding on stone and witness the altar opening up to a blinding light.'
fight_statues_2 = 'As you approach the black marble plinth, you notice that the light seems to form into the shape of a sword, as your hand grips it you feel power flood through you.'

bog_intro_1 = 'As you make your way through the swampy undergrowth you begin to see a shape forming through the trees.'
bog_intro_2 = 'A branch in the road leads west to a promontory, atop which is perched a dilapidated stone wind-mill, its warped wooden vanes stripped bare.'
bog_intro_3 = 'As you approach you get a better view of the tall building.'
bog_intro_4 = 'The onion-domed edifice leans forward and to one side, as though trying to turn away from the stormy gray sky.'
bog_intro_5 = 'You see gray brick walls and dirt-covered windows on the upper floors.'
bog_intro_6 = 'A decrepit wooden platform encircles the windmill above a flimsy doorway leading to the building’s interior.'
bog_intro_7 = 'Perched on a wooden beam above the door is a raven. It hops and squawks at you, seemingly agitated.'

enter_windmill_1 = 'The ground floor has been converted into a makeshift kitchen, but the room is filthy. Baskets and old dishware are piled everywhere.'
enter_windmill_2 = 'Adding to the clutter is a peddler’s cart, a chicken coop, a heavy wooden trunk, and a pretty wooden cabinet with flowers painted on its doors.'
enter_windmill_3 = 'In addition to the clucking of the chickens, you hear toads croaking. The sweet smell of pastries blends horribly with a stench that burns you nostrils.'
enter_windmill_4 = 'The awful odor comes out of an open, upright barrel in the center of the room.'
enter_windmill_5 = 'Warmth issues from a brick oven against one wall, and a crumbling staircase ascends the wall across from it.'
enter_windmill_6 = 'Shrieks and cackles from somewhere higher up cause the old mill the shudder.'

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

                elif game_state == "room 2-2-3":
                    if event.key == pygame.K_1:
                        game_state = "room 2-2-4"

                elif game_state == "room 2-2-4":
                    if event.key == pygame.K_1:
                        game_state = "room 2-2-5"

                elif game_state == "room 2-2-5":
                    if event.key == pygame.K_1:
                        game_state = "room 2-2-6"
                
                elif game_state == "room 2-2-6":
                    if event.key == pygame.K_1:
                        game_state = "room 2-2-7"

                elif game_state == "room 2-2-7":
                    if event.key == pygame.K_RETURN: # press ENTER to go transition state
                        game_state = "room 3-0"
                
                elif game_state == "room 3-0":
                    if event.key == pygame.K_1:
                        game_state = "room 3-0-1"
                    elif event.key == pygame.K_2:
                        game_state = "room 4-0"
                # moors
                elif game_state == "room 3-0-1":
                    if event.key == pygame.K_1: # moors head north
                        game_state = "room 3-1"
                    elif event.key == pygame.K_2: # head east to castle ravenloft
                        game_state = "room 3-2"
                    elif event.key == pygame.K_3: # head south back to town
                        game_state = "room1"
                # mountain slope
                elif game_state == "4-0":
                    if event.key == pygame.K_RETURN:
                        game_state = "4-1"

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

        elif game_state == "room 2-2-3":    
            draw_text(talk_to_woman_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(talk_to_woman_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text('1. [A terrible monster?]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)

        elif game_state == "room 2-2-4":    
            draw_text(scarf_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(scarf_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(scarf_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text('1. [There must be something that can be done?]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)

        elif game_state == "room 2-2-5":    
            draw_text(slay_monster_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(slay_monster_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(slay_monster_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text(slay_monster_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 100)
            draw_text('1. [I would like to help you slay the monster and win my freedom, surely you must know a way that can be accomplished?]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)

        elif game_state == "room 2-2-6":
            draw_text(accomplished_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(accomplished_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text('1. [Then that is where I must go]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)

        elif game_state == "room 2-2-7":
            draw_text(nod_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(nod_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text("Press ENTER to continue", FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)
            # left off to talking to lady inside mansion
        
        elif game_state == "room 3-0":
            draw_text('What will you do now?', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text('1. [Go to the Moors]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)
            draw_text('2. [Go to Mountain Slope]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 60)

        elif game_state == "room 3-0-1":    
            draw_text(moors_intro_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(moors_intro_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(moors_intro_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text(moors_intro_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 80)
            draw_text(moors_intro_5, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 40)
            draw_text('1. [Head North]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)
            draw_text('2. [Head East]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 60)
            draw_text('3. [Head South back to Town]', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 80)

        elif game_state == "room 3-1":
            draw_text('You notice a large V etched into a rock', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(moors_north_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)

        elif game_state == "room 4-0":
            draw_text(mountain_slope_intro_1, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 200)
            draw_text(mountain_slope_intro_2, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 150)
            draw_text(mountain_slope_intro_3, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 125)
            draw_text(mountain_slope_intro_4, FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 - 100)
            draw_text('Press ENTER to explore the Temple!', FONT, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 40)

        pygame.display.flip()
