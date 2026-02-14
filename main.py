# Main file to run the program

from file_handling import *
from Librarian import *
from Customer import *
from library_memory import *

load_books(bookrecord) # load books from file
load_borrowing_record(borrowed_books) # load borrowing records from file for user access
load_borrowing_log(borrowing_log) # load borrowing logs from file for librarian access
 
while True:

    while True: #input validation loop
        print("Welcome to our Library system! \n")
        user_type = int(input("Are you a... (enter option no.): \n \n 1- Customer \n 2- Librarian \n __________________ ")) #asks user if theyre a customer or librarian
        if user_type == 1 or user_type == 2:
            break
    """ to ensure the user enters either 1 (customer) or 2 (librarian), as options differ based on user type """

    if user_type == 1:
        print("\n **** Customer Mode **** \n") #lets user know theyre in customer view
        type = "Customer"
    else: 
         print("\n **** Librarian Mode **** \n") #lets user know theyre in librarian view
         type = "Librarian"

    while True: # email is a unique identifier. checking if email has been used before under a different name
        user_name = input("Enter name: ")
        user_email = input("Enter email: ")
        uniqueness = unique_email(user_email,user_name)
        if (uniqueness == False) or (not user_name) or (not user_email) or (user_name.isspace()) or (user_email.isspace()): # making sure fields contain info
            print("\nInvalid\n")
        else:
            break

    save_user_info(user_name,user_email,type) # save user in file

# --------------------------------------------------------------------------------------------------------------------
#                                                   CUSTOMER VIEW

    if user_type == 1:

        customer = Customer(user_name, user_email) #creates an object using the name and email of the user, to allow them to use the Customer methods

        customer.add_customer_to_memory(user_name,user_email) # Add customer to memory

        while True: # validation and MENU loop, if user enters anything other than options available, they are taken back to the menu of options.
            print('___________________')
            action = int(input(' \n What would you like to do (enter option no.)? \n \n 1- View available books \n 2- Borrow books \n ' \
            '3- Return books \n 4- View borrowed books \n 5- Exit \n __________________')) # sees what option the user would like, by entering the option no.

            if action == 1: # SHOW AVAILABLE BOOKS

                available_books = customer.view_available_books()
                cols = 2
                width = 80

                for i in range(0, len(available_books), cols):
                    row = available_books[i:i+cols] # take up to 2 books

                    while len(row) < cols:
                        row.append("")  # fill missing columns with empty strings so formatting doesn't break

                    print("".join(f"{str(item):<{width}}" for item in row),"\n")
                    '''This uses the built in python formatting to neatly print all the available books in 2 left alligned columns'''

            elif action == 2: # BORROW BOOK
                while True:
                    try:
                        id_2_borrow = int(input("\nEnter the ID of the book you'd like to borrow: "))
                        borrow_result = customer.borrow_book(id_2_borrow,user_email)
                        if borrow_result == True:
                            print("\nBorrowing Successful!")
                        elif borrow_result == False:
                            print("\nBook Unavailable")
                    except ValueError as ve:
                        print(f"\nInvalid input: {ve}. Please try again.")
                    
                    borrow_again = input("\nWould you like to borrow again? Enter y/n: ").lower()
                    if borrow_again != 'y':
                        break

            elif action == 3: # RETURN BOOK
                while True:
                    try:
                        id_2_return = int(input("\nEnter the ID of the book you'd like to return: "))
                        return_result = customer.return_book(id_2_return,user_email)
                        if return_result == True:
                            print("\nReturn Successful!")
                        elif return_result == False:
                            print("\nBook not found in borrowing record")
                    except ValueError as ve:
                        print(f"\nInvalid input: {ve}. Please try again.")

                    return_again = input("\nWould you like to return again? Enter y/n: ").lower()
                    if return_again != 'y':
                        break

            elif action == 4 : # VIEW BORROWED BOOKS
                books = customer.view_borrowed_books(user_email)
                if not books:
                    print('\nYou havent borrowed any books yet')
                else:
                    print(f"\n{books}")

            elif action == 5: # exits / logs out and goes back to the 'are you a customer or librarian' screen
                break     

