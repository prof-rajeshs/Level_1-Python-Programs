# Write a program get number from user print the total number of single-digit prime numbers in the number
n=int(input("Enter a number: "))
count=0
for digit in str(n):
    if int(digit) in [2, 3, 5, 7]:
        count=count+1
print("Total no.of 1digit prime no.s:", count)