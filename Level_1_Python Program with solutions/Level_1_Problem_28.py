# Get a three-digit number from user. If the sum of the one’s digit and hundred’s digit is less than 10, then print “Success”, otherwise print “Failure”
i = int(input("Enter a three-digit number: "))      #356
hundreds_digit = i // 100                            #3
ones_digit = i % 10                                  #6
sum_of_digits = hundreds_digit + ones_digit          #9
result = "Success" * (sum_of_digits < 10) + "Failure" *(sum_of_digits >= 10)
print(result)