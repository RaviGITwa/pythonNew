# Rock Paper Scissors game

import random

options  = ("rock","paper","scissors")
running = True


while running:
  
    player = None
    computer = random.choice(options)
    computer = str(computer)

    while player not in options:
        player = input("please enter a choice(rock, paper, scissors): ")

        print(f"player {player}")
        print(f"computer {computer}")

        if player == computer:
          print("its a tie!")
        elif player == 'rock' and computer == 'scissors':
          print('You WIN!')
        elif player == 'paper' and computer == 'rock':
          print('You WIN!')
        elif player == 'scissors' and computer == 'paper':
          print('You WIN!')
        else:
          print("You Loose")    

        play_again = input("Play again: (Y/N)").lower()
        if not play_again  == "y":
           running = False

print("Thanks for playing")
           

