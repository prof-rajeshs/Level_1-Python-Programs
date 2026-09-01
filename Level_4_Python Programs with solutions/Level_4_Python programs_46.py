# Get a number string up to 50 digits and convert it to integer array.
num_string = input("Enter a number up to 50 digits: ")
num_array = [int(digit) for digit in num_string]
print("The integer array is:", num_array)
