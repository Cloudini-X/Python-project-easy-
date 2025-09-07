name = input("Type your name:")
print("Welcome", name, "to this adventure!🙂")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()
if answer == "left":
    answer = input("You came to a river, you can walk around it or swim across river. Type (walk/swim):")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator 😞 ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game!😞 ")
    else:
        print("Not a valid answer.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you wanna cross?🤔")

    if answer == "yes":
        print("You have a great courage! You won! CONGRAGULATIONS 🥳") 
    else:
        print("As you have no other choice you loose😞")           

