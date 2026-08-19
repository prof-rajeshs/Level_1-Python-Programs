def sum14(no):
    sum_of_digits = sum(int(digit) for digit in str(no))
    if sum_of_digits == 14:
        return 1
    else:
        return 0
def main():
    number = int(input("Enter a number: "))
    result = sum14(number)
    if result == 1:
        print("Sum of Digits is 14")
    else:
        print("Sum of Digits is not 14")
if __name__ == "__main__":
    main()