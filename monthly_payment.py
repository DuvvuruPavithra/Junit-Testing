def monthly_payment():
    year = int(input("Enter the number of years: "))
    principal_loan = float(input("Enter the principal loan: "))
    percent_interest = float(input("Enter the percent interest: "))

    number = 12 * year
    interest = percent_interest / (12 * 100)
    payment = (principal_loan * interest) / (1 - (1 + interest) ** (- number))

    print("Number is:", number)
    print("Total interest is:", interest)
    print("Monthly payment is:", payment)

monthly_payment()





