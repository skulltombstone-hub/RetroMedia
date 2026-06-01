import customtkinter as ctk

class SetupWizard(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            "RetroMedia Setup Wizard"
        )

        self.geometry("900x700")
