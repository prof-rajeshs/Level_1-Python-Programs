# Write a program get number from user print the total number digits which are odd in the number
num = int(input("Enter a number: "))
count = 0
for digit in str(num):
    if int(digit) % 2 != 0:
        count += 1
print("Total number of odd digits in the number:", count)