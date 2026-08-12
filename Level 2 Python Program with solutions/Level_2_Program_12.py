# Write a program to get a number from user and print the sum of all digits.    
sum=0
i=int(input("Enter a number: "))
while i>0:
    sum=sum+(i%10)
    i=i//10 
print("Sum of digits:",sum)