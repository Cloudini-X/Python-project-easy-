#simple calculator

# Taking inputs
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# choose operation
print("Choose operation: + - * /")
operation = input("Enter your choice:")

# perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0: # to prevent division by zero.
        result = num1/num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operation."

# show result
print("Result:", result)







