#Get a two-digit number from user. If the sum of the digits is 10 then print “Success”, otherwise print “Failure”
num = int(input("Enter a two-digit number: "))
tens= num // 10
ones= num % 10
sum_of_digits = tens + ones
result = "Success" * (sum_of_digits == 10) + "Failure" *(sum_of_digits != 10)
print(result)