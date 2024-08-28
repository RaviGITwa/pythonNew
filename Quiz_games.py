# Python Quiz games

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "Which is most abundant gas in the atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the Solar system is the hotest?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. carbon-dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0 
question_number = 0


for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_number]:
     print(option)
    guess = input('Enter (A  B  C  D): ').upper()  
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")

    else :
        print("INCORRECT")
        print(f'Your Correct answer is {answers[question_number]}') 
  
    question_number += 1 
    print(f'Your total score is : {score}')
    
     



