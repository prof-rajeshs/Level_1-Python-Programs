#Write a program get number from user print the total number of two-digit perfect square numbers in the number 
num = int(input("Enter a number: "))  
count = 0
for i in range(1, 10):
    if i * i in [int(str(num)[j:j+2]) for j in range(len(str(num)) - 1)]:
        count = count+1
print("Total no.of 2-digit perfect square no.s in the no.:", count)