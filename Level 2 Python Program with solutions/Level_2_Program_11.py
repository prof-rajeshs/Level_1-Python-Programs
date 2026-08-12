#Write a program to get a number from user print the total number of digits in that number  
num = int(input("Enter a number: "))
count = 0
while num>0:
    num=num//10
    count=count+1
print("Total no.of digits:",count)