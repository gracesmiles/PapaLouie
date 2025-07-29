import pygame
from settings import SETTINGS


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, health):
        """
        Base class for all enemy types.

        Parameters:
        - x, y: Initial position of the enemy.
        - speed: Movement speed.
        - health: Number of hits the enemy can take before being destroyed.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.speed = speed
        self.__health = health  # Encapsulated health attribute
        self.direction = 1  # 1 for right, -1 for left
        self.start_x = x  # Store starting position for boundary checking
        self.original_image = pygame.image.load("assets/images/sundaesaurus.webp").convert_alpha()
        self.enemy_damage = pygame.mixer.Sound("assets/audios/enemy_damage.wav")
        self.dying = False
        self.alpha = 255  # Fully visible
        
        # Load and scale the enemy image
        try:
            self.image = pygame.image.load("assets/images/sundaesaurus.webp")
        except:
            # Fallback to a simple colored rectangle if image not found
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill((255, 0, 0))  # Red rectangle

        # Scale the image once
        self.image = pygame.transform.scale(self.original_image.copy(), (self.width, self.height))
        
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, platforms):
        """Move back and forth on platforms."""
        # Move horizontally
        self.x += self.speed * self.direction
        self.rect.x = self.x
        
        # Check boundaries and reverse direction
        if self.x <= self.start_x - 50 or self.x >= self.start_x + 50:
            self.direction *= -1

    def take_damage(self):
        """Reduces enemy health and checks if it's destroyed."""
        self.__health -= 1
        return self.__health <= 0  # Returns True if enemy should be removed

    def get_health(self):
        """Returns the enemy's current health."""
        return self.__health

    def fade(self):
        """Starts the dying process with fade out and sound"""
        if not self.dying:
            self.dying = True
            self.enemy_damage.play()

    def update(self, platforms):
        if self.dying:
            """Sundae monster fades out"""
            self.alpha -= 10
            if self.alpha <= 5:
                super().kill()
            else:
                self.image = pygame.transform.scale(self.original_image.copy(), (self.width, self.height))
                self.image.set_alpha(self.alpha)
        else:
            """Called by sprite group to update the enemy."""
            self.move(platforms)


# Enemy Subclasses with Polymorphic Movement
class BasicEnemy(Enemy):
    def __init__(self, x, y):
        """A basic enemy that moves back and forth on platforms."""
        super().__init__(x, y, speed=.1, health=1)  # Reduced from 2


class FastEnemy(Enemy):
    def __init__(self, x, y):
        """A fast-moving enemy with low health."""
        super().__init__(x, y, speed=.5, health=1)  # Reduced from 4


class StrongEnemy(Enemy):
    def __init__(self, x, y):
        """A slower but stronger enemy."""
        super().__init__(x, y, speed=0.5, health=2)  # Reduced from 1


class ZigZagEnemy(Enemy):
    def __init__(self, x, y):
        """An enemy that moves in a zig-zag pattern."""
        super().__init__(x, y, speed=1.5, health=1)  # Reduced from 3
        self.direction = 1  # Initial movement direction

    def move(self, platforms):
        """Moves in a zig-zag pattern while moving horizontally."""
        self.x += self.direction * 1.5  # Reduced from 3
        if self.x <= self.start_x - 150 or self.x >= self.start_x + 150:
            self.direction *= -1  # Change direction at boundaries
        self.rect.x = self.x


class HomingEnemy(Enemy):
    def __init__(self, x, y, player):
        """An enemy that follows the player's position."""
        super().__init__(x, y, speed=1, health=1)  # Reduced from 2
        self.player = player  # Reference to the player

    def move(self, platforms):
        """Moves toward the player's x position."""
        if self.player.rect.x > self.x:
            self.x += self.speed
        elif self.player.rect.x < self.x:
            self.x -= self.speed
        self.rect.x = self.x


class RushEnemy(Enemy):
    def __init__(self, x, y):
        """An enemy that speeds up after reaching a certain height."""
        super().__init__(x, y, speed=2, health=1)  # Reduced from 4
        self.rush_speed = 4  # Reduced from 8

    def move(self, platforms):
        """Moves back and forth with variable speed."""
        self.x += self.speed * self.direction
        if self.x <= self.start_x - 120 or self.x >= self.start_x + 120:
            self.direction *= -1
        self.rect.x = self.x
