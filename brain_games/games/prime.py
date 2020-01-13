import random
import math

START_RANDOM_RANGE = 2
END_RANDOM_RANGE = 2000
RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def get_question():
    number = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = str(number)

    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"

    return (question, answer)


def is_prime(number):
    if number == 2:
        return True

    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False

    return True
