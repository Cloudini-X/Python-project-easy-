import random

def number_guessing_game():
    print("Welcome to the number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0 #To count the number of guesses
    max_attempts = 10 #You can change the limit

    while attempts < max_attempts:
        user_guess = input("Enter your guess:")

        #Check if input is a number
        if not user_guess.isdigit():
            print("Please enter valid number!")
            continue
        
        user_guess = int(user_guess)
        attempts += 1

        if user_guess == secret_number:
            print(f"That's correct! Your guessed number {secret_number} in {attempts} attempts is correct!")
            break
        elif user_guess < secret_number:
            print("Too low! Try a high number.")
        else:
            print("Too high! Try a lower number")
    else:print(f"Game over! The number was {secret_number}.")

    #Start the game
number_guessing_game()        


