#Write a loop program to print the two-digit odd numbers, who’s sum of digits are 7 
sum=0
for i in range(9, 100,2): 
    sum=(i//10)+(i%10)
    if sum==7:
        print(i)