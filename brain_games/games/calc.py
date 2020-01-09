import random
from operator import (add, sub, mul)

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100
RULES = "What is the result of the expression?"

operations = [('+', add), ('-', sub), ('*', mul)]


def get_question():
    operand1 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    operand2 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    operation, func = random.choice(operations)

    question = str(operand1) + operation + str(operand2)
    answer = str(func(operand1, operand2))

    return (question, answer)
