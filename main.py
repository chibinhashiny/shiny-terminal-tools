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


while True:
    options = input("Qual programa gostaria de utilizar hoje? \n (Digite o número.) 1 - Conversor de Temperaturas \n (digite SAIR para sair)")
    options = options.replace(" ","")
    options = options.upper()
    if options == "SAIR":
        break
    elif options == "1":
        print("Qual Conversor gostaria de utilizar?")
        which_conversor = input("1 - Celsius para Fahrenheit,\n 2 - Fahrenheit para Celsius, \n 3 - Celsius para Kelvin, \n 4 - Fahrenheit para Kelvin, \n 5 - Kelvin para Celsius, \n 6 - Kelvin para Fahrenheit")
        which_conversor = which_conversor.replace(" ","")
        if which_conversor == "1":
            conversor = DegreeConversor()
            conversor.celsius_to_fahrenheit()

        if which_conversor == "2":
            conversor = DegreeConversor()
            conversor.fahrenheit_to_celsius()

        if which_conversor == "3":
            conversor = DegreeConversor()
            conversor.celsius_to_kelvin()

        if which_conversor == "4":
            conversor = DegreeConversor()
            conversor.fahrenheit_to_kelvin()

        if which_conversor == "5":
            conversor = DegreeConversor()
            conversor.kelvin_to_celsius()

        if which_conversor == "6":
            conversor = DegreeConversor()
            conversor.kelvin_to_fahrenheit()
