def vending_machine(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    print("currency amount")

    for i in notes:
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, "=", j)


if __name__ == "__main__":
    amount_value = int(input("Enter the amount : "))
    vending_machine(amount_value)