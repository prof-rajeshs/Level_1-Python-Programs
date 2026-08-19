def function(no1):
    no2 = int(input("Enter second number: "))   # Define and initialize no2

    # Your Program Here
    if no1 == no2:
        no2 = "Same"
    else:
        no2 = "Not Same"

    return no2


def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)


if __name__ == "__main__":
    main()