from tkinter import *
from keyboard import Keyboard
from functions import add_key_count_stats
from leaderboard import Leaderboard

BG_COLOR = "grey3"


class Window:

    def __init__(self, keyboard_layout_type: str, file_to_examine: str, track_shift: bool, key_color_activated: tuple):
        """
        :param keyboard_layout_type: Specify a keyboard type. Use: "us"
        """

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=BG_COLOR)
        self.window.title(f"Keyboard Heatmap (./txts/{file_to_examine})")

        self.track_shift = track_shift
        self.file_to_examine = file_to_examine
        self.key_color_activated = key_color_activated

        self.keyboard_layout_type = keyboard_layout_type
        if self.keyboard_layout_type == "us":
            self.keyboard_layout = add_key_count_stats(self.file_to_examine, "us", self.track_shift)
        else:
            self.keyboard_layout = add_key_count_stats(self.file_to_examine, "us", self.track_shift)

        self.keyboard = Keyboard(self.keyboard_layout, self.key_color_activated)
        self.keyboard.keyboard_frame.grid(row=0, column=0)

        self.leaderboard = Leaderboard(self.keyboard_layout)
        self.leaderboard.leaderboard_frame.grid(sticky="W", row=1, column=0)

        self.window.mainloop()
