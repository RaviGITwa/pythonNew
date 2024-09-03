# Number Guessing game
import random

lowest_number =1
highest_number =100
answer = random.randint(lowest_number,highest_number)
guesses= 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_number} and {highest_number}")


while is_running:

    guess = input("Please enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("Number is out of range")
            print(f"Select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low, Try again")
        elif guess > answer:
            print("Too High, Try again")
        else:
            print(f"Your Answer is correct {answer}")
            print(f"Number of guesses you took {guesses}")
            is_running = False
else:
    print("Invalid Input")
