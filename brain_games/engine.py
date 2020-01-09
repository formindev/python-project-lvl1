from brain_games.cli import (greet, print_text, get_user_name,
                             print_question, get_user_answer,
                             congratulate, print_fail_answer)


ROUNDS_COUNT = 3
RIGHT_ANSWER_TEXT = "Correct!"


def play(game):
    greet()

    print_text(game.RULES)

    user_name = get_user_name()

    answer_count = 0
    while answer_count < ROUNDS_COUNT:
        question, answer = game.get_question()
        print_question(question)
        user_answer = get_user_answer()
        if user_answer != answer:
            print_fail_answer(user_answer, answer, user_name)
            return
        print_text(RIGHT_ANSWER_TEXT)
        answer_count += 1
    congratulate(user_name)
