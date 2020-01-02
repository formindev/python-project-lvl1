import random
import math

START_RANDOM_RANGE = 2
END_RANDOM_RANGE = 2000


def get_rules():
    rules = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
    return rules


def get_question():
    number = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    question = str(number)
    return question


def is_prime(number):
    if int(number) == 2:
        return "yes"

    if int(number) % 2 == 0:
        return "no"

    limit = int(math.sqrt(float(number))) + 1
    for i in range(3, limit):
        if int(number) % i == 0:
            return "no"
    return "yes"


def prime_game():
    game = {"rules": get_rules, "question": get_question, "answer": is_prime}
    return game
