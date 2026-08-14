#Write a program to get a number from user, print whether that number is prime, and sum of digit is equal to 14
#sum=0
n=int(input("Enter the no:"))
if n<2:
    print(n,"It is not a prime number.")  
else:
    is_prime=True 
for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime:
    print("It is a prime number.",n)
else:
    print("It is not a prime number.",n)
con=str(n)
sum1=0
for i in con:
    sum1=sum1+int(i)  
print("The sum of digits is:",sum1)
