import sqlite3

conn = sqlite3.connect(
    "database/retromedia.db"
)

cursor = conn.cursor()

def find_media(
    keyboard_id,
    keybind
):

    cursor.execute("""

    SELECT * FROM media

    WHERE keyboard_id=?
    AND keybind=?

    """, (keyboard_id, keybind))

    return cursor.fetchone()
