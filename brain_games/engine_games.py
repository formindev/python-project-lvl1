from brain_games.cli import (
                            greet, print_rules, get_user_name,
                            print_question, get_user_answer,
                            congratulate, check,
                            )


ROUNDS_COUNT = 3


def play_game(game):
    greet()

    get_rules = game["rules"]
    print_rules(get_rules())

    user_name = get_user_name()
    answer_count = 0
    while answer_count < ROUNDS_COUNT:
        get_question = game["question"]
        question = get_question()
        print_question(question)
        user_answer = get_user_answer().lower()
        get_right_answer = game["answer"]
        right_answer = get_right_answer(question)
        check(user_answer, right_answer, user_name)
        if user_answer != right_answer:
            return 0
        answer_count += 1
    congratulate(user_name)
    return 0
