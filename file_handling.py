# this file includes all the functions that interact with files

from library_memory import *

def strip_lines(filename):
    '''Strips lines of the backslash n'''
    try:
        if not isinstance(filename,str):
            raise TypeError
        stripped_lines = []
        with open(filename,'r') as file:
            for line in file:
                stripped_lines.append(line.strip())
    except FileNotFoundError:
        raise
    except TypeError:
        raise
    else:
        return stripped_lines
    
# --------------------------------------------------------------------------------------------- #
# Checking information from files

def unique_email(current_email,current_name,filename='UserRecords.csv'):
    '''Checks if email entered belongs to another name'''
    with open(filename, 'r') as file:
        file.seek(21)
        
        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            email = parts[1]

            if current_email == email and current_name != name:
                return False

# --------------------------------------------------------------------------------------------- #
# Loading information into memeroy from files

def load_books(bookrecord):
    '''Loads books saved in BooksRecords file into books_records list for easier access'''
    with open('BooksRecords.csv','r') as file:
        file.seek(35)

        for line in file:
            if not line:
                return 0
            seperate_data = line.strip().split(",")
            id = int(seperate_data[0])
            title = seperate_data[1]
            author = seperate_data[2]
            price = float(seperate_data[3])
            quantity = int(seperate_data[4])

            book = [id, title, author, price, quantity]
            bookrecord.append(book)

def load_borrowing_record(borrowing_record,filename="BorrowingRecords.csv"):
    '''Loads borrowing history into borrowed_books dictionary for user access'''
    with open(filename, 'r') as file:
        file.seek(49)

        for line in file:
            parts = line.strip().split(",")
            email = parts[0]
            id = int(parts[2])
            status = parts[3].lower()

            for book in bookrecord:
                if book[0] == id:
                    title = book[1]

            if email not in borrowed_books:
                borrowed_books[email] = []

            if status == "borrow":
                borrowed_books[email].append([id, title])
            elif status == "return":
                if email in borrowed_books:
                    # remove the returned book from the user's list
                    for b in borrowed_books[email]:
                        if b[0] == id:
                            borrowed_books[email].remove(b)

                    #  remove user if no books left
                    if not borrowed_books[email]:
                        del borrowed_books[email]

def load_borrowing_log(ls,filename='BorrowingRecords.csv'):
    '''Loads borrowing log into memory for librarian access'''
    with open(filename,'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            email = parts[0]
            name = parts[1]
            bookid = parts[2]
            b_or_r =parts[3]
            dt = parts[4]

            ls.append([email,name,bookid,b_or_r,dt])

def load_user_info(user_records,type,filename='UserRecords.csv'):
    '''Loads user information into memory from file'''

    users = []

    with open(filename,'r') as file:
        file.seek(21)

        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            email = parts[1]
            type1 = parts[2]

            user = [name,email]

            if type1.lower() == type:
                users.append(user)

        return users

# --------------------------------------------------------------------------------------------- #
# Saving information in files

def save_new_book(new_id,title,author,price,quantity,filename='BooksRecords.csv'):
        '''Saves new books to files when added by librarians'''

        with open(filename,'r+') as file:
            file.seek(0)
            first_line = file.readline()
            if not first_line:
                file.write("BookID,Title,Author,Price,Quantity\n")
    
        with open(filename, "a") as file:
            record = f"{new_id},{title},{author},{price},{quantity}"
            file.write(record + "\n")

def save_user_info(name,email,type:str,filename="UserRecords.csv"):
    '''Saves user info into the UserRecords file'''
    with open(filename,'a+') as file:
        file.seek(0)
        first_line = file.readline()
        if not first_line:
            file.write("Name,Email,User-Type\n")

    with open(filename,'a+') as file:
        emails = []
        lines = strip_lines("UserRecords.csv")
        for line in lines[1:]:
            emails.append(line.split(",")[1])

        if email not in emails:
            user_str = f"{name},{email},{type}"
            file.write(user_str + "\n")

def save_borrowing_record(name, email, id, bor_or_ret, timestamp,filename="BorrowingRecords.csv"):
    '''Records history of borrowing and returns in BorrowingRecords file'''
    with open(filename,'a+') as file:
        file.seek(0)
        first_line = file.readline()
        if not first_line:
            file.write("Email,Name,BookID,Borrow_or_Return,DateTimeStamp\n")
    
    with open(filename, "a") as file:
        record = f"{email},{name},{id},{bor_or_ret},{timestamp}"
        file.write(record + "\n")

# --------------------------------------------------------------------------------------------- #
# Editing information in files    

def change_quantity(bookID, b_or_r):
    '''Changes quantity of books based on whether it is borrowed or returned'''
    with open('BooksRecords.csv','r+') as file:
        filtered_lines = strip_lines("BooksRecords.csv")
        for i, row in enumerate(filtered_lines):
            parts = row.split(",")
            if parts[0] == str(bookID):
                if b_or_r == "borrow":
                    parts[4] = str(int(parts[4]) - 1)
                elif b_or_r == "return":
                    parts[4] = str(int(parts[4]) + 1)
                row = ",".join(parts)
                filtered_lines[i] = row
                break

    with open("BooksRecords.csv", "w") as file:
        for line in filtered_lines:
            file.write(line + "\n")  

def lib_change_book_att(bookid,attribute_2_change,new_attribute,filename='BooksRecords.csv'):
    '''Changes book info in files when changed by librarian'''
    lines = []
    with open(filename,'r') as file:
        next(file)

        for line in file:
            parts = line.strip().split(",")
            id = int(parts[0])
            title = parts[1]
            author = parts[2]
            price = parts[3]
            qnt = parts[4]

            c_line = [str(id),title,author,price,qnt]

            if bookid == id:
                if attribute_2_change == "title":
                    c_line = [str(id),new_attribute,author,price,qnt]
                elif attribute_2_change == "author":
                    c_line = [str(id),title,new_attribute,price,qnt]
                elif attribute_2_change == "price":
                    c_line = [str(id),title,author,new_attribute,qnt]
                elif attribute_2_change == "quantity":
                    c_line = [str(id),title,author,price,new_attribute]
            lines.append(c_line)

    with open(filename,'w') as file:
        file.seek(0)
        file.write("BookID,Title,Author,Price,Quantity\n")

        for book in lines:
            row = ""
            for i, item in enumerate(book):
                row += str(item)  # convert to string manually
                if i != len(book) - 1: # only add comma if this is not the last iteem
                    row += "," # add comma between items
            row += "\n" # add newline at the end
            file.write(row)

    bookrecord.clear()
    load_books(bookrecord)
