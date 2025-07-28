from PIL import Image

"""
Game settings (FPS, screen size, colors, etc.)
"""

SETTINGS = {
    "WIDTH": 800,       # Game window width
    "HEIGHT": 600,      # Game window height
    "FPS": 80,          # Frames per second
    "BG_COLOR": (135, 206, 235),  # Light blue background
    "TITLE": "Simple Platformer",  # Window title
    "BG_IMAGE": "assets/images/background.jpg"
}

PLAYER_SETTINGS = {
    "speed": 2,         # How fast the player moves left/right (increased for responsiveness)
    "jump_power": 12,   # How high the player jumps (reduced from 18)
    "gravity": 0.9,     # Strength of gravity pulling the player down (reduced from 0.7)
} 

# Transform Images
# Make licorice image horizontal rather than vertical
img_licorice = Image.open("assets/images/red_licorice.png")
licorice = img_licorice.rotate(-90, expand=True)
licorice.save("assets/images/horizontal_red_licorice.png")

PLATFORM_SETTINGS = {
    "licorice_normal": {
        "image": "assets/images/horizontal_red_licorice.png",
        "width": 100,
        "height": 20
    },
    "licorice_moving": {
        "image": "assets/images/horizontal_red_licorice.png",
        "width": 120,
        "height": 20,
        "speed": 0.1  # Reduced from 1
    },
    "platform01": {
        "image": "assets/images/platform01.png",
        "width": 120,
        "height": 50
    }
}

GAME_STATES = {
    "MENU": "menu",
    "PLAYING": "playing",
    "GAME_OVER": "game_over",
    "PAUSED": "paused"
}

COLLECTIBLES = {
    "coin": {
        "image": "assets/images/coin.webp",
        "points": 1  # Increases score by 1
    }
}

ENEMY_SETTINGS = {
    "basic_enemy": {
        "image": "assets/images/enemy.png",
        "speed": 2,
        "health": 1
    },
    "fast_enemy": {
        "image": "assets/images/enemy.png", 
        "speed": 4,
        "health": 1
    }
}

LEVELS = {
    "level_1": {
        "platforms": [
            # Ground platforms
            {"x": 0, "y": 550, "type": "platform01"},
            {"x": 110, "y": 550, "type": "platform01"},
            {"x": 220, "y": 550, "type": "platform01"},
            {"x": 400, "y": 550, "type": "platform01"},
            {"x": 600, "y": 550, "type": "platform01"},
            {"x": 800, "y": 550, "type": "platform01"},
            {"x": 1000, "y": 550, "type": "platform01"},
            {"x": 1200, "y": 550, "type": "platform01"},
            {"x": 1400, "y": 550, "type": "platform01"},
            {"x": 1600, "y": 550, "type": "platform01"},
            
            # 8 Licorice platforms (reduced from 16)
            {"x": 200, "y": 400, "type": "licorice_normal"},
            {"x": 400, "y": 300, "type": "licorice_moving"},
            {"x": 600, "y": 350, "type": "licorice_normal"},
            {"x": 800, "y": 200, "type": "licorice_normal"},
            {"x": 1000, "y": 350, "type": "licorice_normal"},
            {"x": 1200, "y": 250, "type": "licorice_moving"},
            {"x": 1400, "y": 300, "type": "licorice_normal"},
            {"x": 1600, "y": 200, "type": "licorice_normal"}
        ],
        "collectibles": [
            # 8 coins, one on each licorice platform
            {"x": 250, "y": 370, "type": "coin"},
            {"x": 450, "y": 270, "type": "coin"},
            {"x": 650, "y": 320, "type": "coin"},
            {"x": 850, "y": 170, "type": "coin"},
            {"x": 1050, "y": 320, "type": "coin"},
            {"x": 1250, "y": 220, "type": "coin"},
            {"x": 1450, "y": 270, "type": "coin"},
            {"x": 1650, "y": 170, "type": "coin"}
        ],
        "enemies": [
            {"x": 450, "y": 510, "type": "basic_enemy"},   # On ground platform (away from start)
            {"x": 750, "y": 510, "type": "fast_enemy"},    # On ground platform
            {"x": 1050, "y": 510, "type": "basic_enemy"},  # On ground platform
            {"x": 1350, "y": 510, "type": "fast_enemy"},   # On ground platform
            {"x": 1650, "y": 510, "type": "basic_enemy"}   # On ground platform
        ]
    },
    "level_2": {
        "platforms": [
            {"x": 100, "y": 500, "type": "licorice_normal"},
            {"x": 300, "y": 400, "type": "licorice_moving"},
            {"x": 500, "y": 300, "type": "licorice_normal"},
            {"x": 700, "y": 200, "type": "licorice_normal"}
        ],
        "collectibles": [
            {"x": 230, "y": 470, "type": "coin"},
            {"x": 320, "y": 370, "type": "coin"},
            {"x": 520, "y": 270, "type": "coin"},
            {"x": 720, "y": 170, "type": "coin"}
        ]
    }
}

