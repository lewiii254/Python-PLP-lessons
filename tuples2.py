#number 2
# Prompt the user to enter the names of five favorite books
print("Enter the names of your five favorite books, one at a time:")
favorite_books = tuple(input(f"Book {i + 1}: ") for i in range(5))
# Print each book name on a separate line using a for loop
print("Your favorite books:")
for i, book in enumerate(favorite_books):
    print(f"Book {i + 1}: {book}")