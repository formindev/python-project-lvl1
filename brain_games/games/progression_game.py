import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
START_RANDOM_STEP = 1
END_RANDOM_STEP = 10
PROGRESSION_LEN = 10


def get_rules():
    return "What number is missing in the progression?"


def get_question():
    start_number = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    step = random.randint(START_RANDOM_STEP, END_RANDOM_STEP)
    hidden_number = random.randint(0, PROGRESSION_LEN - 1)

    progression = ""

    for i in range(0, PROGRESSION_LEN):
        if i == hidden_number:
            progression += ".. "
        else:
            progression += str(start_number) + " "
        start_number = start_number + step

    return progression


def get_hidden_number(progression):
    numbers = progression.split()

    for index, i in enumerate(numbers):
        if i == "..":
            hidden_number = __calc_hidden_number(index, numbers)

    answer = str(hidden_number)
    return answer


def __calc_hidden_number(index, numbers):
    if index != 0 and index != len(numbers) - 1:
        step = (int(numbers[index + 1]) -
                int(numbers[index - 1])) / 2
        hidden_number = int(int(numbers[index - 1]) + step)
    else:
        step = int(numbers[2]) - int(numbers[1])
        if index == 0:
            hidden_number = int(numbers[1]) - step
        else:
            hidden_number = int(numbers[index - 1]) + step

    return hidden_number


def progression_game():
    game = {
            "rules": get_rules,
            "question": get_question,
            "answer": get_hidden_number,
            }
    return game
