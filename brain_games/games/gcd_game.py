import random
from fractions import gcd

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100


def get_rules():
    rules = "Find the greatest common divisor of given numbers."
    return rules


def get_question():
    number1 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    number2 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = str(number1) + " " + str(number2)
    return question


def get_gcd(numbers):
    (number1, number2) = numbers.split()
    gcd_number = gcd(int(number1), int(number2))
    answer = str(gcd_number)
    return answer


def gcd_game():
    game = {"rules": get_rules, "question": get_question, "answer": get_gcd}
    return game
