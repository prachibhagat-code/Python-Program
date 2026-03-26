class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)
        self.books.append(book)

        print("Book added successfully")

    def display_books(self):

        if len(self.books) == 0:
            print("No books in library")
            return

        for b in self.books:

            status = "Available" if b.available else "Issued"

            print("Title:", b.title,
                  "| Author:", b.author,
                  "| Status:", status)

    def lend_book(self):

        title = input("Enter book title to lend: ")

        for b in self.books:

            if b.title == title and b.available:
                b.available = False
                print("Book issued successfully")
                return

        print("Book not available")

    def return_book(self):

        title = input("Enter book title to return: ")

        for b in self.books:

            if b.title == title:
                b.available = True
                print("Book returned successfully")
                return

        print("Book not found")


library = Library()

while True:

    print("\n------ Library Menu ------")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        library.lend_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")