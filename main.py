import customtkinter as ctk
import json
import time
from pathlib import Path


class ClickerGame:
    def __init__(self, gamecontroller, savefile):
        self.gamecontroller = gamecontroller
        self.savefile = savefile
        self.app = ctk.CTk()
        self.app.title("Clicker Game V0.0.0.1")
        self.app.geometry("800x600")
        self.app.resizable(False, False)
        self.game_frames()
        self.show_frame(self.menu_frame)
        self.setup_game_frames()
        self.game_screen()
        self.stats_screen()
        self.settings_screen()
        self.achievements_screen()
        self.shop_screen()
        self.run()

    def game_frames(self):
        self.menu_frame = ctk.CTkFrame(self.app)
        self.game_frame = ctk.CTkFrame(self.app)
        self.settings_frame = ctk.CTkFrame(self.app)
        self.stats_frame = ctk.CTkFrame(self.app)
        self.achievements_frame = ctk.CTkFrame(self.app)
        self.shop_frame = ctk.CTkFrame(self.app)

        for frame in (self.menu_frame, self.game_frame, self.settings_frame, self.stats_frame, self.achievements_frame,
                      self.shop_frame):
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_frame(self, frame):
        frame.tkraise()

    def setup_game_frames(self):
        self.large_main_font = ctk.CTkFont(family="Comic Sans MS", size=45, weight="bold")
        self.main_font = ctk.CTkFont(family="Comic Sans MS", size=30, weight="bold")

        self.play_btn = ctk.CTkButton(self.menu_frame, text="Play", font=self.large_main_font,
                                      command=lambda: self.show_frame(self.game_frame))
        self.play_btn.place(relx=0.5, rely=0.3, anchor="center")

        self.stats_btn = ctk.CTkButton(self.menu_frame, text="Stats", font=self.large_main_font,
                                       command=lambda: self.show_frame(self.stats_frame))
        self.stats_btn.place(relx=0.5, rely=0.44, anchor="center")

        self.settings_btn = ctk.CTkButton(self.menu_frame, text="Settings", font=self.large_main_font,
                                          command=lambda: self.show_frame(self.settings_frame))
        self.settings_btn.place(relx=0.5, rely=0.58, anchor="center")

        self.achievements_btn = ctk.CTkButton(self.menu_frame, text="Achievements", font=self.large_main_font,
                                              command=lambda: self.show_frame(self.achievements_frame))
        self.achievements_btn.place(relx=0.5, rely=0.72, anchor="center")

        self.menu_btn = ctk.CTkButton(self.game_frame, text="Menu", font=self.large_main_font,
                                      command=lambda: self.show_frame(self.menu_frame))
        self.menu_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.shop_btn = ctk.CTkButton(self.game_frame, text="Shop", font=self.large_main_font,
                                      command=lambda: self.show_frame(self.shop_frame))
        self.shop_btn.place(relx=0.97, rely=0.97, anchor="se")

        self.shop_back_btn = ctk.CTkButton(self.shop_frame, text="Back", font=self.large_main_font,
                                           command=lambda: self.show_frame(self.game_frame))
        self.shop_back_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.stats_back_btn = ctk.CTkButton(self.stats_frame, text="Back", font=self.large_main_font,
                                            command=lambda: self.show_frame(self.menu_frame))
        self.stats_back_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.settings_back_btn = ctk.CTkButton(self.settings_frame, text="Back", font=self.large_main_font,
                                               command=lambda: self.show_frame(self.menu_frame))
        self.settings_back_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.achievements_back_btn = ctk.CTkButton(self.achievements_frame, text="Back", font=self.large_main_font,
                                                   command=lambda: self.show_frame(self.menu_frame))
        self.achievements_back_btn.place(relx=0.2, rely=0.97, anchor="se")

    def game_screen(self):
        self.main_font = ctk.CTkFont(family="Comic Sans MS", size=35, weight="bold")

        self.click_btn = ctk.CTkButton(self.game_frame, text="Click", font=self.main_font,
                                       command=self.gamecontroller.clickbtn_event)

        self.click_btn.place(relx=0.5, rely=0.5, anchor="center")

        self.number_count = ctk.CTkLabel(self.game_frame, text="0", font=self.main_font)

        self.number_count.place(relx=0.5, rely=0.6, anchor="center")

    def stats_screen(self):
        self.clicks_alltime = ctk.CTkLabel(self.stats_frame, text=f"Total clicks: 0", font=self.main_font)

        self.clicks_alltime.place(relx=0.5, rely=0.3, anchor="center")

        self.current_time = ctk.CTkLabel(self.stats_frame, text="Current time: 0", font=self.main_font)

        self.current_time.place(relx=0.5, rely=0.4, anchor="center")

        self.total_time = ctk.CTkLabel(self.stats_frame, text="Total time: %H: %M: %S", font=self.main_font)

        self.total_time.place(relx=0.5, rely=0.5, anchor="center")

    def settings_screen(self):
        self.settingslb = ctk.CTkLabel(self.settings_frame, text="Settings", font=self.main_font)

        self.settingslb.place(relx=0.5, rely=0.5, anchor="center")

    def achievements_screen(self):
        self.achievementlb = ctk.CTkLabel(self.achievements_frame, text="Achievements", font=self.main_font)

        self.achievementlb.place(relx=0.5, rely=0.5, anchor="center")

    def shop_screen(self):
        self.shoplb = ctk.CTkLabel(self.shop_frame, text="Shop", font=self.main_font)

        self.shoplb.place(relx=0.5, rely=0.5, anchor="center")

    def run(self):
        self.app.mainloop()


class GameController:
    def __init__(self, savefile, clickergame):
        self.clickergame = clickergame
        self.savefile = savefile
        self.load_data()

    def load_data(self):
        data = self.savefile.grab_data()
        self.time_open = data['time_open']
        self.clicks = data['clicks']
        self.total_time = data['total_time']
        self.running_time = data['running_time']
        self.gold = data['gold']
        self.autoclickers = data['autoclickers']

    def update_data(self):
        self.savefile.time_open = self.time_open
        self.savefile.clicks = self.clicks
        self.savefile.total_time = self.total_time
        self.savefile.running_time = self.running_time
        self.savefile.gold = self.gold
        self.savefile.autoclickers = self.autoclickers
        self.savefile.save()

    def clickbtn_event(self):
        self.clicks += 1
        self.config_update()

    def config_update(self):
        self.clickergame.number_count.configure(text=f'{self.clicks}')


class SaveFile:
    def __init__(self, filename='savefile.json'):
        self.filename = filename
        self.time_open = 0
        self.clicks = 0
        self.total_time = 0
        self.running_time = time.time()
        self.gold = 0
        self.autoclickers = 0

    def save(self):
        data = {
            'time_open': self.time_open,
            'clicks': self.clicks,
            'total_time': self.total_time,
            'running_time': self.running_time,
            'gold': self.gold,
            'autoclickers': self.autoclickers
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load(self):
        if Path(self.filename).is_file():
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.time_open = data['time_open']
                self.clicks = data['clicks']
                self.total_time = data['total_time']
                self.running_time = data['running_time']
                self.gold = data['gold']
                self.autoclickers = data['autoclickers']
        else:
            print(f"No save file found at {self.filename}. Starting with default values.")

    def grab_data(self):
        return {
            'time_open': self.time_open,
            'clicks': self.clicks,
            'total_time': self.total_time,
            'running_time': self.running_time,
            'gold': self.gold,
            'autoclickers': self.autoclickers
        }


if __name__ == "__main__":
    app = ClickerGame()
    app.run()