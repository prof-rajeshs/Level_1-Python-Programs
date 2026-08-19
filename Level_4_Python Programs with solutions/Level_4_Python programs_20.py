#Write a program to print the total number of single digit Prime numbers Assume 0 & 1 are not Prime.
count = 0
for i in range(2, 10):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count = count + 1
print("Total number of single digit prime numbers:", count)