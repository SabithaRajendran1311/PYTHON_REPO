add=lambda x,y:x+y
subtract=lambda x,y:x-y
multiply=lambda x,y:x*y
divide=lambda x,y:x/y
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multily")
print("4.divide")
choice=input("enter choice(1/2/3/4):")
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
if choice=='1':
    print("Result:",add(num1,num2))
elif choice=='2':
    print("Result:",subtract(num1,num2))
elif choice=='3':
    print("Result:",multiply(num1,num2))
elif choice=='4':
    print("Result:",divide(num1,num2))
else:
    print("invalid input")
