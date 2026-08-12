#Get a three-digit number from user and make the one’s digit as 2, then print it.
i = int(input("Enter a three-digit number: "))
result = (i // 10) * 10 + 2 
print("Result:", result)