import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
RULES = "Find the greatest common divisor of given numbers."


def get_question():
    number1 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    number2 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = str(number1) + " " + str(number2)
    gcd_number = get_gcd(number1, number2)
    answer = str(gcd_number)

    return (question, answer)


def get_gcd(number1, number2):
    if number2 == 0:
        return number1
    return get_gcd(number2, number1 % number2)
