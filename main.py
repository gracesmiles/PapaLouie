import pygame
import random  # Import Random Module
from settings import SETTINGS , GAME_STATES  # Import game settings, game states, and win score
from classes.player import Player # Import player from the player class
from classes.platform import Platform # Import Platform from the platform class
from classes.camera import Camera  # Import Camera
from classes.game import Game  # Import Game Manager
from classes.ui import UI # Import UI Elements
from classes.collectible import Coin  # Import coin from collectible class
from classes.level_manager import LevelManager  # Import LevelManager


# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Play Background Music
pygame.mixer.music.load("assets/audios/background_music.mp3")
pygame.mixer.music.set_volume(0.5)  # Optional: volume 0.0 to 1.0
pygame.mixer.music.play(loops=-1)

# Create the game window
screen = pygame.display.set_mode((SETTINGS["WIDTH"], SETTINGS["HEIGHT"]))
pygame.display.set_caption(SETTINGS["TITLE"])

# Load the background image
background = pygame.image.load(SETTINGS["BG_IMAGE"])

# Create player instance and game objects
spawn_x = 100
spawn_y = 200
player = Player(spawn_x, spawn_y)  # Starting position
game = Game()
ui = UI(screen)
level_manager = LevelManager("level_1")

# Pause menu state
paused = False
p_key_pressed = False  # Track if P key was pressed to prevent multiple toggles

# Sundae smash state
sundae_smash_available = False
s_key_pressed = False  # Track if S key was pressed to prevent multiple activations

# Create collectible group
collectibles = pygame.sprite.Group()
for _ in range(5):  # Spawn 5 random collectibles
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    if random.choice([True, False]):
        collectibles.add(Coin(x, y))

# Create Camera instance
camera = Camera(SETTINGS["WIDTH"] + 1000, SETTINGS["HEIGHT"])  # Extend world horizontally to accommodate all level content

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()  # Detect key presses

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game.state == GAME_STATES["MENU"] and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.set_state(GAME_STATES["PLAYING"])

        if game.state == GAME_STATES["GAME_OVER"] and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()

                # Reset game state
                level_manager = LevelManager("level_1")  # Restart at level 1
                player.rect.topleft = (100, 200)
                sundae_smash_available = False  # Reset sundae smash

        # Handle pause menu toggle
        if game.state == GAME_STATES["PLAYING"] and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not p_key_pressed:
                paused = not paused
                p_key_pressed = True
            
            # Handle sundae smash activation
            if event.key == pygame.K_s and sundae_smash_available and not s_key_pressed:
                # Kill all enemies in camera view
                enemies_killed = False
                for enemy in list(level_manager.enemies):
                    if camera.camera.colliderect(enemy.rect):
                        enemy.kill()
                        enemies_killed = True
                if enemies_killed:
                    sundae_smash_available = False  # Use up the sundae smash
                s_key_pressed = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                p_key_pressed = False
            if event.key == pygame.K_s:
                s_key_pressed = False

        # Handle pause menu button clicks
        if paused and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            resume_rect, restart_rect = ui.get_pause_menu_buttons()
            
            if resume_rect.collidepoint(mouse_pos):
                paused = False
            elif restart_rect.collidepoint(mouse_pos):
                # Restart the game
                game.reset()
                level_manager = LevelManager("level_1")
                player.rect.topleft = (spawn_x, spawn_y)
                paused = False
                sundae_smash_available = False  # Reset sundae smash

    screen.fill(SETTINGS["BG_COLOR"])  
    bg_x = -camera.camera.x  # Camera follows horizontally
    bg_y = SETTINGS["HEIGHT"] - background.get_height() - camera.camera.y  # Align bottom vertically
    screen.blit(background, (bg_x, bg_y))

    if game.state == GAME_STATES["MENU"]:
        ui.draw_menu()

    elif game.state == GAME_STATES["PLAYING"]:
        if not paused:
            player.prev_rect = player.rect.copy()
            player.move(keys) 
            player.apply_gravity(level_manager.platforms)  # Use platforms from LevelManager

            # Check if player fell off screen
            if player.rect.top > SETTINGS["HEIGHT"]:
                if game.lose_life():
                    pass
                else:
                    player.rect.topleft = (spawn_x, spawn_y)
                    player.vel_y = 0
                    player.on_ground = False

            # Update camera to follow player and Update moving platforms
            camera.update(player)
            level_manager.platforms.update()  # Now we update the platforms using the Level Manager
            level_manager.update_enemies()  # Update enemies with platform info
      
            # Detect collisions with collectibles (coins)
            collected = pygame.sprite.spritecollide(player, level_manager.collectibles, True)
            for item in collected:
                game.collect_coin(item.points)
            
            # Check if all coins are collected (8 coins total)
            if len(level_manager.collectibles) == 0 and not sundae_smash_available:
                sundae_smash_available = True

            # Detect collisions with enemies
            enemy_hit = pygame.sprite.spritecollide(player, level_manager.enemies, False)
            enemies_to_kill = []
            MARGIN = 25
            
            if enemy_hit:
                # Check if player is jumping on enemy (player's bottom is above enemy's top)
                for enemy in enemy_hit:
                    player_bottom = player.rect.bottom
                    enemy_center_y = enemy.rect.centery
                    
                    if player.rect.bottom <= enemy.rect.top + MARGIN and player.vel_y > 0:
                        enemy.fade()
                        enemies_to_kill.append(enemy)
                        player.vel_y = -8    # player bounces
                    else:
                        # Player hit enemy from side - lose life
                        if game.lose_life():
                            pass
                        else:
                            player.rect.topleft = (spawn_x, spawn_y)
                            player.vel_y = 0
                            player.on_ground = False

                for enemy in enemies_to_kill:
                    enemy.kill() # Player jumped on enemy - kill enemy

        # Draw the player with camera offset and UI elements
        screen.blit(player.image, camera.apply(player))
        ui.draw_score(game.score)
        ui.draw_lives(game.lives)

        # Draw sundae smash indicator if available
        if sundae_smash_available:
            ui.draw_sundae_smash_indicator()

        # Draw platforms with camera offset
        for platform in level_manager.platforms:
            screen.blit(platform.image, camera.apply(platform))

        for collectible in level_manager.collectibles:  # Apply camera movement to collectibles
            screen.blit(collectible.image, camera.apply(collectible))

        # Draw enemies with camera offset
        for enemy in level_manager.enemies:
            screen.blit(enemy.image, camera.apply(enemy))

        # Draw pause menu if paused
        if paused:
            ui.draw_pause_menu()

    elif game.state == GAME_STATES["GAME_OVER"]:
        ui.draw_game_over(game.score, game.lives > 0)

    pygame.display.flip()

pygame.quit()
