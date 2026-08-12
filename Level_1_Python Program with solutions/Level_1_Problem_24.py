#Get a three-digit number from user and subtract 5 from that number if one’s digit number and 100’s digit number are same, then print the result. Do not use “if”.
n = int(input("Enter a three-digit number: "))
hundreds_digit = n // 100   
ones_digit = n % 10
result = n - 5 * (hundreds_digit == ones_digit)
print("The result is:", result)