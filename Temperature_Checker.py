Temp = float(input("Give me the temperature in Celsius: "))

if Temp < 0:
    print("It's freezing!")
elif Temp < 15:
    print("It's cold!")
elif Temp < 25:
    print("The temperature is okay.")
else:
    print("It's extremely hot!")