library={}
def add_book(title,author,year):
    book={'Title':title,'Author':author,'Year':year}
    library[title]=book
    print(f'{title}added to library.')
def remove_book(title):
    if title in library:
        del library[title]
        print(f'{title}removed from library.')
    else:
        print('f{title}not found in library.')
def print_library():
    for title,book in library.items():
        print(f'Title:{book["Title"]},Author:{book["Author"]},Year:{book["Year"]}')
def main():
    while True:
        print("1.add book")
        print("2.remove book")
        print("3.print library")
        print("4.exit")
        choice=input("enter your choice:")
        if choice=='1':
            title=input("enter the title:")
            author=input("enter the author:")
            year=input("enter the year:")
            add_book(title,author,year)
        elif choice=='2':
            title=input("enter the title of the book to remove:")
            remove_book(title)
        elif choice=='3':
            print("library contents:")
            print_library()
        elif choice=='4':
            print("exiting the libary program.")
            break
        else:
            print("invalid choice.please select aa valid option.")
if __name__=="__main__":
    main()

