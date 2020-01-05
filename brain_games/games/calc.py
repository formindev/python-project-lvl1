import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
RULES = "What is the result of the expression?"

operations = ['+', '-', '*']


def get_question():
    operand1 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    operand2 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    random_index = random.randint(0, len(operations) - 1)
    operation = operations[random_index]

    question = str(operand1) + operation + str(operand2)
    answer = str(eval(question))

    return (question, answer)
