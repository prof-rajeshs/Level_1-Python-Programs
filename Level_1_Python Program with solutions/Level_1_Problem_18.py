#Get a two-digit number from user and make the ten’s digit 1, then print it 
i = int(input("Enter a two-digit number: "))
result = 10 + (i % 10)
print("Result:", result)