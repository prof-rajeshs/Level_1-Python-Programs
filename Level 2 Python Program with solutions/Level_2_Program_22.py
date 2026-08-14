#  Write a program get number from user print the total number of two-digit odd numbers in the number
num = int(input("Enter a number: "))    
count = 0
for i in range(len(str(num)) - 1):
    two_digit_number = int(str(num)[i:i+2])
    if two_digit_number % 2!= 0:
        count += 1  
print("Total number of two-digit odd numbers in the number:", count)