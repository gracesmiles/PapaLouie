"""
Menus, start screen, health bar, rescued counter
"""

import pygame


class UI:
    def __init__(self, screen):
        """Initialize fonts and screen reference."""
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.match_font("Arial"), 22)  # Use modern font

    def draw_text(self, text, x, y, color=(0, 0, 128), center=True):
        """Renders and displays text on the screen, centered if needed."""
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y)) if center else (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_menu(self):
        """Displays the main menu text."""
        self.draw_text("PAPA LOUIE", 400, 200, (0, 0, 128))  # Dark blue title
        self.draw_text("Press SPACE to Start", 400, 300, (50, 50, 50))  # Dark gray instructions

    def draw_game_over(self, score, win_condition):
        """Displays the game over text."""
        message = "You Win!" if win_condition else "Game Over"
        color = (0, 128, 0) if win_condition else (200, 0, 0)  # Green for win, red for lose
        self.draw_text(message, 400, 250, color)
        self.draw_text(f"Final Score: {score}", 400, 320, (50, 50, 50))  # Dark gray score
        self.draw_text("Press R to Restart", 400, 400, (0, 0, 128))  # Dark blue restart prompt

    def draw_score(self, score):
        """Displays the current score and timer."""
        self.draw_text(f"Score: {score}", 50, 40, (0, 0, 0), center=False)  # Black text, top left

    def draw_hud(self, level_name, score):
        """Displays the level, score, and timer on the HUD."""
        self.draw_text(f"Level: {level_name}", 50, 10, (0, 0, 0), center=False)  # Level text
        self.draw_text(f"Score: {score}", 50, 40, (0, 0, 0), center=False)  # Score text

    def draw(self, color=(128, 0, 128)):
        self.options = ["Resume", "Quit"]
        resume_surface = self.font.render("Resume", True, color)
        resume_rect = text_surface.get_rect(center=(400, 200))
        quit_surface = self.font.render("Quit", True, color)
        quit_rect = text_surface.get_rect(center=(400, 300))
        self.screen.blit(resume_surface, resume_rect)  
        self.screen.blit(quit_surface, quit_rect)
