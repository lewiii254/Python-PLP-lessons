import random

def random_joke_generator():
    # Joke categories
    jokes = {
        "Programming": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why do Java developers wear glasses? Because they can't C#!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
            "Why did the programmer quit his job? He didn't get arrays (a raise).",
            "What's a programmer's favorite hangout place? Foo Bar!"
        ],
        "General": [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you call fake spaghetti? An impasta!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What did the ocean say to the shore? Nothing, it just waved."
        ],
        "Dad Jokes": [
            "I'm afraid for the calendar. Its days are numbered.",
            "What do you call a factory that makes okay products? A satisfactory.",
            "What did the janitor say when he jumped out of the closet? Supplies!",
            "I only know 25 letters of the alphabet. I don't know y.",
            "What do you call a fish wearing a bowtie? Sofishticated."
        ]
    }
    
    favorites = []  # To store user's favorite jokes
    
    def display_menu():
        print("\nWhat would you like to do?")
        print("1. Hear a joke")
        print("2. Save the current joke to favorites")
        print("3. View favorite jokes")
        print("4. Quit")

    print("Welcome to the Extended Random Joke Generator!")
    
    category = None
    current_joke = None
    
    while True:
        # Choose a category
        if not category:
            print("\nAvailable joke categories:")
            for idx, cat in enumerate(jokes.keys(), 1):
                print(f"{idx}. {cat}")
            category_choice = input("Select a category by number (or type 'quit' to exit): ").strip()
            
            if category_choice.lower() == "quit":
                print("Goodbye! Thanks for using the Random Joke Generator!")
                break
            
            try:
                category = list(jokes.keys())[int(category_choice) - 1]
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
                continue
        
        # Display a random joke
        current_joke = random.choice(jokes[category])
        print(f"\nHere's a joke from the {category} category:")
        print(f"\"{current_joke}\"")
        
        # Display menu
        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                break  # Show another joke from the same category
            elif choice == "2":
                if current_joke not in favorites:
                    favorites.append(current_joke)
                    print("Joke saved to your favorites!")
                else:
                    print("This joke is already in your favorites.")
            elif choice == "3":
                if favorites:
                    print("\nYour favorite jokes:")
                    for i, joke in enumerate(favorites, 1):
                        print(f"{i}. {joke}")
                else:
                    print("\nYou have no favorite jokes yet.")
            elif choice == "4":
                print("Goodbye! Thanks for using the Random Joke Generator!")
                return
            else:
                print("Invalid choice. Please try again.")
                
random_joke_generator()                