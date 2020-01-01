import random
import math


def get_rules():
    return "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def get_question():
    number = random.randint(2, 2000)
    return str(number)


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
    return {"rules": get_rules, "question": get_question, "answer": is_prime}
