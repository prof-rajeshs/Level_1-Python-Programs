#Write a program to get a number from user and if the last digit of the number is even print the same number. If the last digit of the number is odd then subtract 1 from the last digit and print the number   
i=int(input("Enter a number: "))
if (i%10)%2==0:
    print(i)    
else:
    i=i-1
    print(i)                