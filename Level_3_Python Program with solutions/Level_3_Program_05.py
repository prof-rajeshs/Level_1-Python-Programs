def find_number_of_zeros(number):
    count = 0

    if number == 0:
        return 1

    while number > 0:
        digit = number % 10

        if digit == 0:
            count = count + 1

        number = number // 10

    return count


# Example usage (without input or logic):
number = int(input("Enter a number: "))
result = find_number_of_zeros(number)
print(result)