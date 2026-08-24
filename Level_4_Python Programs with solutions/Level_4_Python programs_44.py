num = input("Enter a number: ")

result = num.lstrip('0')

if result == "":
    result = "0"

print("After removing leading zeros:", result)