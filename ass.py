class Library:
    # task-1
    book_list = []
    @classmethod
    def add_book(cls, book):
        cls.book_list.append(book)
    @classmethod
    def find_book(cls, book_id):
        for book in cls.book_list:
            if book.book_id == book_id:
                return book
        return None
    @classmethod
    def display_books(cls):
        if not cls.book_list:
            print("No books available.")
        else:
            for book in cls.book_list:
                book.display_info()

class Book:
    # task-2
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        # task-3
        Library.add_book(self)
    # task-4
    def borrow(self):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' borrowed.")
        else:
            print(f"Book '{self.title}' is not available.")
    # task-5
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' returned.")
        else:
            print(f"Book '{self.title}' was not borrowed.")
    # task-6
    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")
# task-7
def system_menu():
    while True:
        print("\nsystem_menu:")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            Library.display_books()
        elif choice == "2":
            book_id = input("Enter book ID to borrow: ")
            book = Library.find_book(book_id)
            if book:
                book.borrow()
            else:
                print("Book not found.")
        elif choice == "3":
            book_id = input("Enter book ID to return: ")
            book = Library.find_book(book_id)
            if book:
                book.return_book()
            else:
                print("Book not found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
# task-3
book1 = Book("101", "The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("102", "1984", "George Orwell")
book3 = Book("103", "To Kill a Mockingbird", "Harper Lee")
system_menu()
# ------------------------------------------------------------------------------
# task-8 and 9 also done in between the code by error handling and encapsulation