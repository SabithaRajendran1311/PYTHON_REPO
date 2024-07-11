strings=[]
while True:
    string=input("Enter  a string(or'exit'to quit):")
    if string=='exit':
        break
    strings.append(string)
result=''.join(strings)
print("Concatenated string:",result)
