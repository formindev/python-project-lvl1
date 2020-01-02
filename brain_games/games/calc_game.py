import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100

operations = ['+', '-', '*']


def get_rules():
    rules = "What is the result of the expression?"
    return rules


def get_question():
    operand1 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    operand2 = random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    random_index = random.randint(0, len(operations) - 1)
    operation = operations[random_index]

    question = str(operand1) + operation + str(operand2)
    return question


def eval_expression(expression):
    answer = str(eval(expression))
    return answer


def calc_game():
    game = {
            "rules": get_rules,
            "question": get_question,
            "answer": eval_expression,
            }
    return game
