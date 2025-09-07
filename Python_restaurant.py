menu = {
    'Pizza':   120,
    'Pasta':   90,
    'Burger':  65,
    'Soup':   45,
    'Coffee':  10,
    'Noodles': 80,
    'Salad': 50,
    'Vada pav':  25,
    'Samosa': 25
}

print("Welcome to python restaurant")
for item, price in menu.items():
    print(f"{item}: Rs{price}")
order_total = 0

item_1 = input("Enter the name of the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1] # 0 + 120
    print(f"Your  item {item_1} has been added to your order")
else:
    print(f"Oredered item {item_1} is not available yet!")

another_item = input("Do you want to add another item? (yes/no)").lower()
if another_item == "yes":
    item_2 = input("Enter the name of the second item =")
    if item_2 in menu:
       order_total += menu[item_2]
       print("Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")        