from brain_games.even_game import even_game
from brain_games.scripts.brain_games import greet
from brain_games.cli import print_rules


def get_rules():
    print_rules("Answer 'yes' if number even otherwise answer 'no'.")


def main():
    greet()
    get_rules()
    even_game()


if __name__ == "__main__":
    main()
