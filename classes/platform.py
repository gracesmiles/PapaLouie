"""
Static and moving platforms
"""

import pygame
from settings import PLATFORM_SETTINGS  # Import platform settings


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, platform_type="normal"):
        super().__init__()
        self.type = platform_type
        self.image = pygame.image.load(PLATFORM_SETTINGS[platform_type]["image"])
        self.image = pygame.transform.scale(
            self.image, (PLATFORM_SETTINGS[platform_type]["width"], PLATFORM_SETTINGS[platform_type]["height"])
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = PLATFORM_SETTINGS[platform_type].get("speed", 0)  # Only moving platforms use speed

    def update(self):
        """Moves the platform if it's a moving type."""
        if self.type == "moving":
            self.rect.x += self.speed
            # Reverse direction if hitting a boundary
            if self.rect.right >= 800 or self.rect.left <= 0:
                self.speed *= -1
