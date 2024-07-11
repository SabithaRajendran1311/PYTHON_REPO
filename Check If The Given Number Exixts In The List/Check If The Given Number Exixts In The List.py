num_list=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    num=int(input("enter an integer:"))
    num_list.append(num)
    target=int(input("enter the number to search:"))
    target=int(input("enter the number to search"))
    if target in num_list:
        print("{}exists in the list.".format(target))
    else:
        print("{}dose not exits in the list.".format(target))
