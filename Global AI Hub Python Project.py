class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.split(',')
            print("Book Title:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            if title not in book:
                self.file.write(book)
        print("Book removed .")


lib = Library()

while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    else:
        print("Please enter 1, 2, or 3.")