import random


def get_rules():
    return "What number is missing in the progression?"


def get_question():
    start_number = random.randint(1, 100)
    step = random.randint(1, 10)
    hidden_number = random.randint(0, 9)
    progression = ""
    for i in range(0, 10):
        if i == hidden_number:
            progression += ".. "
        else:
            progression += str(start_number) + " "
        start_number = start_number + step
    return progression


def get_number(numbers):
    progression = numbers.split()
    for index, i in enumerate(progression):
        if i == "..":
            if index != 0 and index != len(progression) - 1:
                step = (int(progression[index + 1]) -
                        int(progression[index - 1])) / 2
                number = int(int(progression[index - 1]) + step)
            else:
                step = int(progression[2]) - int(progression[1])
                if index == 0:
                    number = int(progression[1]) - step
                else:
                    number = int(progression[index - 1]) + step
    return str(number)


def progression_game():
    return {"rules": get_rules, "question": get_question, "answer": get_number}
