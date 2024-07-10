import customtkinter as ctk

class GameGUI:
    def __init__(self, game):
        self.game = game
        self.game.title("Clicker Game V0.0.0.1")
        self.game.geometry("800x600")
        self.game_frames()
        self.show_frame(self.menu_frame)
        self.setup_game_frames()
        self.game_screen()
        self.stats_screen()
        self.settings_screen()
        self.achievements_screen()
        self.shop_screen()


    def game_frames(self):
        self.menu_frame = ctk.CTkFrame(self.game)
        self.game_frame = ctk.CTkFrame(self.game)
        self.settings_frame = ctk.CTkFrame(self.game)
        self.stats_frame = ctk.CTkFrame(self.game)
        self.achievements_frame = ctk.CTkFrame(self.game)
        self.shop_frame = ctk.CTkFrame(self.game)

        for frame in (self.menu_frame, self.game_frame, self.settings_frame, self.stats_frame, self.achievements_frame,
                      self.shop_frame):
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_frame(self, frame):
        frame.tkraise()

    def setup_game_frames(self):
        large_main_font = ctk.CTkFont(family="Comic Sans MS", size=45, weight="bold")
        main_font = ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold")

        self.play_btn = ctk.CTkButton(self.menu_frame, text="Play", font=large_main_font,
                                      command=lambda: self.show_frame(self.game_frame))
        self.play_btn.place(relx=0.5, rely=0.3, anchor="center")

        self.stats_btn = ctk.CTkButton(self.menu_frame, text="Stats", font=large_main_font,
                                       command=lambda: self.show_frame(self.stats_frame))
        self.stats_btn.place(relx=0.5, rely=0.44, anchor="center")

        self.settings_btn = ctk.CTkButton(self.menu_frame, text="Settings", font=large_main_font,
                                          command=lambda: self.show_frame(self.settings_frame))
        self.settings_btn.place(relx=0.5, rely=0.58, anchor="center")

        self.achievements_btn = ctk.CTkButton(self.menu_frame, text="Achievements", font=large_main_font,
                                          command=lambda: self.show_frame(self.achievements_frame))
        self.achievements_btn.place(relx=0.5, rely=0.72, anchor="center")

        self.menu_btn = ctk.CTkButton(self.game_frame, text="Menu", font=large_main_font,
                                      command=lambda: self.show_frame(self.menu_frame))
        self.menu_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.shop_btn = ctk.CTkButton(self.game_frame, text="Shop", font=large_main_font,
                                      command=lambda: self.show_frame(self.shop_frame))
        self.shop_btn.place(relx=0.97, rely=0.97, anchor="se")

        self.shop_back_btn = ctk.CTkButton(self.shop_frame, text="Back", font=large_main_font,
                                      command=lambda: self.show_frame(self.game_frame))
        self.shop_back_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.stats_back_btn = ctk.CTkButton(self.stats_frame, text="Back", font=large_main_font,
                                      command=lambda: self.show_frame(self.menu_frame))
        self.stats_back_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.settings_back_btn = ctk.CTkButton(self.settings_frame, text="Back", font=large_main_font,
                                      command=lambda: self.show_frame(self.menu_frame))
        self.settings_back_btn.place(relx=0.2, rely=0.97, anchor="se")

        self.achievements_back_btn = ctk.CTkButton(self.achievements_frame, text="Back", font=large_main_font,
                                      command=lambda: self.show_frame(self.menu_frame))
        self.achievements_back_btn.place(relx=0.2, rely=0.97, anchor="se")

    def game_screen(self):
        main_font = ctk.CTkFont(family="Comic Sans MS", size=35, weight="bold")

        click_btn = ctk.CTkButton(self.game_frame, text="Click", font=main_font)

        click_btn.place(relx=0.5, rely=0.5, anchor="center")

        number_count = ctk.CTkLabel(self.game_frame, text="0", font=main_font)

        number_count.place(relx=0.5, rely=0.6, anchor="center")

    def stats_screen(self):
        main_font = ctk.CTkFont(family="Comic Sans MS", size=30, weight="bold")

        clicks_alltime = ctk.CTkLabel(self.stats_frame, text="Clicks all time: 0", font=main_font)

        clicks_alltime.place(relx=0.5, rely=0.3, anchor="center")

        current_time = ctk.CTkLabel(self.stats_frame, text="Current time: 0", font=main_font)

        current_time.place(relx=0.5, rely=0.4, anchor="center")

        total_time = ctk.CTkLabel(self.stats_frame, text="Total time: hrs: mins: secs", font=main_font)

        total_time.place(relx=0.5, rely=0.5, anchor="center")

    def settings_screen(self):
        main_font = ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold")

        settingslb = ctk.CTkLabel(self.settings_frame, text="Settings", font=main_font)

        settingslb.place(relx=0.5, rely=0.5, anchor="center")




    def achievements_screen(self):
        main_font = ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold")

        achievementlb = ctk.CTkLabel(self.achievements_frame, text="Achievements", font=main_font)

        achievementlb.place(relx=0.5, rely=0.5, anchor="center")

    def shop_screen(self):
        main_font = ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold")

        shoplb = ctk.CTkLabel(self.shop_frame, text="Shop", font=main_font)

        shoplb.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    print("GAME GUI RUNNING")
