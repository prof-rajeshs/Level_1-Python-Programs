#Get a three-digit number from user and print sum the digits
i = int(input("Enter a three-digit number: "))
sum_of_digits = (i // 100) + ((i // 10) % 10) + (i % 10)
print("Sum of digits:", sum_of_digits)