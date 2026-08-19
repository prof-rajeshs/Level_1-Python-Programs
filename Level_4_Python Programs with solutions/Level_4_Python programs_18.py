#Write a program to print the sum of all TWO digit odd numbers
sum = 0
for i in range(11, 100, 2):
    sum = sum + i
print("Sum of all two digit odd numbers:", sum)