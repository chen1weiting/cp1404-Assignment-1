import csv

# Create a list to store books
booklist = []

# Define a function to load books from csv file
def load_csv_file():
    with open('books.csv') as books_csv_file:
        csv_reader = csv.reader(books_csv_file, delimiter=',')
        line_count = 0
        # Loop through each row of the csv file and add it to the booklist
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                booklist.append({
                    "title": row[0],
                    "author": row[1],
                    "pages": row[2],
                    "required": row[3]
                })
                line_count += 1
    print("{} books loaded from books.csv".format(line_count - 1))


# Define a function to print the menu
def print_menu():
    print("MENU")
    print("list - List all books")
    print("add - Add a book")
    print("mark - Mark a book as completed")
    print("quit - Save and Quit")


# Define a function to list all the books with their details
def list_books():
    print("Book List")
    # Loop through each book in the booklist
    for book in booklist:
        # If the book is required, add an asterisk next to it
        if book["required"] == "r":
            book_required = "*"
        else:
            book_required = ""
        # Print the book details
        print("{} {} - {}, {} pages{}".format(booklist.index(book) + 1, book["title"], book["author"], book["pages"],
                                              book_required))
    # If there are no required books, print the appropriate message
    if all(book["required"] != "r" for book in booklist):
        print("No required books!")


# Define a function to add a book to the booklist
def add_book():
    # Prompt for the book's title, author and pages
    book_title = input("Title: ")
    book_author = input("Author: ")
    book_pages = input("Pages: ")
    # Error check the book's title, author and pages
    if book_title == "" or book_author == "" or not book_pages.isdigit():
        print("Error: Book not added")
    else:
        # Add the book to the book list in memory
        booklist.append({
            "title": book_title,
            "author": book_author,
            "pages": book_pages,
            "required": "r"
        })
        print("{} by {}, ({} pages) added to book list".format(book_title, book_author, book_pages))


# Define a function to mark a book as completed
def mark_book_complete():
    # Prompt for the book's number
    book_number = input("Enter the number of the book to mark as completed: ")
    # Error check the book's number
    if book_number.isdigit() and int(book_number) <= len(booklist):
        # Change the book's status to completed
        booklist[int(book_number) - 1]["required"] = "c"
        print("{} by {} marked as completed".format(booklist[int(book_number) - 1]["title"],
                                                    booklist[int(book_number) - 1]["author"]))
    else:
        print("Error: Invalid book number")


# Define a function to save the books to csv file
def save_csv_file():
    with open('books.csv', mode='w') as books_csv_file:
        writer = csv.writer(books_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Title", "Author", "Pages", "Required"])
        # Loop through each book in the booklist and save it to the csv file
        for book in booklist:
            writer.writerow([book["title"], book["author"], book["pages"], book["required"]])


def main():
    print(" Welcome YOURNAME")
    # Load the books from csv file
    load_csv_file()
    # Loop until the user chooses to quit
    while True:
        # Print the menu
        print_menu()
        # Prompt for user input
        user_choice = input("Enter your choice: ")
        # If user chooses list, list all the books with their details
        if user_choice == "list":
            list_books()
        # If user chooses add, add a book to the booklist
        elif user_choice == "add":
            add_book()
        # If user chooses mark, mark a book as complete
        elif user_choice == "mark":
            mark_book_complete()
        # If user chooses quit, save the books to the csv file and quit
        elif user_choice == "quit":
            save_csv_file()
            break
        # If user input is invalid, print the appropriate message
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
