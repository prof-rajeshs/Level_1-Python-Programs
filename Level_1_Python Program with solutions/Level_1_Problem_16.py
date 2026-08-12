#Get a four-digit number from user and only reverse the first two digits of the number, then print the number   
i = int(input("Enter a four-digit number: "))
thousands_digit = i // 1000     
hundreds_digit = (i // 100) % 10
tens_digit = (i // 10) % 10
ones_digit = i % 10
reverse = (hundreds_digit * 1000) + (thousands_digit * 100) + (tens_digit * 10) + ones_digit
print("The number with the first two digits reversed is:", reverse)