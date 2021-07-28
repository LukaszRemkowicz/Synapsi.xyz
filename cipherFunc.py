import string


class Cipher:

    def __init__(self):
        """ Constructor which allows to use special character/numbers in algorithm """
        """ Can be change, depends from user needs """

        self.character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation

    def cipher_algorithm(self, string_word, key, decrypt=False, shift_type="right"):

        if key < 0:
            print("key cannot be negative")
            return None

        set_length = len(self.character_set)

        if decrypt:
            key = set_length - key

        if shift_type == "left":
            """ If left then inverse algorithm """

            key = -key

        table = str.maketrans(self.character_set, self.character_set[key:] + self.character_set[:key])

        translated_text = string_word.translate(table)

        return translated_text
