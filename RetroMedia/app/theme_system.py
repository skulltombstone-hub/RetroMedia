from pathlib import Path

THEME_DIR = Path("themes")

current_theme = "default"

def load_theme(name):

    global current_theme

    current_theme = name

def get_theme_assets():

    return THEME_DIR / current_theme
