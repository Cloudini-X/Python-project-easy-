from cryptography.fernet import Fernet
import os

#---------------Key Handling-------------
def load_or_create_key():
    """ Load existing or create a new one if not found"""
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("New key generated and saved as key.key")
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

#load the key 
key = load_or_create_key()
fer = Fernet(key)

def add():
#Add a new account + password
 name = input("Account Name:")
 pwd = input("Password:")
 encrypted_pwd = fer.encrypt(pwd.encode()).decode()
 with open("passwords.txt", "a") as f:
     f.write(name + "|" + encrypted_pwd + "\n")
 print("Password saved securely!")

def view():
     #view all stored accounts + decrypted passwords
    if not os.path.exists("passwords.txt"):
        print("No saved passwords yet")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
             user, encrypted_pwd = data.split("|")
             decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
             print("User:", user, "| Password:", decrypted_pwd)

def delete():
# Delete a saved password by account name
  if not os.path.exists("passwords.txt"):
     print("No saved passwords yet.")
     return
  
  account_to_delete =  input("Enter the account name you want to delete:")

  lines_kept = []
  found = False

  with open("passwords.txt", "r") as f:
     for line in f.readlines():
       if line.startswith(account_to_delete + "|"):
          found = True
          continue # Skip this line(delete)
       lines_kept.append(line)

  if found:
     with open("passwords.txt", "w") as f:
        f.writelines(lines_kept)
     print(f"Deleted password for account:{account_to_delete}")
  else:
     print("Account not found.")

def delete_all():
     # Delete all saved passwords
     if os.path.exists("passwords.txt"):
        confirm = input("Are you sure you want to delete all saved passwords?(yes/no)").lower()
        if confirm == "yes":
           open("passwords.txt", "w").close()
           print("All saved passwords are deleted!")
        else:
           print("Cancelled. Your passwords are safe.")
     else:
        print("No saved passwords to delete.")

while True:
    mode = input("\nChoose an option: add/view/delete/deleteall/q(quit): ").lower()

    if mode == "q":
        print("Goodbye!")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "delete":
        delete()
    elif mode == "deleteall":
        delete_all()
    else:
        print("Invalid choice, try again.")
