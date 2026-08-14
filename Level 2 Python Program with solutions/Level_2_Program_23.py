#Write a program get number from user print the total number of single-digit perfect square numbers in the number
num = int(input("Enter a number: "))
count = 0    
for digit in str(num):
    if int(digit) in [0, 1, 4, 9]:
        count += 1  
        print("Total no.of 1digit perfect square no.s:", count)  
