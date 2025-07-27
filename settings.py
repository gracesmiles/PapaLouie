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
    "speed": 1,         # How fast the player moves left/right
    "jump_power": 12,   # How high the player jumps
    "gravity": 0.7,     # Strength of gravity pulling the player down
}

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
        "speed": 1
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
    "GAME_OVER": "game_over"
}

COLLECTIBLES = {
    "heart": {
        "image": "assets/images/heart.png",
        "points": 1  # Increases score by 10
    }
}

LEVELS = {
    "level_1": {
        "platforms": [
            {"x": 200, "y": 400, "type": "licorice_normal"},
            {"x": 400, "y": 300, "type": "licorice_moving"},
            {"x": 800, "y": 200, "type": "licorice_normal"},
            {"x": 1000, "y": 350, "type": "licorice_normal"},
            {"x": 0, "y": 550, "type": "platform01"},
            {"x": 110, "y": 550, "type": "platform01"},
            {"x": 220, "y": 550, "type": "platform01"},
            {"x": 400, "y": 550, "type": "platform01"}
        ],
        "collectibles": [
            {"x": 250, "y": 370, "type": "heart"},
            {"x": 450, "y": 270, "type": "heart"},
            {"x": 650, "y": 170, "type": "heart"},
            {"x": 550, "y": 470, "type": "heart"},
            {"x": 1100, "y": 300, "type": "heart"}
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
            {"x": 230, "y": 470, "type": "heart"},
            {"x": 320, "y": 370, "type": "heart"},
            {"x": 520, "y": 270, "type": "heart"},
            {"x": 720, "y": 170, "type": "heart"}
        ]
    }
}
