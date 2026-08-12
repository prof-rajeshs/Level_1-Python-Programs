i=int(input("Enter the first three-digit number: " ))
j=int(input("Enter the second three-digit number: " ))
sum_of_digits_i = (i % 10) + (i // 100)
sum_of_digits_j = (j % 10) + (j // 100)
if sum_of_digits_i > sum_of_digits_j:
    bigger_sum = i
else:
    bigger_sum = j
tens_digit = (bigger_sum // 10) % 10
ones_digit = bigger_sum % 10
hundreds_digit = bigger_sum // 100
sum_of_all_digits = hundreds_digit + tens_digit + ones_digit
print("sum=",sum_of_all_digits)