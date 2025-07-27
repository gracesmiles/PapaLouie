import pygame


class PauseMenu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.options = ["Resume", "Quit"]

    def draw(self, color=(128, 0, 128)):
        resume_surface = self.font.render("Resume", True, color)
        resume_rect = text_surface.get_rect(center=(400, 200))
        quit_surface = self.font.render("Resume", True, color)
        quit_rect = text_surface.get_rect(center=(400, 300))
        self.screen.blit(resume_surface, resume_rect)  
        self.screen.blit(quit_surface, quit_rect)
      
        
