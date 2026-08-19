def function(no1):
    no2 = 0
    no2 = no1 + 2
    return no1
def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)
if __name__ == "__main__":
    main()