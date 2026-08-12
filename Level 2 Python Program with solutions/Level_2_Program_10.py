#Write a loop program to print the sum of two-digit odd numbers, whose ten’s digit is 7
sum = 0
for i in range (70,80):
    if i % 2 != 0:
        #print(i)
        sum = sum + i
print("Sum:", sum)      