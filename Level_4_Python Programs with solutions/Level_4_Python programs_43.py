#Get a string and find the length of the string
s = input("Enter a string: ")

print("Length of the string:", len(s))

if s.isdigit():
    print("Valid number")
else:
    print("Not a valid number")