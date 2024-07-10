import customtkinter as ctk
import game_gui as GUI

class ClickerGame:
    def __init__(self):
        self.game = ctk.CTk()
        self.GUI = GUI.GameGUI(self.game)
    def run(self):
        self.game.mainloop()

if __name__ == "__main__":
    game = ClickerGame()
    game.run()