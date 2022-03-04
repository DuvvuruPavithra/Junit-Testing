def decimalToBinary(inp_val):
    if inp_val >= 1:
        # recursive function call
        decimalToBinary(inp_val // 2)

    # printing remainder from each function call
    print(inp_val % 2, end='')


# Driver Code
if __name__ == '__main__':
    # decimal value
    inp_val = int(input("Enter a decimal number:"))

    # Calling special function
decimalToBinary(inp_val)
