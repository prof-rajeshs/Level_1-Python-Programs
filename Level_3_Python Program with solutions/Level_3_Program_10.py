def count_Digits(no):
    # Convert the number to a string and return its length
    result = len(str(no))
    return result

def main():
    number1 = int(input("Enter a number: "))
    result = count_Digits(number1)
    print(result)

if __name__ == "__main__":
    main()