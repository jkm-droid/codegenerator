import random


def generate_first_digit():
    number = random.randint(124, 459)

    return number


def generate_second_digit():
    number = random.randint(534, 987)

    return number


def generate_first_string(get_name, length=1):
    letter = get_name.upper()

    return ''.join(random.sample(letter, length))


def generate_second_string(get_name, length=1):
    letter = get_name.upper()

    # random.shuffle(letter)

    return ''.join(random.sample(letter, length))
