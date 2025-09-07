def KBD_game():
    questions = [
        {"question": "Which animal is known as the 'Ship of the Desert'?",
         "options": ["A. Horse", "B. Camel", "C. Cow", "D. Elephant"],
         "answer": "B"},
        {"question": "What is the smallest country in the world by area?",
         "options": ["A. Monaco", "B. Vatican City", "C. Nauru", "D. San Marino"],
         "answer": "B"},
        {"question": "Which metal is liquid at room temperature?",
         "options": ["A. Mercury", "B. Gold", "C. Silver", "D. Iron"],
         "answer": "A"},
        {"question": "Who invented the World Wide Web?",
         "options": ["A. Steve Jobs", "B. Tim Berners-Lee", "C. Bill Gates", "D. Mark Zuckerberg"],
         "answer": "B"}
    ]

    prize_money = [1000, 25000, 50000, 100000]
    total_won = 0

    print("Welcome to Kaun Banega Dhanpati!")
    print("Answer the questions correctly to win money!\n")

    for i in range(len(questions)):
        q = questions[i]
        print(f"Q{i+1}. {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print(f"Correct! You won ₹{prize_money[i]}\n")
            total_won = prize_money[i]
        else:
            print("Wrong answer. Game over!")
            break  # ✅ break is correctly inside the for loop

    print(f"\nYou won a total of ₹{total_won}!\nThanks for playing!")

# Call the game function
KBD_game()
