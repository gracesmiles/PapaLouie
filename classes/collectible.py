import pygame
from settings import COLLECTIBLES


class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, collectible_type):
        super().__init__()
        self.type = collectible_type
        self.image = pygame.image.load(COLLECTIBLES[collectible_type]["image"])  # Load the correct image
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize for consistency
        self.rect = self.image.get_rect(topleft=(x, y))
        self.points = COLLECTIBLES[collectible_type]["points"]  # Store the point value


class Coin(Collectible):
    def __init__(self, x, y):
        super().__init__(x, y, "coin")  # Uses "coin" properties
