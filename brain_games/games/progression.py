import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
START_RANDOM_STEP = 1
END_RANDOM_STEP = 10
PROGRESSION_LEN = 10
RULES = "What number is missing in the progression?"


def get_question():
    start_number = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    step = random.randint(START_RANDOM_STEP, END_RANDOM_STEP)
    hidden_number = random.randint(0, PROGRESSION_LEN - 1)

    question = ""

    for i in range(0, PROGRESSION_LEN):
        if i == hidden_number:
            answer = str(start_number)
            question += ".. "
        else:
            question += str(start_number) + " "

        start_number = start_number + step

    return (question, answer)
