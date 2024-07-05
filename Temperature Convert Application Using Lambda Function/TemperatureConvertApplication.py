celsius_to_fahrenheit=lambda celsius:(celsius*9/5)+32
fahrenheit_to_celsius=lambda fahrenheit:(fahrenheit-32)*5/9
print("option")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
choice=input("enter your choice(1/2):")
if choice=='1':
    celsius=float(input("enter temperature in celsius:"))
    print("temperatur in fahrenheit:",celsius_to_fahrenheit(celsius))
elif choice=='2':
    fahrenheit=float(input("enter temperature in fahrenheit:"))
    print("temperatur in celsius:",fahrenheit_to_celsius(fahrenheit))
else:
    print("invalid choice")
