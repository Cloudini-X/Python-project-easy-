import random
import string
# Get 3 random letters
def random3():
    return "".join(random.choices(string.ascii_letters, k=3))

#Encoding one word
def encode(word):
    if len(word)<3:
        return word [::-1]
    return random3() + word[1:] + word [0] + random3()

#Decoding one word
def decode(word):
    if len (word)<3:
        return word [::-1]
    w = word [3:-3]
    return w[-1] + w[:-1] 

# Ask User
choice = input("Do you want to code or decode?").lower()
message = input("Enter your message:")
words = message.split()
if choice == "code":
    result = [encode(word) for word in words]
elif choice == "decode":
    result = [decode(word) for word in words]
else:
    result = ["Invalid choice."]

print("Result:", " ".join(result))

