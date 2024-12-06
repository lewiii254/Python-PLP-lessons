# Function to get a set of integers from the user
def get_set(prompt):
    print(prompt)
    user_input = input("Enter integers separated by spaces: ")
    try:
        return set(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return get_set(prompt)

# Get two sets of integers from the user
set1 = get_set("Enter elements of the first set:")
set2 = get_set("Enter elements of the second set:")

# Find the intersection of the two sets
common_elements = set1.intersection(set2) #set1 & set2  # Alternatively, you can use set1.intersection(set2)

# Display the results
print("\nFirst set:", set1)
print("Second set:", set2)
print("Common elements:", common_elements)
