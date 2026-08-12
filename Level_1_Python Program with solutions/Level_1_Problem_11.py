#Get a two-digit number from user and print sum the digits.
i = int(input("Enter a two-digit number: "))
sum_of_digits = (i // 10) + (i % 10)
print("Sum of digits:", sum_of_digits)