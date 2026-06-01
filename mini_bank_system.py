# Mini bank system

# Dictionary to store accounts
accounts = {}

# Function to create account
def create_account():
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists!")
    else:
        balance = float(input("Enter initial deposit amount:"))
        accounts[name] = balance
        print(f"Account created for {name} with {balance} INR.")

# Function to deposit money
def deposit():
    name = input("Enter your account")  
    if name in accounts:
        amount = float(input("Enter amount to deposit:"))
        accounts[name] += amount 
        print(f"Deposited {amount} INR. New Balance: {accounts[name]} INR.")
    else:
        print("Account not found!")

# Function to withdraw money
def withdraw():
    name = input("Enter your account name:")
    if name in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[name]:
            accounts[name] -= amount
            print(f"Withdrawn {amount} INR. Remaining balance: {accounts[name]} INR.")
        else:
            print("Insufficent balance!")
    else:
        print("Account not found!")

# Function to check balance
def check_balance():
    name = input("Enter your account name:")
    if name in accounts:
        print(f"{name}'s balance: {accounts[name]} INR")
    else:
        print("Account not found!")

# Main loop
while True:
    print("\n---Mini Banking system---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5)")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thankyou for using the Mini Banking System!")
        break
    else:
        print("Invalid choice! Please enter a number 1-5.")

    
    
    




    


        
        