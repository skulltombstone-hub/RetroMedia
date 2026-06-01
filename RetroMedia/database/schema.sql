CREATE TABLE IF NOT EXISTS media (

    id INTEGER PRIMARY KEY,

    title TEXT,
    category TEXT,

    keyboard_id TEXT,
    keybind TEXT,

    media_path TEXT,
    intro_path TEXT,
    poster_path TEXT,

    autoplay INTEGER,
    delay_intro INTEGER,
    delay_start INTEGER,

    media_type TEXT
);
