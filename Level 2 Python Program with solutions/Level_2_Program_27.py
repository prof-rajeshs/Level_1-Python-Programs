#Write a program to print the total count of numbers which are less than 100000 and whose sum of digits is 14  
count = 0
for i in range(100000):
    if sum(int(digit) for digit in str(i)) == 14:
        count += 1      
print("Result:", count)