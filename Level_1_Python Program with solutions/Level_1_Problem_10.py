#Get a three-digit number from user and print the ten’s digit.
i = int(input("Enter a three-digit number: "))
tens_digit = (i // 10) % 10 
print("The ten’s digit is:", tens_digit)