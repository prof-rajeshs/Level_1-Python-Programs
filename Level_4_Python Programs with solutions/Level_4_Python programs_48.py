#Adjust the carry in an integer array. (i.e. convert the 2 digit numberinto single digit and add the carry to the next number)
def adjust_carry(arr):
    carry = 0
    for i in range(len(arr) - 1, -1, -1):
        total = arr[i] + carry
        arr[i] = total % 10
        carry = total // 10

    # If there's still a carry left after processing all digits, we can handle it here if needed.
    if carry > 0:
        print("Carry left after adjustment:", carry)