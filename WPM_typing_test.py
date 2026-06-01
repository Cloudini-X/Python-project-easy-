import time
import random

# Multiple sentence to choose from
sentence = [
    "Python is very fun and easy to learn.",
    "Typing speed improves with practice.",
    "Always focus on accuracy first, speed comes later.",
    "The quick brown fox jumps over the lazy dog."
]

# Pick a random sentence
sample_text = random.choice(sentence)

# show the text 
print("Type the following text exactly and press Enter when done:\n")
print(sample_text, "\n")

# wait for user to start
input("press Enter to start typing...")

# start timer
start_time = time.time()

# User types the text
typed_text = input("\nStart typing here:\n")

# End timer
end_time = time.time()
elapsed_time = end_time - start_time

# Calculate wpm
words_typed = len(typed_text) / 5
minutes = elapsed_time/60
WPM = words_typed / minutes

# Calculate accuracy
correct_chars = 0 
for i in range(min(len(sample_text), len(typed_text))):
    if sample_text[i]== typed_text[i]:
        correct_chars += 1
total_chars = max(len(sample_text), len(typed_text))
accuracy = (correct_chars / total_chars) * 100

# show results
print("\n---Result---")
print(f"Time taken: {elapsed_time:.2f} seconds")
print(f"WPM (words per minute): {WPM:.2f}")
print(f"Accuracy: {accuracy:.2f}%")















