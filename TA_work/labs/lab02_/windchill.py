t = float(input("Please enter the temperature(F) "))
v = float(input("Please enter the velocity(mph) "))
print(f'The wind chill is {35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)}')