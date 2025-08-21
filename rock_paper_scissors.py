import random

computer_wins = 0
user_wins = 0
options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!\n")
print("Press Q at any time to quit.\n")

while(True):

    computer = options[random.randint(0,2)]

    play = input("\nRock, Paper, Scissors?\n")

    if play.lower() == "q":
        print("Thanks for playing!\n")
        break

    if play.lower() not in options:
        print("Not an option.\n")
        continue

    print("\nComputer picked " + computer + ".")

    if play.lower() == "rock" and computer == "scissors" or play.lower() == "paper" and computer == "rock" or play.lower() == "scissors" and computer == "paper":
        print("You win!")
        user_wins += 1
    
    elif play.lower() == computer:
        print("Draw!\n")
    
    else:
        print("You lose!")
        computer_wins += 1 

print("You won " + str(user_wins) + " times.")
print("The computer won " + str(computer_wins) + " times.")

if user_wins > computer_wins:
    print("You win " + str(user_wins) + " - " + str(computer_wins) + "!")
elif user_wins == computer_wins:
    print("Draw!")
else: 
    print("You lose " + str(computer_wins) + " - " + str(user_wins) + "!")
