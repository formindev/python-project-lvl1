import random
import math

START_RANDOM_RANGE = 2
END_RANDOM_RANGE = 2000
RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def get_question():
    number = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = str(number)
    answer = __is_prime(number)

    return (question, answer)


def __is_prime(number):
    if number == 2:
        return "yes"

    if number % 2 == 0:
        return "no"

    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit):
        if number % i == 0:
            return "no"

    return "yes"
