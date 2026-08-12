# Get a number from user and subtract 5 from that number if the number’s ten’s position digit is odd, then print the result. Do not use “if”. 
num = int(input("Enter a number: "))
tens= (num // 10) % 10   
result = num - 5 * (tens % 2)
print(result)