def check_assending(no):
    # Convert the integer to a string to easily compare adjacent digits
    s = str(no)
    
    # Check if each digit is less than or equal to the next digit
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return "No"
    return "Yes"

def main():
    number1 = int(input("Enter a number: "))
    result = check_assending(number1)
    print(result)

if __name__ == "__main__":
    main()