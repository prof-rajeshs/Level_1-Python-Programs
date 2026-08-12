#Get a four-digit number from user. If the sum of the ten’s digit and hundred’s digit is equal to 10, and one of the digits is more than 7 then print “Success”, otherwise print “Failure”. 
i = int(input("Enter a four-digit number: "))  
thousands= i // 1000     
hundreds= (i // 100) % 10
tens= (i // 10) % 10
sum_of_digits = hundreds + tens
ones = i % 10
if sum_of_digits == 10 and (hundreds > 7 or tens > 7):
    print("Success")
else:
    print("Failure")