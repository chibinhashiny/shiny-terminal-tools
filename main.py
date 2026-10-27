import temperature_conversor
import password_generator

while True:
    options = input("Qual programa gostaria de utilizar hoje? \n (Digite o número.) 1 - Conversor de Temperaturas \n 2 - Gerador de Senha \n (digite SAIR para sair)")
    options = options.replace(" ","")
    options = options.upper()
    if options == "SAIR":
        break
    elif options == "1":
        print("Qual Conversor gostaria de utilizar?")
        which_conversor = input("1 - Celsius para Fahrenheit,\n 2 - Fahrenheit para Celsius, \n 3 - Celsius para Kelvin, \n 4 - Fahrenheit para Kelvin, \n 5 - Kelvin para Celsius, \n 6 - Kelvin para Fahrenheit")
        which_conversor = which_conversor.replace(" ","")
        if which_conversor == "1":
            conversor = temperature_conversor.DegreeConversor()
            conversor.celsius_to_fahrenheit()

        if which_conversor == "2":
            conversor = temperature_conversor.DegreeConversor()
            conversor.fahrenheit_to_celsius()

        if which_conversor == "3":
            conversor = temperature_conversor.DegreeConversor()
            conversor.celsius_to_kelvin()

        if which_conversor == "4":
            conversor = temperature_conversor.DegreeConversor()
            conversor.fahrenheit_to_kelvin()

        if which_conversor == "5":
            conversor = temperature_conversor.DegreeConversor()
            conversor.kelvin_to_celsius()

        if which_conversor == "6":
            conversor = temperature_conversor.DegreeConversor()
            conversor.kelvin_to_fahrenheit()

    elif options == "2":
        password_gen = password_generator.PassGen(length=input("Digite quantos caractéres você gostaria que a senha tivesse:"))
        password_gen.generate_random_password(password_gen)