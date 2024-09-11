# Anagram Game
import random

words = ('sachin','sehwag','dravid','laxman',
         'ganguly','yuvraj','kaif','dhoni','rohit','virat')

word = random.choice(words)
jumble = " ".join(random.sample(word,len(word)))

chances = 3

print("~"*30)
print("~~~  Cricketers Jumble Game  ~~~")
print("~"*30)

while chances!=0:
    print(f"Jumbled word {jumble}")
    guess = input("Enter your guess ").lower()
    if guess == word:
        print("Correct, You Won!")
        break
    else:
        chances -= 1
        print(f"Incorrect Guess, you have {chances} chance pending")
        continue
else:
    print("You Loose")
    print("Thank you for playing")


     
