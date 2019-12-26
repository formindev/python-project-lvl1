import prompt


def run():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def question(number):
    print("Question:", number)


def answer():
    result = prompt.string("Your answer: ")
    return result


def check(recived, expected, name):
    if recived != expected:
        print(recived, "is wrong answer ;(. Correct answer was", expected)
        print("Let's try again, {0}!".format(name))
    else:
        print("Correct!")


def congrat(name):
    print("Congratulations {0}!".format(name))
