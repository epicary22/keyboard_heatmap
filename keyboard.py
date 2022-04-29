from tkinter import *
from key import Key
from functions import rgb_tuple_to_hex, color_between, add_key_count_stats, COLORS
import keyboard_layouts
import math

KEY_COLOR_BASE = COLORS["BLACK"]
KEY_COLOR_ACTIVATED = COLORS["RED"]
BG_COLOR = "grey3"
TEXT_COLOR = "white"
KEYBOARD_FONT = ("Terminal", 10, "normal")


class Keyboard:

    def __init__(self, key_layout: list, key_color_activated: tuple):  # , keys: list[Key]):
        """
        :param layout_type: Specify a keyboard type. Use: "us"
        """
        self.key_color_activated = key_color_activated

        self.key_layout = key_layout
        self.SIZE_MULTIPLIER = 2
        self.keyboard_frame = Frame(
            height=5*self.SIZE_MULTIPLIER,
            width=15*self.SIZE_MULTIPLIER,
            pady=5,
            padx=5,
            bg=BG_COLOR
        )
        self.assemble_keyboard()

    def assemble_keyboard(self) -> None:
        row_num = 0
        for row in self.key_layout:
            column_num = 0
            row_frame = Frame()
            for key in row.items():
                key_name = key[0]
                key_data = key[1]
                key_button = Button(
                    text="",
                    font=KEYBOARD_FONT,
                    fg=TEXT_COLOR,
                    bg=rgb_tuple_to_hex(color_between(KEY_COLOR_BASE, self.key_color_activated, key_data["percent"])),
                    width=math.floor(key_data["length"] * self.SIZE_MULTIPLIER),
                    height=math.floor(self.SIZE_MULTIPLIER / 1.5),
                    highlightthickness=0
                )
                if not key_name.isupper() and key_name.isalpha():
                    key_button.config(text=f"{key_data['shift']}")
                elif not key_name.isupper():
                    key_button.config(text=f"{key_data['normal']}{key_data['shift']}")
                else:
                    key_button.config(text=f"{key_data['normal']}")
                key_button.grid(in_=row_frame, row=row_num, column=column_num)
                column_num += 1
            row_frame.grid(in_=self.keyboard_frame)
            row_num += 1