# --------------------------------------------------------------------------------------------------------------------
#                                                       LIBRARIAN VIEW

    elif user_type == 2:
        librarian = Librarian(user_name, user_email)

        librarian.add_librarian_to_memory(user_name,user_email)

        while True: # validation and MENU loop, if user enters anything other than options available, they are taken back to the menu of options.
            print('___________________')
            action = int(input('\n What would you like to do (enter option no.)? \n \n 1- View all books \n 2- Add new books \n ' \
            '3- Change book info \n 4- View customer records \n 5- View borrowed books \n 6- View all borrowing logs \n 7- View librarians record \n 8- Exit' \
            ' \n __________________ '))  #sees what option the user would like, by entering the option no.

            if action == 1: # VIEW ALL BOOKS & THEIR INFO
                books = librarian.view_all_books()
                cols = 2
                width = 80

                for i in range(0, len(books), cols):
                    row = books[i:i+cols] # take up to 4 customers for this row

                    while len(row) < cols:
                        row.append("")

                    print("".join(f"{str(item):<{width}}" for item in row),"\n")

            elif action == 2: # ADD NEW BOOKS
                while True:
                    title = input("\nTitle: ")
                    author = input("\nAuthor: ")
                    price = float(input("\nPrice: "))
                    quantity = int(input("\nQuantity: "))
                    try:
                        librarian.add_books(title,author,price,quantity)
                    except ValueError as ve:
                        print(f"\nInvalid input: {ve}. Please try again.")

                    add_again = input("\nWould you like to return again? Enter y/n: ").lower()
                    if add_again != 'y':
                        break

            elif action == 3: # CHANGE BOOK INFO
                try: 
                    id_2_change = int(input("\nEnter book ID: "))
                    att = int(input('\nWhat would you like to change?\n\n1- Title \n2- Author \n3- Price \n4- Quantity\n__________________ '))
                    change = input("\nEnter change: ")
                    if att == 1:
                        lib_change_book_att(id_2_change,"title",change)
                    elif att == 2:
                        lib_change_book_att(id_2_change,"author",change)
                    elif att == 3 and change > 0:
                        lib_change_book_att(id_2_change,"price",float(change))
                    elif att == 4 and change > 0:
                        lib_change_book_att(id_2_change,"quantity",int(change))
                except:
                    print('Error')

            elif action == 4: # VIEW CUSTOMER RECORDS
                customers = librarian.view_customers_record()
                cols = 6
                width = 20

                for i in range(0, len(customers), cols):
                    row = customers[i:i+cols] # take up to 6 customers for this row

                    while len(row) < cols:
                        row.append("")

                    print("".join(f"{str(item):<{width}}" for item in row),"\n")

            elif action == 5: # VIEW BORROWED BOOKS FOR A CERTAIN CUSTOMER
                email = input("\nEnter user Email: ")
                books = librarian.view_borrowed_books(email)
                if not books:
                    print('\nNo borrowed books')
                else:
                    print(f"\n{books}")

            elif action == 6: # BORROWING LOGS
                cols = 1
                width = 80

                for i in range(0, len(borrowing_log), cols):
                    row = borrowing_log[i:i+cols]

                    while len(row) < cols:
                        row.append("")

                    print("".join(f"{str(item):<{width}}" for item in row),"\n")
            
            elif action == 7: # VIEW LIBRARAIANS RECORD
                librarians = librarian.view_librarians_record()
                cols = 6
                width = 20

                for i in range(0, len(librarians), cols):
                    row = librarians[i:i+cols]

                    while len(row) < cols:
                        row.append("")

                    print("".join(f"{str(item):<{width}}" for item in row),"\n")

            elif action == 8: # exits / logs out and goes back to the 'are you a customer or librarian' screen
                break 