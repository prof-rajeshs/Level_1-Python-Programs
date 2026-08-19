def swapNumbers(no):
    # Extract the tens digit and units digit
    tens = no // 10
    units = no % 10
    
    # Swap the digits and form the new number
    swapped = (units * 10) + tens
    return swapped

def main():
    number1 = int(input("Enter a number: "))
    result = swapNumbers(number1)
    print(result)

if __name__ == "__main__":
    main()