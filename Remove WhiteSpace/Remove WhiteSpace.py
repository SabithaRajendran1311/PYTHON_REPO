strings=[]
while True:
    string=input("Enter a string(or'exit'to quit):")
    if string=='exit':
        break
    strings.append(string)
    stripped_strings=[string.replace(" ","")for string in strings]
    print("strings without whitespace:",stripped_strings) 

