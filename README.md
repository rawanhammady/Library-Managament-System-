# Library-Managament-System-
Simple library management system with a terminal based UI. Allows 2 types of user: librarians and customers.

# Features
- Add and manage/edit books
- Borrow and return books
- User and librarian records
- Borrowing log with datetimestamp
- Data persistence using CSV files.
- User records, books, and borrowing logs are automatically saved to csv files and automatically loaded to program runtime memory when running
- Terminal based UI

# Customers
- View available books
- Borrow and return books
- View the books currently borrowed by them

# Librarians
- View all books with their available quantities
- View names and emails of all customers and librarians that have used the system
- View books currently borrowed by a certain user
- View borrowing/returning logs with user info and datetime of operation
- Add new books
- Edit existing book information

# Structure
- main.py : main program & UI
- Abstract.py : Blueprint for customer and librarian classes and methods
- Customer.py : customer class. Methods that can be used by cutomers
- Librarian.py : librarian class. Methods that can be used by librarians
- file_handling.py : includes all functions that interact with the csv files
- library_memory.py : contains lists/dictionaries that represent program memomry. Existing records are automatically loaded from csv files into them
- BooksRecords.csv : Record of books at the library. Contains: bookID (automatic generation upon book additon), title, author, price, and quantity
- UserRecords.csv : Record of all users that have used the system. Contains: name, email, and user type (customer/librarian)
- BorowingRecords.csv : Log of all borrowing/returning operations by cutomers. Contains: email, name, bookID, operation (borrow/return), datetimestamp

# How to Run
1. Make sure Python 3 is installed
2. Open the project in VS Code
3. Ensure all files are in the same folder
4. Run the main.py file

# Notes
This project was developed as part of a university programming assignment
and later refactored and organized for portfolio purposes.

# License
All rights reserved.  
This code is provided for viewing purposes only. Do not copy, reuse, or redistribute without explicit permission from the author.

# Author
Rawan Ali
