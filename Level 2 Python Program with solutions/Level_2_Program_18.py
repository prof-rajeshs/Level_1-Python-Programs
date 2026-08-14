# Write a program to get number from user, print whether that number’s first two digits (ten’s digits and one’s digit) is prime
num=int(input("Enter the no."))
if num<2:
    print("It is not prime",num)
else:
    fl_digits=(num%100)
    is_prime=True
for i in range(2,fl_digits):
    if fl_digits%i==0:
        is_prime=False
        break
if is_prime:
    print("It is a prime",num)
else:
    print("It is not a prime",num)