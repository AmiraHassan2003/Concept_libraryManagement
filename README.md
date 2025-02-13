# Library Management System (Functional Paradigm)

## Overview

 - The Library Management System is designed to handle books, members, and borrowings using a functional programming approach. The system includes functionalities such as adding, updating, searching, and deleting books and members, as well as managing borrowing records.

## Features

### 1. Book Management

 - Add a new book

 - Remove a book by ID

 - Search for books by title, author, or genre

 - Update book details (title, author, genre)

 - Retrieve all books

### 2. Member Management

 - Add a new member

 - View member details by ID

 - Update member name or phone number

### 3. Borrowing Management

 - Borrow a book (store borrowing details: member ID, book ID, borrow and return date)

 - View borrowing history for a specific book

 - View borrowing history for a specific member



## Project Structure

libraryManagement_FunctionalParadigm/
│── book.py            # Handles book-related functionalities
│── member.py          # Handles member-related functionalities
│── borrowings.py      # Handles borrowing transactions
│── main.py            # Entry point of the system


## How to Use

### Manage Books

 - Add a book: book.addBook("title", "author", "genre")

 - Remove a book: book.removeBook(book_id)

### Search books:

 - By Title: book.searchTitleBook("title", titles, authors, genres)

 - By Author: book.searchAuthorBook("author", titles, authors, genres)

 - By Genre: book.searchGenreBook("genre", titles, authors, genres)

### Update book details:

 - Title: book.updateTitle(id, "new_title", ids_book, authors, genres)

 - Author: book.updateAuthor(id, "new_author", ids_book, titles, genres)

 - Genre: book.updateGenre(id, "new_genre", ids_book, titles, authors)

 - View all books: book.getAllBooks(titles, authors, genres)

### Manage Members

 - Add a member: member.addMember("name", "phone")

 - View a member: member.viewMember(id, names, phones)

### Update member details:

 - Name: member.updateName(id, "new_name", ids_member, phones)

 - Phone: member.updatePhone(id, "new_phone", ids_member, names)

### Manage Borrowings

 - Borrow a book: borrow.borrowBook(member_id, book_id, "borrow_date", "return_date", booksList, memberBorrowingList)

### View borrowing history:

 - By Book ID: borrow.historyBook(book_id)

 - By Member ID: borrow.historyMember(member_id)


