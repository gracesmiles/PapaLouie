import pygame
from settings import SETTINGS, PLAYER_SETTINGS  # Import game and player settings

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_image = pygame.image.load("assets/images/player.png")  # Load original image
        self.image = pygame.transform.scale(original_image, (50, 50))  # Scale image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0  # Vertical velocity for jumping
        self.on_ground = False  # Track if player is on a surface

    def move(self, keys):
        """Handles left, right movement and jumping."""
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SETTINGS["speed"]
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SETTINGS["speed"]

        # Prevent player from moving beyond the left boundary
        if self.rect.left < 0:
            self.rect.left = 0

        # Righthand boundary value
        if self.rect.right > SETTINGS["WIDTH"] + 400:  
            self.rect.right = SETTINGS["WIDTH"] + 400

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -PLAYER_SETTINGS["jump_power"]  # Jump if on ground
            self.on_ground = False  # Set to False so gravity applies again

    def apply_gravity(self, platforms):
        """Applies gravity to the player."""
        self.vel_y += PLAYER_SETTINGS["gravity"]
        self.rect.y += self.vel_y
        # Prevent player from falling off the screen
        if self.rect.bottom >= 560:  # Adjust based on game window height
            self.rect.bottom = 560
            self.vel_y = 0
            self.on_ground = True

        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y >= 0:
                self.rect.bottom = platform.rect.top  # Snap player on top of platform
                self.vel_y = 0  # Stop downward motion
                self.on_ground = True  # Player is grounded
