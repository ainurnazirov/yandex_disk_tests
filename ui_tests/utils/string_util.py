import random
import string


class StringUtil:
    @staticmethod
    def generate_random_string(length=8):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
