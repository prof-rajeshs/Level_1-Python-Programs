for num in range(9999, 999, -1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Largest four digit prime number:", num)
        break