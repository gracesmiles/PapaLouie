import pygame
from settings import GAME_STATES

class Game:
    def __init__(self):
        """Initializes the game state, score, timer, and lives."""
        self.state = GAME_STATES["MENU"]  # Start in the menu
        self.score = 0  # Player's score (coins)
        self.start_time = None  # Track when the game starts
        self.lives = 3  # Player's lives
        self.coin_effect = pygame.mixer.Sound("assets/audios/coin_collected.wav")

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
        self.lives = 3

    # ✅ Add reset timer method
    def reset_timer(self):
        """Resets the timer to the full allotted time."""
        self.start_time = pygame.time.get_ticks()

    def increase_score(self, amount=1):
        """Increases the player's score (coins)."""
        self.score += amount

    def collect_coin(self, amount=1):
        """Increases the player's coin count and plays sound"""
        self.coin_effect.play()
        self.score += amount

    def draw_red_flash(self, duration=500, alpha=150):
        self.overlay.set_alpha(alpha)
        self.screen.blit(self.overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration)
    
    def lose_life(self):
        """Decreases the player's life and checks for game over."""
        self.lives -= 1
        self.draw_red_flash()
        if self.lives <= 0:
            self.state = GAME_STATES["GAME_OVER"]
            return True  # Game over
        return False  # Still alive

    def check_win_or_lose(self):
        """Checks if the game should end based on score or time."""
        # Remove automatic win condition - let player play until they lose all lives
        pass
