# DEPRECATED
# DO NOT USE

class Key:

    def __init__(self, normal_value: str, **kwargs):
        """
        :param normal_value: The normal value that the keystroke should return (i.e. "a")
        :param kwargs:
            shift:  The character's "special" shift value (such as "?" or ">"). Not required for normal letters.
            length: The length of the key (default is 1).
        """
        self.normal_value = normal_value

        if "shift" in kwargs.keys:
            self.shift_value = kwargs["shift"]
        else:
            self.shift_value = normal_value.capitalize()

        if "length" in kwargs.keys:
            self.length = kwargs["length"]
        else:
            self.length = 1
