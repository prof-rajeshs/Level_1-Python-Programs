#Get a four-digit number from user and only reverse the last two digits of the number, then print the number   
i = int(input("Enter a four-digit number: "))
n=i // 100    
tens_digit = (i %100)//10
ones_digit = i % 10
reverse=(n*100)+(ones_digit*10)+(tens_digit)   
print("The number with the last two digits reversed is:", reverse)