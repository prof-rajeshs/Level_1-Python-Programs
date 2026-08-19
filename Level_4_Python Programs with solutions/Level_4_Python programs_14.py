#Write a program to print the total no.of single digit odd no.s
n=int(input("Enter a number:"))
count=0
for i in range(1,n,2):
    count=count+1
print("Total number of single digit odd numbers:", count)