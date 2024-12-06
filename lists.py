# List of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Use list comprehension to find words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the original list and the filtered list
print("Original list of words:", words)
print("Words with an odd number of characters:", odd_length_words)

mybooks = ("The Holy Bible", "The Art of War", "The 48 Laws of Power", "The 48 Laws of Human Nature", "The Wages of Sin") 
for book in mybooks: print("I like reading {}".format(book))

