# Get a two-digit number from user and make the one’s digit as 0, then print it.    
i = int(input("Enter a two-digit number: "))    
result = (i // 10) * 10
print("Result:", result)