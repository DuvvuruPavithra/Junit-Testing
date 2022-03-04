# Taking binary input
binary = input("Enter a binary number:")

# Calling the function
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        # int() function to convert binary numbers into decimals.
        # int() function converts the binary string in base 2 number.
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)
binary_to_decimal(binary)



