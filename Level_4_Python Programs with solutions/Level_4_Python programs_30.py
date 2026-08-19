for num in range(99999999, 9999999, -1):
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Largest eight-digit prime number:", num)
        break