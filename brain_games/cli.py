import prompt


def greet():
    print('Welcome to the Brain Games!')


def get_user_name():
    user_name = prompt.string("May I have your name? ")
    print("Hello,", user_name)
    return user_name


def print_rules(rules):
    print(rules)


def print_question(question):
    print("Question:", question)


def get_user_answer():
    user_answer = prompt.string("Your answer: ")
    return user_answer


def check(recived_answer, expected_answer, user_name):
    if recived_answer != expected_answer:
        print("{0} is wrong answer ;(. Correct answer was {1}"
              .format(recived_answer, expected_answer))
        print("Let's try again, {0}!".format(user_name))
    else:
        print("Correct!")


def congratulate(user_name):
    print("Congratulations {0}!".format(user_name))
