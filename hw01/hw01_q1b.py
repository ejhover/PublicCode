#Emmet Hoversten
#hover114
#CSCI 1133 Section 050
#Homework 1
initial_price = float(input("What price would you like to convert? "))
initial_currency = input("What currency is this price in?(euro or usd) ")
if initial_currency == "euro":
	print("The converted price is", initial_price * 1.43)
elif initial_currency == "usd":
	print("The converted price is", initial_price / 1.43)
else:
	print("Unknown currency: I only work with 'euro' and 'usd' ")

