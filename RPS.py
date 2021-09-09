#rock paper scissors
import random

def comp_choice(options):
    val = random.randint(0,2)
    return options[val]

options=["rock", "paper", "scissors"]

score = 0
c_score = 0
print("Welcome to Rock Paper Scissors!")
print("Score: You - %d vs Computer - %d" %(score,c_score))

while True:
    print("Lets begin!")
    choice = input("Rock, Paper or Scissors? ").lower()
    c_choice = comp_choice(options)

    print("You picked: %s" %choice)
    print("The computer picked: %s" %c_choice)

    if (choice == "rock" and c_choice == "scissors"):
        print("point you!")
        score = score + 1
    elif (choice == "paper" and c_choice == "rock"):
        print("point you!")
        score = score + 1
    elif (choice == "scissors" and c_choice == "paper"):
        print("point you!")
        score = score + 1
    elif (c_choice == "paper" and choice == "rock"):
        print("point computer!")
        c_score = c_score + 1
    elif (c_choice == "scissors" and choice == "paper"):
        print("point computer!")
        c_score = c_score + 1
    elif (c_choice == "rock" and choice == "scissors"):
        print("point computer!")
        c_score = c_score + 1
    elif(choice == c_choice):
        print("Tie! no points")

    print("Score: You - %d vs Computer - %d" %(score,c_score))
    cont = input("Again? (y/n) ").lower()
    if cont == "n":
        break


print("Final score is: You - %d vs Computer - %d" %(score,c_score))
print("Goodbye!")