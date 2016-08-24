import string
import random


def generate_url_part():
    chars = 6
    part = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(chars))
    return part

if __name__ == "__main__":
    generate_url_part()
