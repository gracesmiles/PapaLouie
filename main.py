import pygame
import random  # Import Random Module
from settings import SETTINGS , GAME_STATES  # Import game settings, game states, and win score
from classes.player import Player # Import player from the player class
from classes.platform import Platform # Import Platform from the platform class
from classes.camera import Camera  # Import Camera
from classes.game import Game  # Import Game Manager
from classes.ui import UI # Import UI Elements
from classes.collectible import Heart  # Import coin and bomb from collectible class
from classes.level_manager import LevelManager  # Import LevelManager


# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SETTINGS["WIDTH"], SETTINGS["HEIGHT"]))
pygame.display.set_caption(SETTINGS["TITLE"])

# Load the background image
background = pygame.image.load(SETTINGS["BG_IMAGE"])

# Create player instance and game objects
player = Player(100, 500)  # Starting position
game = Game()
ui = UI(screen)
level_manager = LevelManager("level_1")

# Create collectible group
collectibles = pygame.sprite.Group()
for _ in range(5):  # Spawn 5 random collectibles
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    if random.choice([True, False]):
        collectibles.add(Heart(x, y))

# Create Camera instance
camera = Camera(SETTINGS["WIDTH"] + 400, SETTINGS["HEIGHT"])  # Extend world horizontally

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()  # Detect key presses

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game.state == GAME_STATES["MENU"] and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.set_state(GAME_STATES["PLAYING"])

        if game.state == GAME_STATES["GAME_OVER"] and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()

                # Reset game state
                level_manager = LevelManager("level_1")  # Restart at level 1
                player.rect.topleft = (100, 500)

    screen.fill(SETTINGS["BG_COLOR"])  
    screen.blit(background, (0, 0)) 

    if game.state == GAME_STATES["MENU"]:
        ui.draw_menu()

    elif game.state == GAME_STATES["PLAYING"]:
        player.move(keys) 
        player.apply_gravity(level_manager.platforms)  # Use platforms from LevelManager

        # Update camera to follow player and Update moving platforms
        camera.update(player)
        level_manager.platforms.update()  # Now we update the platforms using the Level Manager
  
        # Detect collisions
        collected = pygame.sprite.spritecollide(player, level_manager.collectibles, True)
        for item in collected:
            game.increase_life(item.points)

        # Draw the player with camera offset and UI elements
        screen.blit(player.image, camera.apply(player))
        ui.draw_score(game.score, game.get_time_left())

        # Draw platforms with camera offset
        for platform in level_manager.platforms:
            screen.blit(platform.image, camera.apply(platform))

        for collectible in level_manager.collectibles:  # Apply camera movement to collectibles
            screen.blit(collectible.image, camera.apply(collectible))

    elif game.state == GAME_STATES["GAME_OVER"]:
        pass

    pygame.display.flip()

pygame.quit()
