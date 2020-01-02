import random

START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 100


def get_rules():
    rules = "Answer 'yes' if number even otherwise answer 'no'."
    return rules


def get_question():
    question = str(random.randint(START_RANDOM_RANGE, END_RANDOM_RANGE))
    return question


def is_even(number):
    answer = "yes" if (int(number) % 2) == 0 else "no"
    return answer


def even_game():
    game = {"rules": get_rules, "question": get_question, "answer": is_even}
    return game
