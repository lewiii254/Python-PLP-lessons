# Simple Quiz Game
def quiz_game():
    print("Welcome to the Python Quiz Game!")
    
    questions = [
        {
            "question": "What is the output of print(2**3)?",
            "options": ["6", "8", "9", "Error"],
            "answer": "8"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["def", "fun", "define", "function"],
            "answer": "def"
        },
        {
            "question": "What does 'len()' function do in Python?",
            "options": [
                "Calculates length of an object", 
                "Finds the type of an object", 
                "Returns an error", 
                "None of the above"
            ],
            "answer": "Calculates length of an object"
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")
        
        answer = input("Enter the number of your answer: ").strip()
        correct_option = q['options'].index(q['answer']) + 1
        
        if answer == str(correct_option):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
    
    print(f"\nYour final score is {score}/{len(questions)}!")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz_game()

# Uncomment the line below to run the function
quiz_game()