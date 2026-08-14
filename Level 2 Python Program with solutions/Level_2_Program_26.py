#Write a program to print biggest 4-digit number which is divisible by 7 and 9.``
for i in range(9999, 999, -1):
    if i % 7 == 0 and i % 9 == 0:
        print("Biggest 4-digit number divisible by 7 and 9 is:", i)
        break   