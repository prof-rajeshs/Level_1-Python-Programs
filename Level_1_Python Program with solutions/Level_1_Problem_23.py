#  Get a two digit number from user and subtract 5 from that number if the sum of the digits of the number is odd, then print the result. Do not use “if”.
num = int(input("Enter a two-digit number: "))
tens_digit = num // 10
ones_digit = num % 10
sum_of_digits = tens_digit + ones_digit
result = num - 5 * (sum_of_digits % 2)      
print("The result is:", result)