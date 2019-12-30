import random


def get_rules():
    return "Answer 'yes' if number even otherwise answer 'no'."


def get_question():
    return str(random.randint(1, 100))


def is_even(number):
    if (int(number) % 2) == 0:
        return "yes"
    return "no"


def even_game():
    return {"rules": get_rules, "question": get_question, "answer": is_even}
