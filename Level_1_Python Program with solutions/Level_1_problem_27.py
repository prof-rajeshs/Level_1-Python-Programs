#Get a three-digit number from user. If the sum of the digits is 10 then print “Success”, otherwise print “Failure”
i= int(input("Enter a three-digit number: "))
hundreds = i // 100     
tens = (i// 10) % 10
ones = i % 10
sum_of_digits = hundreds + tens + ones
result = "Success" * (sum_of_digits == 10) + "Failure" *(sum_of_digits != 10)
print(result)   