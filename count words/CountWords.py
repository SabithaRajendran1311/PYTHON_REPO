strings=[]
while True:
    string=input("Enter a string(or'exit'to quit):")
    if string=='exit':
        break
    strings.append(string)
word_counts=[len(string.split())for string in strings]
print("word counts:",word_counts)
  
