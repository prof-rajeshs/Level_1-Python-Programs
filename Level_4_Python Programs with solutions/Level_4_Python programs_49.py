# Write a function to convert an integer array to a character array and print it.
def convert_to_char_array(int_array):
    char_array = [str(digit) for digit in int_array]
    print("The character array is:", char_array)
# Input integer array
int_array = [1, 2, 3, 4, 5]

# Function call
convert_to_char_array(int_array)