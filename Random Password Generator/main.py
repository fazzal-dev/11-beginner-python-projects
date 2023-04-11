import string
import random


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = int(input("Enter the lenght of your password: "))
    password = "".join(random.choice(characters)
                       for _ in range(password_length))
    return password


print(generate_password())
