#Program to print the sum of all TWO digit Prime numbers
sum = 0

for num in range(10, 100):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        sum = sum + num

print("Sum of all two-digit prime numbers:", sum)
