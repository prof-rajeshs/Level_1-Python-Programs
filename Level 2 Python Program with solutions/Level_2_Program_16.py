#  Write a program get number from user print whether that number is prime or not
num=int(input("Enter a number: "))
if num<2:
    print(num,"is not a prime number.")
else:
    is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
if is_prime:
    print("The no.is a prime number.",num)         
else:
    print("The no.is not a prime number.",num)