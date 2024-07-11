num_list=[]
n=int(input("enter the number of element:"))
for i in range(n):
    num=int(input("Enter an interger:"))
    num_list.append(num)
max_value=max(num_list)
min_value=min(num_list)
print("Maximun value:",max_value)
print("Minimun value:",min_value)


