import random

def randD_digit(digit):
    min_num = pow(10, digit-1)
    max_num = pow(10, digit)-1

    return random.randint(min_num, max_num)