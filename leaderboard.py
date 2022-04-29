from tkinter import *
import math

BG_COLOR = "grey3"
TEXT_COLOR = "white"
KEYBOARD_FONT = ("Terminal", 8, "normal")


class Leaderboard:

    def __init__(self, key_layout: list):
        self.leaderboard_frame = Frame(
            padx=5,
            pady=5,
            bg=BG_COLOR
        )

        self.COLUMNS = 3
        
        self.all_keys = {}
        for row in key_layout:
            self.all_keys.update(row)
        self.sorted_keys = dict(sorted(self.all_keys.items(), key=lambda item: item[1]["percent"], reverse=True))
        self.leaderboard_text = []
        pos = 0
        for name, data in self.sorted_keys.items():
            if (name != "SHIFT_2" and name != "CTRL_2") and data["percent"] != 0:
                pos += 1
                self.leaderboard_text.append(f"{pos}. '{data['normal']}', {data['count']} instances, " \
                                         f"{data['percent'] * 100:.2f}% relative to '{list(self.sorted_keys.keys())[0]}'\n")

        leaderboard_length = len(self.leaderboard_text)
        column_size = math.ceil(leaderboard_length / self.COLUMNS)
        rank_total = 0
        for column in range(self.COLUMNS):
            for row in range(column_size):
                if rank_total < leaderboard_length:
                    leaderboard_label = Label(text=self.leaderboard_text[rank_total], fg=TEXT_COLOR, font=KEYBOARD_FONT, bg=BG_COLOR, padx=10, pady=0)
                    leaderboard_label.grid(in_=self.leaderboard_frame, sticky="W", row=row, column=column)
                    rank_total += 1
