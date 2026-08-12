#  Get a three-digit number from user. If the sum of the digits is less than 10, then print the sum, otherwise add the digits of the sum. If the sum of the digits is less than 10, then print the sum, otherwise add the digits of the sum, and print the sum
i=int(input("Enter the 3 digit no."))
hundred=i//100
tens=(i//10)%10
ones=i%10
sum=hundred+tens+ones
if sum<10:
    print(sum)
else:
    sum=(sum//10)+(sum%10)
    if sum<10:
        print(sum)
    else:
        print(sum)