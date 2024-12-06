# Qns 1 Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

# Initialize an empty list
numbers = []

# Ask user how many numbers they want to input
n = int(input("Enter the number of integers: "))

# Get user input and append to the list
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Compute the sum of the integers in the list
total_sum = sum(numbers)

# Output the result
print("The sum of the integers is:", total_sum)