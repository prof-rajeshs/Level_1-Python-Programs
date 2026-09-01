#Get a string using gets function and count all the words in it.
text = input("Enter a string: ")

# Count the words
words = text.split()
count = len(words)

# Display the result
print("Number of words:", count)