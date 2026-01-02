temperature= float(input("Enter the temperature in Celsius: "))
if temperature > 40.5:    
    print("temperature is {}!! Go to hospital.".format(temperature))

elif temperature > 39.4:
    print("call your doctor.")
else:
    print("consider retsting at home or medication.")


print("Stay safe!")