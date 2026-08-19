#Get a Three digit number from user and print the digit in “Tens”position
n=int(input("Enter a three digit no.:"))
n=(n//10)%10
print("The tens digit is:", n)  