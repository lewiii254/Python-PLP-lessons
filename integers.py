# Program to create a list of integers and compute their sum

# Step 1: Accept a list of integers from the user
def get_user_input():
    print("Enter integers separated by spaces:")
    user_input = input()
    try:
        # Convert input into a list of integers
        numbers = list(map(int, user_input.split()))
        return numbers
    except ValueError:
        print("Invalid input! Please enter only integers.")
        return get_user_input()

# Step 2: Calculate the sum of the integers in the list
def calculate_sum(numbers):
    return sum(numbers)

# Step 3: Main function
def main():
    numbers = get_user_input()
    total = calculate_sum(numbers)
    print(f"The sum of the integers in the list is: {total}")

# Run the program
if __name__ == "__main__":
    main()
