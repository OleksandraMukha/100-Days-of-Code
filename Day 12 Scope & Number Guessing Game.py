import random
LEVEL_EASY = 10
LEVEL_HARD = 5
attempts = 0

def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if level == "easy":
        return LEVEL_EASY
    else: 
        return LEVEL_HARD

def check_answer(user_guess, actual_answer, attempts):
    if user_guess > actual_answer:
        print("Too high")
        attempts -= 1
    elif user_guess < actual_answer:
        print("Too low")
        attempts -= 1
    else:
        print("You got it!")
    return attempts

def game():
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)

    attempts = difficulty_level()

    guess = 0
    while guess != random_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, random_number, attempts)
        if attempts == 0:
            print(f"You've run out of guesses, you lose. Coorect answer {random_number}.")
            return
game()