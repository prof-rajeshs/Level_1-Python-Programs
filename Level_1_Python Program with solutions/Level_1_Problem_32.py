# Get two 2-digit numbers from user. If the sum of the numbers is less than 100, then print the sum, otherwise print the differenc
i= int(input("Enter the first two-digit number: "))
j= int(input("Enter the second two-digit number: "))    
sum = i + j
if sum < 100:  
    print("Sum:", sum)
else:
    difference = i - j
    print("Difference:", difference)