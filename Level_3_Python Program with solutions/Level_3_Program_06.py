def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse

def main():
    """Example usage of the reverse_number function"""
    number = int(input("Enter a number: "))
    result = reverse_number(number)
    print(f"The reversed number would be: {result}")

if __name__ == "__main__":
    main()