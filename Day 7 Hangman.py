"""
On Day 7, I learned how to break down complex problems into manageable 
steps using flowcharts. I worked on a project that involved picking a 
random word, checking player guesses, replacing blanks with correct 
letters, tracking the player's lives, and enhancing the user experience. 
The project focused on creating a Hangman Game, where the objective is 
to guess the hidden word while avoiding losing all lives. 
"""
import random

stages = [
    '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
    /    |
        ===
    ''',
    '''
     +---+
     O   |
    /|\\  |
         |
        ===
    ''',
    '''
     +---+
     O   |
    /|   |
         |
        ===
    ''',
    '''
     +---+
     O   |
     |   |
         |
        ===
    ''',
    '''
     +---+
         |
         |
         |
        ===
    '''
]

word_list = [
    "maple", "quantum", "flare", "orbit", "horizon",
    "nebula", "cosmic", "gravity", "eclipse", "galaxy",
    "meteor", "asteroid", "comet", "stellar", "satellite",
    "lunar", "solar", "telescope", "blackhole", "supernova"
]

lives = 6

chosen_word = random.choice(word_list)
#print(chosen_word) 

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"*************{lives}/6 LIVES LEFT*************")

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win!")

    if lives > 0:
        print(stages[lives])
