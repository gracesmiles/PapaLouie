import pygame
from settings import SETTINGS  # Import game settings

# Initialize Pygame
pygame.init()

# Create the game window using values from the dictionary
screen = pygame.display.set_mode((SETTINGS["WIDTH"], SETTINGS["HEIGHT"]))
pygame.display.set_caption(SETTINGS["TITLE"])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SETTINGS["BG_COLOR"])  # Set background color
    pygame.display.flip()  # Refresh the screen

# Quit Pygame
pygame.quit()
