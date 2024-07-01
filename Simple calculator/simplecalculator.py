def add(a,b):
 return a+b
def subtract(a,b):
 return a-b
def multiply(a,b):
 return a*b
def divide(a,b):
 if b!=0:
   return a/b
 else:
     print("Error:Division by zero!")
print("simple Calculator")
print("__________")
while True:
    print("operations:")
    print("1.Adittion")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=input("enter your choice(1-5):")
    if choice=="5":
        print("calculate program has ended.")
        break
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    if choice=="1":
        result=add(num1,num2)
        print("Result:",result)
    elif choice=="2":
        result=subtract(num1,num2)
        print("Result:",result)
    elif choice=="3":
        result=multiply(num1,num2)
        print("Result:",result)
    elif choice=="4":
        result=divide(num1,num2)
        if result is not None:
            print("Result:",result)
        else:
            print("invalid choice.please enter a number between 1 and 5.")
        
        
    

