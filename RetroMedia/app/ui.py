import customtkinter as ctk
from tkinter import filedialog

from media_manager import create_media_entry

class RetroMediaUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("RetroMedia")

        self.geometry("800x600")

        add_button = ctk.CTkButton(
            self,
            text="Adicionar mídia",
            command=self.add_media
        )

        add_button.pack(pady=20)

    def add_media(self):

        files = filedialog.askopenfilenames()

        create_media_entry(
            title="Nova Midia",
            category="Movies",
            media_files=files,
            keybind="f1",
            keyboard_id="KEYBOARD_1"
        )
