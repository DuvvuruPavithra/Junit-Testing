def temperature_conv():
    fahrenheit = int(input("Enter the Temperature value in Fahrenheit : "))
    celsius = int(input("Enter the Temperature value in Celsius : "))

    # converting celsius to fahrenheit
    celsius_to_fahrenheit = (celsius * 1.8) + 32
    print("The temperature of converting celsius to fahrenheit:", celsius_to_fahrenheit)
    fahrenheit_to_celsius = (fahrenheit - 32) / 1.8
    print("The temperature of converting celsius to fahrenheit:", fahrenheit_to_celsius)
temperature_conv()