from pynput import keyboard

registered_keys = {}

def register_key(key_name, callback):
    registered_keys[key_name] = callback

def on_press(key):
    try:
        k = key.char
    except:
        k = str(key)

    if k in registered_keys:
        registered_keys[k]()

listener = keyboard.Listener(on_press=on_press)
listener.start()
