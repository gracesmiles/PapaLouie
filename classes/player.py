import pygame
from settings import SETTINGS, PLAYER_SETTINGS  # Import game and player settings
from classes.platform import Platform


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Transform Images
        # Make left and right
        right1Load = pygame.image.load("assets/images/playerLeft_walk1.png")
        right2Load = pygame.image.load("assets/images/playerLeft_walk2.png")
        right1 = pygame.transform.flip(right1Load, True, False)
        right2 = pygame.transform.flip(right2Load, True, False)
        pygame.image.save(right1, "assets/images/playerRight_walk1.png")
        pygame.image.save(right2, "assets/images/playerRight_walk2.png")
        
        # Make lists for walking left or right and scale
        self.walk_left = [
            pygame.transform.scale(pygame.image.load("assets/images/playerLeft_walk1.png"), (50, 80)),
            pygame.transform.scale(pygame.image.load("assets/images/playerLeft_walk2.png"), (50, 80))
        ]
        self.walk_right = [
            pygame.transform.scale(pygame.image.load("assets/images/playerRight_walk1.png"), (50, 80)),
            pygame.transform.scale(pygame.image.load("assets/images/playerRight_walk2.png"), (50, 80))
        ]
        self.image = self.walk_right[0]  # Starting image
        self.jump_effect = pygame.mixer.Sound("assets/audios/jump.wav")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0  # Vertical velocity for jumping
        self.on_ground = False  # Track if player is on a surface
        self.fell_off_screen = False    # Track if player is still on platforms
        self.walk_index = 0
        self.animation_counter = 0
        self.facing_right = True
        self.jump_pressed = False  # Track if jump key was pressed

    def move(self, keys):
        """Handles left, right movement and jumping."""
        moving = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SETTINGS["speed"]
            self.facing_right = False
            moving = True
            self.image = self.walk_left[self.animation_counter]
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SETTINGS["speed"]
            self.facing_right = True
            moving = True
            self.image = self.walk_right[self.animation_counter]

        length_list = 2
        if moving:
            self.animation_counter = (self.animation_counter + 1) % length_list

        # Prevent player from moving beyond the left boundary
        if self.rect.left < 0:
            self.rect.left = 0

        # Righthand boundary value
        if self.rect.right > SETTINGS["WIDTH"] + 1000:  
            self.rect.right = SETTINGS["WIDTH"] + 1000

        # Handle jumping - only jump once per key press
        if keys[pygame.K_SPACE] and self.on_ground and not self.jump_pressed:
            self.vel_y = -PLAYER_SETTINGS["jump_power"]  # Jump if on ground
            self.on_ground = False  # Set to False so gravity applies again
            self.jump_pressed = True  # Mark that jump was pressed
            self.jump_effect.play()
        
        # Reset jump_pressed when space is released
        if not keys[pygame.K_SPACE]:
            self.jump_pressed = False
    
    def apply_gravity(self, platforms):
        """Applies gravity to the player."""
        self.vel_y += PLAYER_SETTINGS["gravity"]
        self.rect.y += self.vel_y
        
        # Check if player fell off the screen
        if self.rect.bottom >= SETTINGS["HEIGHT"]:  # Adjust based on game window height
            self.fell_off_screen = True
            self.on_ground = False
        
        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y >= 0:
                self.rect.bottom = platform.rect.top  # Snap player on top of platform
                self.vel_y = 0  # Stop downward motion
                self.on_ground = True  # Player is grounded
