import random
import os

def difficult(easy_or_hard):
    if easy_or_hard == "easy":
        return 10
    elif easy_or_hard == "hard":
        return 5
    else:
        again = input("Invalid syntax. Please enter 'easy' or 'hard': ")
        return difficult(again)


chosen_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = difficult(difficulty)
print(f"You have {attempts} attempts remaining to guess the number.")

while True:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if attempts == 0:
        print(f"You've run out of guesses, you lose! The answer was {chosen_number}.")
        break
    if guess > chosen_number:
        print("Too high.")
    elif guess < chosen_number:
        print("Too low.")
    elif guess == chosen_number:
        print(f"You got it!. The answer was {chosen_number}.")
        break
    else:
        print(f"You lose the game!. The answer was {chosen_number}.")
        break
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")