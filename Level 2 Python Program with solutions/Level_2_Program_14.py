#Write a program to get a number from user and interchange the first and last digits and print the result.   
num = input("Enter a number: ")
if len(num) > 1:
    first_digit = num[0]
    last_digit = num[-1]
    middle_digits = num[1:-1]
    result = last_digit + middle_digits + first_digit   
print("Result:",result)