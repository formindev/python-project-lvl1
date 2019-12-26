from brain_games.even_game import even_game
from brain_games.scripts.brain_games import greet


def rules():
    print("Answer 'yes' if number even otherwise answer 'no'.")


def main():
    greet()
    rules()
    even_game()


if __name__ == "__main__":
    main()
