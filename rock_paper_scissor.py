import random

def rock_paper_scissors():
    print("Welcome to the game rock-paper-scissors!")
    print("Rules: Rock beats scissors, scissors beats paper, paper beats rock")

    choices = ["rock","paper","scissors"]

    while True:
        user_choice = input("Enter rock, paper or scissors:").lower()

        if user_choice == "quit":
          print("Thanks for playing!")
          break   #Exit the game
        
        if user_choice not in choices:
            print("Please enter valid choice!")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose:{computer_choice}")

        if user_choice == computer_choice:
            print("Its a tie!!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or\
             (user_choice == "paper" and computer_choice == "rock") or\
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You won!!\n")
        else:
            print("You lose!\n")

#start the game
rock_paper_scissors()                
             
              