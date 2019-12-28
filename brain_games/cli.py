import prompt


def run():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def print_rules(rules):
    print(rules)


def print_question(number):
    print("Question:", number)


def get_answer():
    result = prompt.string("Your answer: ")
    return result


def check(recived, expected, name):
    if recived != expected:
        print("{0} is wrong answer ;(. Correct answer was {1}".format(recived, expected))
        print("Let's try again, {0}!".format(name))
    else:
        print("Correct!")


def congrat(name):
    print("Congratulations {0}!".format(name))
