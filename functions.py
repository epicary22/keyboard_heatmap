import struct
import os
import keyboard_layouts

COLORS = {
    "BLACK": (0, 0, 0),
    "BLUE": (0, 0, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 231, 0)
}


def get_txts_filenames() -> list:
    txts_files = os.listdir("./txts")
    return txts_files


def add_key_count_stats(filename: str, keyboard_type: str, track_shift: bool):
    if keyboard_type == "us":
       keys = keyboard_layouts.US_KEYBOARD_LAYOUT
    else:
       keys = keyboard_layouts.US_KEYBOARD_LAYOUT

    with open(f"./txts/{filename}", "r") as file:
        lines = file.readlines()
        lines_str = "".join(lines)
    
    for char in lines_str:
        for row in keys:
            for key in row.items():
                key_data = key[1]
                key_data.update({"count": 0})

    LSHIFT = keys[3]["SHIFT"]
    RSHIFT = keys[3]["SHIFT_2"]

    for char in lines_str:
        for row in keys:
            for key in row.items():
                key_data = key[1]
                if track_shift:
                    if char == key_data["normal"]:
                        key_data.update({"count": key_data["count"] + 1})
                    elif char == key_data["shift"]:
                        key_data.update({"count": key_data["count"] + 1})
                        LSHIFT.update({"count": LSHIFT["count"] + 1})
                        RSHIFT.update({"count": RSHIFT["count"] + 1})
                else:
                    if char == key_data["normal"] or char == key_data["shift"]:
                        key_data.update({"count": key_data["count"] + 1})

    key_counts = []
    total_key_count = 0
    for char in lines_str:
        for row in keys:
            for key in row.items():
                if key[0] != "SHIFT_2" or key[0] != "CTRL_2":
                    key_data = key[1]
                    if char == key_data["normal"] or key_data["shift"]:
                        key_counts.append(key_data["count"])
                        total_key_count += key_data["count"]
    maximum_key_count = max(key_counts)

    print(total_key_count)  # SOMETHING IS MESSED UP HERE!! FIX IT!!!

    for char in lines_str:
        for row in keys:
            for key in row.items():
                if key[0] != "SHIFT_2" or key[0] != "CTRL_2":
                    key_data = key[1]
                    key_data.update({"percent": key_data["count"] / maximum_key_count})
                    key_data.update({"percent_total": key_data["count"] / total_key_count})

    return keys


def rgb_tuple_to_hex(color: tuple) -> str:
    hex_bytes = bytes.hex(struct.pack("BBB", *color))
    hex_str = "#" + str(hex_bytes)
    return hex_str


def color_between(color1: tuple, color2: tuple, percent: float) -> tuple:
    new_color = []
    for pos in range(3):
        new_color.append(round(color1[pos] + ((color2[pos] - color1[pos]) * percent)))
    new_color_tuple = tuple(new_color)
    return new_color_tuple
