import string
import random

class PassGen:
    def __init__(self, length):
        self.length = int(length)

    def generate_random_password(length):
        random_characters = random.choices(string.ascii_letters, k = length)
        random_characters = "".join(random_characters)
        print(f"Senha gerada: {random_characters}")


    def generate_random_password_with_numbers(length):
        random_characters_and_numbers = string.ascii_letters + string.digits
        random_digits_pass = random.choices(random_characters_and_numbers, k=length)
        random_digits_pass = "".join(random_digits_pass)
        print(f"Senha gerada: {random_digits_pass}")


