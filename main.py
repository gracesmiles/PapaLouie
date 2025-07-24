import pygame
from settings import SETTINGS
from classes.player import Player

# Initialize Pygame
pygame.init()

# Create the game window using values from the dictionary
screen = pygame.display.set_mode((SETTINGS["WIDTH"], SETTINGS["HEIGHT"]))
pygame.display.set_caption(SETTINGS["TITLE"])

# Create player instance
player = Player(100, 500)

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SETTINGS["BG_COLOR"])  # Set background color
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(player.image, player.rect)  #Draw Player
    
    player.move(keys)      # Move the player based on input
    player.apply_gravity() # Apply gravity using a method from our player class

    pygame.display.flip()

pygame.quit()

