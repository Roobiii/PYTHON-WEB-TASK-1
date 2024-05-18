import random
import logo_art

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high")
        return attempts - 1
    else:
        print(f"Your guess is right... The answer was {answer}")
        return 0

def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 to 100.")
    answer = random.randint(1, 100)
    level = input("Choose level of difficulty....Type 'easy' or 'hard': ")
    attempts = set_difficulty(level)
    if attempts!= EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("You have entered wrong difficulty level...Play again!!")
        return   
    guessed_number = 0
    while guessed_number != answer and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0 and guessed_number != answer:
            print("You are out of guesses.... You lose!")
            print(logo_art.over)
            return
        elif guessed_number != answer:
            print("Guess again")

game()
