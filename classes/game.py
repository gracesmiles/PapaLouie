import pygame
from settings import GAME_STATES

class Game:
    def __init__(self):
        """Initializes the game state, score, and timer."""
        self.state = GAME_STATES["MENU"]  # Start in the menu
        self.score = 0  # Player's score
        self.start_time = None  # Track when the game starts

    def set_state(self, new_state):
        """Changes the current game state."""
        if new_state in GAME_STATES.values():
            self.state = new_state
            if new_state == GAME_STATES["PLAYING"]:
                self.start_time = pygame.time.get_ticks()  # Start the timer

    def reset(self):
        """Resets the game when restarting."""
        self.state = GAME_STATES["PLAYING"]
        self.score = 0
        self.start_time = pygame.time.get_ticks()

    # ✅ Add reset timer method
    def reset_timer(self):
        """Resets the timer to the full allotted time."""
        self.start_time = pygame.time.get_ticks()

    def increase_score(self, amount=1):
        """Increases the player's score."""
        self.score += amount

    def increase_life(self, amount=1):
        """Increases the player's life"""
        self.score += amount

    def check_win_or_lose(self):
        """Checks if the game should end based on score or time."""
        if self.score >= WIN_SCORE:
            self.state = GAME_STATES["GAME_OVER"]  # Win condition
