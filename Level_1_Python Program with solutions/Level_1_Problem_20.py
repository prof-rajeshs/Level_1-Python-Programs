# Get a three-digit number from user and make the ten’s digit as 0, then print it.  
i = int(input("Enter a three-digit number: "))
hundreds_digit = i // 100
tens_digit = (i // 10) % 10
ones_digit = i % 10
result = (hundreds_digit * 100) + (0 * 10) + ones_digit
print("Result:", result)