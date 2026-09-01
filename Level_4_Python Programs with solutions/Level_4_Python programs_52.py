#Get a main string and sub string. Check the sub string in main string an print the position
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring: ")
position = main_string.find(sub_string)
if position != -1:
    print("The substring is found at position:", position)
else:
    print("The substring is not found in the main string.")