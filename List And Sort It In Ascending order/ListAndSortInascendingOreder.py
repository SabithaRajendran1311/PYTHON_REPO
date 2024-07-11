num_list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    num=int(input("Enter an interger:"))
    num_list.append(num)
    num_list.sort()
print("Sorted list(ascending order):",num_list)
