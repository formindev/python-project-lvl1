from brain_games.cli import (
                            greet, print_rules, get_user_name,
                            print_question, get_user_answer,
                            congratulate, check,
                            )


ROUNDS_COUNT = 3


def play(game):
    greet()

    print_rules(game.RULES)

    user_name = get_user_name()

    answer_count = 0
    while answer_count < ROUNDS_COUNT:
        question, answer = game.get_question()
        print_question(question)
        user_answer = get_user_answer()
        check(user_answer, answer, user_name)
        if user_answer != answer:
            return
        answer_count += 1
    congratulate(user_name)
