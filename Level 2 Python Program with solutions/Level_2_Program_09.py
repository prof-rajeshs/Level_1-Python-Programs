#Write a loop program to print the sum of two-digit numbers whose one’s digit is 5  
sum = 0
for i in range(10, 100):
    if i % 10 == 5:
        sum = sum + i
print("Sum:", sum)