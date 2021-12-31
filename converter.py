menu = """
Welcome to the currency converter

1 - Colombian pesos
2 - Argentine pesos 
3 - Mexican pesos

Choose an option: """
option = int(input(menu))
if option == 1:
    pesos = input("¿How many Colombian pesos do you have ?: ")
    pesos = float(pesos)
    dollar_value = 4042
    dollars = pesos / dollar_value
    dollars = round(dollars, 2) # round nos sirve para redondear la cantidad de decimales
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
elif option == 2:
    pesos = input("¿How many Argentine pesos do you have ?: ")
    pesos = float(pesos)
    dollar_value = 102
    dollars = pesos / dollar_value
    dollars = round(dollars, 2) # round nos sirve para redondear la cantidad de decimales
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
elif option == 3:
    pesos = input("¿How many Mexican pesos do you have ?: ")
    pesos = float(pesos)
    dollar_value = 20
    dollars = pesos / dollar_value
    dollars = round(dollars, 2) # round nos sirve para redondear la cantidad de decimales
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
else:
    print("Enter a correct option please")
    


