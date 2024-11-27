#random joke generator
import random
def randomJokeGenerator():
    jokes = [
        "Why do programmers prefer dark mode? Because light attract bugs!",
        "Why do java Developers wear glasses? Because they can't C#!",
        "How many programmers does it take to change a light bulb? None that's a hardware problem",
        "Why did the Programmer Quit his job? He didn't get arrays (a raise)",
        "What's a Programmer's favorite hangout place? Foo Bar!"
    ]
    
    print("Welcome to the Random Joke Generator!")
    print(random.choice(jokes))
    
    another = input("Do you want to hear another Joke? (yes/no): ").strip().lower()
    if another == "yes":
        randomJokeGenerator()
        
randomJokeGenerator()    