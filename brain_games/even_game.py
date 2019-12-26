from brain_games.cli import (question, answer, check, congrat)
from brain_games.cli import run
import random


def even_game():
    user_name = run()
    answer_count = 0
    while answer_count < 3:
        number = random.randint(1, 100)
        question(number)
        user_answer = answer()
        right_answer = is_even(number)
        check(user_answer, right_answer, user_name)
        if user_answer != right_answer:
            return 0
        answer_count += 1
    congrat(user_name)
    return 0


def is_even(number):
    if (number % 2) == 0:
        return "yes"
    return "no"
