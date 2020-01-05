import random
from fractions import gcd

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
RULES = "Find the greatest common divisor of given numbers."


def get_question():
    number1 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    number2 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = str(number1) + " " + str(number2)
    gcd_number = gcd(number1, number2)
    answer = str(gcd_number)

    return (question, answer)
