# Get a two-digit number from user and print the reverse of the number.
i = int(input("Enter a two-digit number: "))
tens_digit = i // 10        
ones_digit = i % 10
reverse= (ones_digit * 10) + tens_digit
print("The reverse of the number is:", reverse)
