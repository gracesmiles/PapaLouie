"""
Handles switching between levels
"""

import pygame
from settings import LEVELS
from classes.platform import Platform

class LevelManager:
    def __init__(self, level_name):
        """Initialize the level manager and load the first level."""
        self.level_name = level_name
        self.platforms = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.load_level()

    def load_level(self):
        """Loads level data from LEVELS dictionary and creates objects."""
        level_data = LEVELS[self.level_name]

        # Create platforms
        for platform_data in level_data["platforms"]:
            platform = Platform(platform_data["x"], platform_data["y"], platform_data["type"])
            self.platforms.add(platform)

        # Create collectibles
        """
        for item_data in level_data["collectibles"]:
            if item_data["type"] == "coin":
                collectible = Coin(item_data["x"], item_data["y"])
            else:
                collectible = Bomb(item_data["x"], item_data["y"])
            self.collectibles.add(collectible)

    def get_remaining_coins(self):
        #Returns a list of remaining coins in the current level.
        return [c for c in self.collectibles if isinstance(c, Coin)]
        """

    def next_level(self):
        """Loads the next level if available."""
        level_keys = list(LEVELS.keys())
        current_index = level_keys.index(self.level_name)

        if current_index < len(level_keys) - 1:
            self.level_name = level_keys[current_index + 1]
            self.platforms.empty()
            #self.collectibles.empty()
            self.load_level()
            return True
        return False  # No next level available
