from brain_games.calc_game import calc_game
from brain_games.scripts.brain_games import greet
from brain_games.cli import print_rules


def get_rules():
    print_rules("What is the result of the expression?")


def main():
    greet()
    get_rules()
    calc_game()


if __name__ == "__main__":
    main()
