#:Add two integer arrays of up to 50 digits and store the result in a 51 digits array
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

array1 = list(map(int, num1))
array2 = list(map(int, num2))

# Create a 51-digit result array
result = [0] * 51

i = len(array1) - 1
j = len(array2) - 1
k = 50
carry = 0

while i >= 0 or j >= 0 or carry > 0:

    digit1 = array1[i] if i >= 0 else 0
    digit2 = array2[j] if j >= 0 else 0

    total = digit1 + digit2 + carry

    result[k] = total % 10
    carry = total // 10

    i -= 1
    j -= 1
    k -= 1

# Print the result without leading zeros
start = 0
while start < 50 and result[start] == 0:
    start += 1

print("Sum:", ''.join(map(str, result[start:])))