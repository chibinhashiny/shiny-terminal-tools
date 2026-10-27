import string
import random

class PassGen:
    def __init__(self, length):
        self.length = int(length)

    def generate_random_password(length):
        random_characters = random.choices(string.ascii_letters, k = length)
        random_characters = "".join(random_characters)
        print(f"Senha gerada: {random_characters}")


