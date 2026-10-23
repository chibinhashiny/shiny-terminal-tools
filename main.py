class DegreeConversor:
    def fahrenheit_to_celsius(self):
        degree_value = float(input("Digite uma temperatura em Fahrenheit"))
        converted_fahrenheit_to_celsius = ((degree_value - 32) * 5/9)
        print("A temperatura Fahrenheit em Celsius  é:", converted_fahrenheit_to_celsius,"°C")

    def celsius_to_fahrenheit(self):
        degree_value = float(input("Digite uma temperatura em Celsius"))
        converted_celsius_to_fahrenheit = (degree_value * 9/5 + 32)
        print("A temperatura Celsius em Fahrenheit é:", converted_celsius_to_fahrenheit,"°F")


while True:
    options = input("Qual programa gostaria de utilizar hoje? \n (Digite o número.) 1 - Conversor de Temperaturas")
    options = options.replace(" ","")
    if options == "1":
        print("Qual Conversor gostaria de utilizar?")
        which_conversor = input("1 - Celsius para Fahrenheit, 2 - Fahrenheit para Celsius, 3 - Sair")
        which_conversor = which_conversor.replace(" ","")
        if which_conversor == "1":
            conversor = DegreeConversor()
            conversor.celsius_to_fahrenheit()
        if which_conversor == "2":
            conversor = DegreeConversor()
            conversor.fahrenheit_to_celsius()
        if which_conversor == "3":
             break
