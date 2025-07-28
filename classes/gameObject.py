import pygame


class GameObject:
    def __init__(self, x, y, width, height, speed):
        """
        Base class for all game objects.

        Parameters:
        - x, y: Position of the object on the screen.
        - width, height: Size of the object.
        - speed: Movement speed of the object.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        """ Placeholder move method to be overridden by child classes. """
        pass

    def draw(self, screen):
        """ Placeholder draw method to be overridden by child classes. """
        pass
