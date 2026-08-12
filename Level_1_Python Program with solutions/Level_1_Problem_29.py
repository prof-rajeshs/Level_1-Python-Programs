# Get a four-digit number from user. If the sum of the ten’s digit and hundred’s digit is greater than 10, then print “Success”, otherwise print “Failure”
i = int(input("Enter a four-digit number: "))      #3567
hundreds= (i // 100) % 10                                                                          #5
tens= (i // 10) % 10                                                                               #6
sum_of_digits = hundreds + tens   
if sum_of_digits > 10:  
    print("Success")
else:
    print("Failure")                                                               #11