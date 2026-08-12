#   Write a loop program to print the two-digit even numbers, who’s sum of digits are 6.
sum=0
for i in range(10, 100,2):
    sum=(i//10)+(i%10)
    if sum==6:
        print(i)