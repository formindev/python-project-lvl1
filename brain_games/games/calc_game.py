import random

operations = ['+', '-', '*']


def get_rules():
    return "What is the result of the expression?"


def get_question():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operation = operations[random.randint(0, 2)]
    return str(operand1) + operation + str(operand2)


def eval_exp(expression):
    return str(eval(expression))


def calc_game():
    return {"rules": get_rules, "question": get_question, "answer": eval_exp}
