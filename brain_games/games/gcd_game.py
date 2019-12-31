import random
from fractions import gcd


def get_rules():
    return "Find the greatest common divisor of given numbers."


def get_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return str(number1) + " " + str(number2)


def get_gcd(numbers):
    (number1, number2) = numbers.split()
    gcd_numbers = gcd(int(number1), int(number2))
    return str(gcd_numbers)


def gcd_game():
    return {"rules": get_rules, "question": get_question, "answer": get_gcd}
