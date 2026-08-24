#Print the total number of all Palindrome numbers less than 100000
count = 0

for i in range(100000):
    if str(i) == str(i)[::-1]:
        count += 1

print("Total number of palindrome numbers less than 100000:", count)
