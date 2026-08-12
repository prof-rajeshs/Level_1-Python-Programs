#Get two 2-digit numbers from user. Print the sum of digits of the biggest number.  
i=int(input("Enter the first two-digit number: " ))
j=int(input("Enter the second two-digit number: " ))
if i > j:
    biggest_number = i  
else:
    biggest_number = j
tens_digit = biggest_number // 10
ones_digit = biggest_number % 10    
sum=tens_digit+ones_digit
print("The sum of digits of the biggest number is:", sum)