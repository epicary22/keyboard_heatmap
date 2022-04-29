from window import Window
from functions import get_txts_filenames, COLORS


def main():
    print("Please choose a file to examine (type the number of the one you want to use):")
    filenames = get_txts_filenames()
    print("./txts:")
    for pos in range(len(filenames)):
        filename = filenames[pos]
        print(f" {pos}. {filename}")
    while True:
        chosen_file_pos = input("> ")
        if chosen_file_pos.isnumeric():
            chosen_file_pos = int(chosen_file_pos)
            if chosen_file_pos > len(filenames) - 1:
                chosen_file_pos = ""
                print(f"Please enter a number in the range of: 0 to {len(filenames) - 1}.")
            else:
                break
        else:
            print(f"Please enter a number in the range of: 0 to {len(filenames) - 1}.")
    file_to_examine = filenames[chosen_file_pos]

    print("Please choose an output color (type the name of the one you want to use):")
    for name in COLORS:
        print(f" * {name}")
    while True:
        chosen_color = input("> ").upper()
        if chosen_color not in COLORS.keys():
            print("Please type the name of one of the colors above.")
        else:
            break

    color_to_use = COLORS[chosen_color]

    track_shift = input("Do you want to track shift presses? (y/n): ") == "y"

    my_window = Window(
        keyboard_layout_type="us",
        file_to_examine=file_to_examine,
        track_shift=track_shift,
        key_color_activated=color_to_use
    )


main()

# This program is a "Keyboard Heatmap" where it will take in a .txt, look at all of the characters, and then
# show you which keys were hit the most on a gradient scale (all keys will be weighted from 0.00 to 1.00, they
# will have a corresponding shade of green to go with, kinda like GitHub tiles).

# TODO make a label on the window that displays the highest ranking keys, in order. That's really all that's left!
