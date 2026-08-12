#Get two 3-digit numbers from user. Print the difference between the one’s digit and hundred’s digit of the number whose ten’s digit is bigger than the other number’s ten’s digit  
i=int(input("Enter the first three-digit number: " ))
j=int(input("Enter the second three-digit number: " ))
tens_digit_i = (i // 10) % 10
tens_digit_j = (j // 10) % 10
if tens_digit_i > tens_digit_j:
    number_with_bigger_tens_digit = i
else:
    number_with_bigger_tens_digit = j
hundreds_digit = number_with_bigger_tens_digit // 100
ones_digit = number_with_bigger_tens_digit % 10
difference = ones_digit - hundreds_digit
print("The difference between the one’s digit and hundred’s digit of the number whose ten’s digit is bigger is:", difference)