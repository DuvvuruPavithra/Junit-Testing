
def sqrt_using_newton_method(number):
    epsilon = 1e-15
    t = number

    while abs(t - number/t) > epsilon*t:
        t = (number/t + t) / 2
    print(t)

if __name__ == "__main__":
    num = int(input("Enter the Non negative number to find its square root : "))
sqrt_using_newton_method(num)


