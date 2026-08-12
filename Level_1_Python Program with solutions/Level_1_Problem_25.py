#Get a four-digit number from user and subtract 5 from that number if ten’s digit position and 100’s digit position is same, then print the result. Do not use “if”. 
n = int(input("Enter a four-digit number: "))   
hundreds_digit = (n // 100) % 10
tens_digit = (n // 10) % 10
result = n - 5 * (hundreds_digit == tens_digit)
print("The result is:", result)