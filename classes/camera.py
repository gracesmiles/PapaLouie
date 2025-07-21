"""
Camera movement to follow the player
"""

import pygame
from settings import SETTINGS  # Import game settings


class Camera:
    def __init__(self, width, height):
        """Initializes the camera with boundaries to follow the player properly."""
        self.camera = pygame.Rect(0, 0, width, height)  # Camera viewport
        self.world_width = width  # Define world width
        self.world_height = height

    def update(self, player):
        """Centers the camera on the player unless at the world boundaries."""
        target_x = player.rect.centerx - SETTINGS["WIDTH"] // 2

        # Ensure the camera follows only within the extended world
        self.camera.x = max(0, min(target_x, self.world_width - SETTINGS["WIDTH"]))

    def apply(self, entity):
        """Applies camera offset only to game objects (not the background)."""
        return entity.rect.move(-self.camera.x, 0)  # Only move horizontally
