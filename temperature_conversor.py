class DegreeConversor:
    def fahrenheit_to_celsius(self):
        degree_value = float(input("Digite uma temperatura em Fahrenheit"))
        converted_fahrenheit_to_celsius = ((degree_value - 32) * 5/9)
        print("A temperatura Fahrenheit em Celsius  é:", round(converted_fahrenheit_to_celsius, 2), "°C")

    def celsius_to_fahrenheit(self):
        degree_value = float(input("Digite uma temperatura em Celsius"))
        converted_celsius_to_fahrenheit = (degree_value * 9/5 + 32)
        print("A temperatura Celsius em Fahrenheit é:", round(converted_celsius_to_fahrenheit, 2), "°F")

    def celsius_to_kelvin(self):
        degree_value = float(input("Digite uma temperatura em Celsius"))
        converted_celsius_to_kelvin = (degree_value + 273.15)
        print("A temperatura Celsius em Kelvin é:", round(converted_celsius_to_kelvin, 2), "°K")

    def fahrenheit_to_kelvin(self):
        degree_value = float(input("Digite uma temperatura em Fahrenheit"))
        converted_fahrenheit_to_kelvin = ((degree_value - 32) * 5 / 9 + 273.15)
        print("A temperatura Fahrenheit em Kelvin é:", round(converted_fahrenheit_to_kelvin, 2), "°K")

    def kelvin_to_celsius(self):
        degree_value = float(input("Digite uma temperatura em Kelvin"))
        converted_kelvin_to_celsius = (degree_value - 273.15)
        print("A temperatura Kelvin em Celsius é:", round(converted_kelvin_to_celsius, 2), "°C")

    def kelvin_to_fahrenheit(self):
        degree_value = float(input("Digite uma temperatura em Kelvin"))
        converted_kelvin_to_fahrenheit = ((degree_value - 273.15) * 9 / 5 + 32)
        print("A temperatura Kelvin em Fahrenheit é:", round(converted_kelvin_to_fahrenheit, 2), "°F")