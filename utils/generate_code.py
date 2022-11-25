import random


def generate_code():
    numbers = '0123456789'
    code = ''.join(random.choice(numbers)  for x in range(length))
    return code