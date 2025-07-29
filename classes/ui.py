"""
Menus, start screen, health bar, rescued counter
"""

import pygame


class UI:
    def __init__(self, screen):
        """Initialize fonts and screen reference."""
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.match_font("Arial"), 22)  # Use modern font
        self.large_font = pygame.font.Font(pygame.font.match_font("Arial"), 32)  # Larger font for titles

    def draw_text(self, text, x, y, color=(0, 0, 128), center=True):
        """Renders and displays text on the screen, centered if needed."""
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y)) if center else (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_menu(self):
        """Displays the main menu with a professional design."""
        # Create semi-transparent black background
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(128)  # 50% transparency
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Draw menu background
        menu_rect = pygame.Rect(200, 150, 400, 300)
        pygame.draw.rect(self.screen, (50, 50, 50), menu_rect)  # Dark gray background
        pygame.draw.rect(self.screen, (100, 100, 100), menu_rect, 3)  # Border
        
        # Draw title
        title_surface = self.large_font.render("PAPA LOUIE", True, (255, 215, 0))  # Gold color
        title_rect = title_surface.get_rect(center=(400, 200))
        self.screen.blit(title_surface, title_rect)
        
        # Draw start button
        start_rect = pygame.Rect(275, 360, 250, 40)
        pygame.draw.rect(self.screen, (0, 128, 0), start_rect)  # Green button
        pygame.draw.rect(self.screen, (255, 255, 255), start_rect, 2)  # White border
        
        start_text = self.font.render("Press SPACE to Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=(400, 380))
        self.screen.blit(start_text, start_text_rect)

        # Draw instructions
        #instructions_rect = pygame.Rect(275, 260, 250, 40)
        instructions_txt1 = self.font.render("Use left and right arrow keys to move", True, (255, 255, 255))
        instructions_txt2 = self.font.render("Use the space bar to jump", True, (255, 255, 255))
        instructions_txt1_rect = instructions_txt1.get_rect(center=(400, 270))
        instructions_txt2_rect = instructions_txt2.get_rect(center=(400, 310))
        self.screen.blit(instructions_txt1, instructions_txt1_rect)
        self.screen.blit(instructions_txt2, instructions_txt2_rect)
    

    def draw_sundae_smash_indicator(self):
        """Draws the sundae smash indicator in the top right corner."""
        # Create background for the indicator
        indicator_rect = pygame.Rect(600, 20, 180, 60)
        pygame.draw.rect(self.screen, (255, 165, 0), indicator_rect)  # Orange background
        pygame.draw.rect(self.screen, (255, 255, 255), indicator_rect, 2)  # White border
        
        # Draw "SUNDAE SMASH" text
        smash_text = self.font.render("SUNDAE SMASH", True, (255, 255, 255))
        smash_rect = smash_text.get_rect(center=(690, 35))
        self.screen.blit(smash_text, smash_rect)
        
        # Draw "Press S" text
        press_text = self.font.render("Press S", True, (255, 255, 255))
        press_rect = press_text.get_rect(center=(690, 55))
        self.screen.blit(press_text, press_rect)

    def draw_game_over(self, score, win_condition):
        """Displays the game over menu with a professional design."""
        # Create semi-transparent black background
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(128)  # 50% transparency
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Draw menu background
        menu_rect = pygame.Rect(200, 150, 400, 300)
        pygame.draw.rect(self.screen, (50, 50, 50), menu_rect)  # Dark gray background
        pygame.draw.rect(self.screen, (100, 100, 100), menu_rect, 3)  # Border
        
        # Draw title
        message = "You Win!" if win_condition else "Game Over"
        color = (0, 255, 0) if win_condition else (255, 0, 0)  # Green for win, red for lose
        title_surface = self.large_font.render(message, True, color)
        title_rect = title_surface.get_rect(center=(400, 200))
        self.screen.blit(title_surface, title_rect)
        
        # Draw score
        score_text = self.font.render(f"Final Coins: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(400, 250))
        self.screen.blit(score_text, score_rect)
        
        # Draw restart button
        restart_rect = pygame.Rect(300, 300, 200, 40)
        pygame.draw.rect(self.screen, (0, 128, 0), restart_rect)  # Green button
        pygame.draw.rect(self.screen, (255, 255, 255), restart_rect, 2)  # White border
        
        restart_text = self.font.render("Press R to Restart", True, (255, 255, 255))
        restart_text_rect = restart_text.get_rect(center=(400, 320))
        self.screen.blit(restart_text, restart_text_rect)

    def draw_score(self, score):
        """Displays the current coin count."""
        self.draw_text(f"Coins: {score}", 50, 40, (255, 215, 0), center=False)  # Gold text, top left

    def draw_lives(self, lives):
        """Displays the current lives."""
        self.draw_text(f"Lives: {lives}", 50, 70, (200, 0, 0), center=False)  # Red text, below score

    def draw_hud(self, level_name, score, lives):
        """Displays the level, score, and lives on the HUD."""
        self.draw_text(f"Level: {level_name}", 50, 10, (0, 0, 0), center=False)  # Level text
        self.draw_text(f"Coins: {score}", 50, 40, (255, 215, 0), center=False)  # Coin text
        self.draw_text(f"Lives: {lives}", 50, 70, (200, 0, 0), center=False)  # Lives text

    def get_pause_menu_buttons(self):
        """Returns the button rectangles for the pause menu without drawing."""
        resume_rect = pygame.Rect(300, 280, 200, 40)
        restart_rect = pygame.Rect(300, 330, 200, 40)
        return resume_rect, restart_rect

    def draw_pause_menu(self):
        """Draws a proper pause menu with background and clickable buttons."""
        # Create semi-transparent black background
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(128)  # 50% transparency
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Draw menu background
        menu_rect = pygame.Rect(250, 200, 300, 200)
        pygame.draw.rect(self.screen, (50, 50, 50), menu_rect)  # Dark gray background
        pygame.draw.rect(self.screen, (100, 100, 100), menu_rect, 3)  # Border
        
        # Draw title
        title_surface = self.large_font.render("PAUSED", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(400, 230))
        self.screen.blit(title_surface, title_rect)
        
        # Draw Resume button
        resume_rect = pygame.Rect(300, 280, 200, 40)
        pygame.draw.rect(self.screen, (0, 128, 0), resume_rect)  # Green button
        pygame.draw.rect(self.screen, (255, 255, 255), resume_rect, 2)  # White border
        
        resume_text = self.font.render("Resume", True, (255, 255, 255))
        resume_text_rect = resume_text.get_rect(center=(400, 300))
        self.screen.blit(resume_text, resume_text_rect)
        
        # Draw Restart button
        restart_rect = pygame.Rect(300, 330, 200, 40)
        pygame.draw.rect(self.screen, (255, 165, 0), restart_rect)  # Orange button
        pygame.draw.rect(self.screen, (255, 255, 255), restart_rect, 2)  # White border
        
        restart_text = self.font.render("Restart", True, (255, 255, 255))
        restart_text_rect = restart_text.get_rect(center=(400, 350))
        self.screen.blit(restart_text, restart_text_rect)
