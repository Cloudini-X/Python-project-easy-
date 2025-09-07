print("Hey! Welcome to the name vibe of TMKOC!!!")

while True:
    name = input("Enter your name:")

    if not name.isalpha():
        print("please enter valid name(letters only)")
        break
    
    first_letter = name[0].lower()

    if first_letter in  "qwert":
        print(f"Your name {name} shows character of Jethala Gada!")
        break
    elif first_letter in  "yuiop":
        print(f"Your name {name} shows character of Hathi bahi!")
        break
    elif first_letter in  "hsdfg":
        print(f"Your name {name} shows character of Aatmaram Tukaram Bhide!")
        break 
    elif first_letter in  "ajkl":
        print(f"Your name {name} shows character of Babitaji!")
        break
    elif first_letter in  "zxcv":
        print(f"Your name {name} shows character of Daya!")
        break
    else:
        first_letter in "bnm"
        print(f"Your name {name} shows character of Champak chacha!")
        break

