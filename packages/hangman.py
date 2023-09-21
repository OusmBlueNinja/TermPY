# ["hangman", "packages.hangman", ["hangman"]]
# Made By YourNameHere
import random

# List of words for the Hangman game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

def hangman(command: list):
    if len(command) != 0:
        print("Usage: hangman")
        return

    # Select a random word from the word list
    word_to_guess = random.choice(word_list)

    # Initialize game state
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord to guess: " + display_word)
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"'{guess}' is not in the word.")

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word: " + word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was: " + word_to_guess)

