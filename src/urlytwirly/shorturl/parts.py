import string
import random


def generate_url_part():
    chars = 6
    characters = 'ACDEFGHKMNPQRSTUVWXYZ2345679'
    part = ''.join(random.choice(characters) for _ in range(chars))
    return part

if __name__ == "__main__":
    generate_url_part()
