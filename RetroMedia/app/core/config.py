from pathlib import Path

ROOT = Path.cwd()

MEDIA_DIR = ROOT / "media"

CONFIG_DIR = ROOT / "config"

THEMES_DIR = ROOT / "themes"

CACHE_DIR = ROOT / "cache"

DATABASE_DIR = ROOT / "database"

SUPPORTED_VIDEO = [
    ".mp4",
    ".mkv",
    ".avi",
    ".mov"
]

SUPPORTED_AUDIO = [
    ".mp3",
    ".flac",
    ".wav"
]

SUPPORTED_BOOKS = [
    ".pdf"
]
