import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
RULES = "Answer 'yes' if number even otherwise answer 'no'."


def get_question():
    number = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = str(number)
    answer = "yes" if number % 2 == 0 else "no"

    return (question, answer)
