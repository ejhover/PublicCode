dollars = int(input("Enter dollars "))
cents = int(input("Enter cents "))
quarters = dollars*4 + cents//25
dimes = (cents%25)//10
nickles = ((cents%25)%10)//5
pennies = ((cents%25)%10)%5
print(quarters, "quarters")
print(dimes, "dimes")
print(nickles, "nickles")
print(pennies, "pennies")

