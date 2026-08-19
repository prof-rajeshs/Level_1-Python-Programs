# Get a Three digit number from the user and print the sum of all digits.
n=int(input("Enter a three digit no.:"))
sum=(n//100)+((n//10)%10)+(n%10)        
print("The sum of all digits is:", sum)