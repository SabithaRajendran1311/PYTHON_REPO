list_items=[]
while True:
    item=input("Enter an item for the list(or'done' to finish):")
    if item=='done':
        break
    list_items.append(item)
    string_item=input("Enter a string item:")
    tuple_items=tuple(list_items)+(string_item,)
    print(tuple_items)
