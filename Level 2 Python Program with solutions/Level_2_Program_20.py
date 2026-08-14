#Write a program print total number of single digit Prime numbers
count=0
for i in range(2,10):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        count+=1
print("Total number of single digit Prime numbers:", count)