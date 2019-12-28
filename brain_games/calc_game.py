from brain_games.cli import (print_question, get_answer, check, congrat)
from brain_games.cli import run
import random

operations = ['+', '-', '*']

def calc_game():
    user_name = run()
    answer_count = 0
    while answer_count < 3:
        operand1 = random.randint(1, 100)
        operand2 = random.randint(1, 100)
        operation = operations[random.randint(0, 2)]
        number = str(operand1) + operation + str(operand2)
        print_question(number)
        user_answer = get_answer()
        right_answer = str(eval(number))
        check(user_answer, right_answer, user_name)
        if user_answer != right_answer:
            return 0
        answer_count += 1
    congrat(user_name)
    return 0

