import pygame
from classes.gameObject import GameObject
import settings


class Enemy(GameObject):
    def __init__(self, x, y, speed, health):
        """
        Base class for all enemy types.

        Parameters:
        - x, y: Initial position of the enemy.
        - speed: Movement speed.
        - health: Number of hits the enemy can take before being destroyed.
        """
        super().__init__(x, y, width=40, height=40, speed=speed)
        self.__health = health  # Encapsulated health attribute
        self.image = pygame.image.load("assets/images/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def move(self):
        """Default movement: moves straight down."""
        self.y += self.speed

    def take_damage(self):
        """Reduces enemy health and checks if it's destroyed."""
        self.__health -= 1
        return self.__health <= 0  # Returns True if enemy should be removed

    def get_health(self):
        """Returns the enemy's current health."""
        return self.__health

    def draw(self, screen):
        """Draws the enemy on the screen."""
        screen.blit(self.image, (self.x, self.y))


# Enemy Subclasses with Polymorphic Movement
class BasicEnemy(Enemy):
    def __init__(self, x, y):
        """A basic enemy that moves straight down."""
        super().__init__(x, y, speed=3, health=2)


class FastEnemy(Enemy):
    def __init__(self, x, y):
        """A fast-moving enemy with low health."""
        super().__init__(x, y, speed=6, health=1)


class StrongEnemy(Enemy):
    def __init__(self, x, y):
        """A slower but stronger enemy."""
        super().__init__(x, y, speed=2, health=3)


class ZigZagEnemy(Enemy):
    def __init__(self, x, y):
        """An enemy that moves in a zig-zag pattern."""
        super().__init__(x, y, speed=3, health=2)
        self.direction = 1  # Initial movement direction

    def move(self):
        """Moves in a zig-zag pattern while descending."""
        self.x += self.direction * 5
        if self.x <= 0 or self.x + self.width >= settings.SCREEN_WIDTH:
            self.direction *= -1  # Change direction at screen edges
        super().move()


class HomingEnemy(Enemy):
    def __init__(self, x, y, player):
        """An enemy that follows the player's position."""
        super().__init__(x, y, speed=2, health=3)
        self.player = player  # Reference to the player

    def move(self):
        """Moves toward the player's x position."""
        if self.player.x > self.x:
            self.x += self.speed
        elif self.player.x < self.x:
            self.x -= self.speed
        super().move()


class RushEnemy(Enemy):
    def __init__(self, x, y):
        """An enemy that speeds up after reaching a certain height."""
        super().__init__(x, y, speed=4, health=2)
        self.rush_speed = 10  # Speed after the rush triggers

    def move(self):
        """Rushes toward the bottom after a delay."""
        if self.y > settings.SCREEN_HEIGHT / 3:
            self.y += self.rush_speed
        else:
            super().move()
