#  Get a three-digit number from user and print the reverse of the number
i = int(input("Enter a three-digit number: "))
hundreds_digit = i // 100
tens_digit = (i // 10) % 10
ones_digit = i % 10
reverse = (ones_digit * 100) + (tens_digit * 10) +hundreds_digit        
print("The reverse of the number is:", reverse)