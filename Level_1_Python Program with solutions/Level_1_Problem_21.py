# Get a number from user and subtract 5 from that number if the number is odd, then print the result. Do not use “if”.
num = int(input("Enter a number: "))
result = num - (num % 2) * 5
print("The result is:", result)