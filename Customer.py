# Methods that can be called by customers

from datetime import datetime
from library_memory import *
from file_handling import *
from Abstract import *


class Customer(CustomersBluePrint):
    def __init__(self, name: str, email: str):
        self.__cust_name = name
        self.__cust_email = email

    def add_customer_to_memory(self,name,email):
        custrecord.append([name,email])

    def view_available_books(self):
        '''Shows customers all available books'''
        filtered_available_books = []

        for book in bookrecord:
            if book[4] > 0:
                filtered_available_books.append(book[:4]) # only shows title, author, and price without the availability for a neater look (since availability is True anyways)
        '''Filters books by availability and adds them to a new list'''
        return filtered_available_books
    
    def borrow_book(self,id,email):
        id_2b_borrowed = id

        if not isinstance(id_2b_borrowed,int) or id_2b_borrowed<=0:
            raise ValueError

        for book in bookrecord:
            if book[0] == id_2b_borrowed:
                if book[4] < 1:
                    return False
                else:
                    if email not in borrowed_books.keys(): #checks if the user has borrowed books
                        borrowed_books[email] = [] #if the user hasnt borrowed any books before, 
                        #if yes, a new key and empty list is initialized for them in the borrowed_books dictionary to add their borrowed books
                        # key: user's email, value: list of borrowed books (each book is a list with the title, author, etc...)
                    book[4] = book[4] - 1 #changes book availability to False
                    borrowed_books[email].append([book[0],book[1]]) #books is added to their list of borrowed books
                    change_quantity(id_2b_borrowed,"borrow")
                    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    save_borrowing_record(self.__cust_name,self.__cust_email,id_2b_borrowed,"borrow",timestamp)
                    load_borrowing_log(borrowing_log)
                    return True
        return False
    
    def return_book(self,id,email):
        id_2b_returned = id

        if not isinstance(id_2b_returned,int) or id_2b_returned<=0:
            raise ValueError
        
        for book in bookrecord:
                if book[0] == id_2b_returned:
                    book[4] = book[4] + 1 
            
        for key, books in borrowed_books.items():
            if key == email: # finds the user in the borrowed_books dictionary
                for borrowed_book in books:
                    if borrowed_book[0] == id_2b_returned: # finds the book they want to return in the list of all their borrowed books
                        books.remove(borrowed_book) # removes the book from the list of their borrowed books
                        change_quantity(id_2b_returned,"return")
                        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        save_borrowing_record(self.__cust_name,self.__cust_email,id_2b_returned,"return",timestamp)
                        load_borrowing_log(borrowing_log)
                        return True
                    
        return False

    def view_borrowed_books(self,current_user_email):
        for email, books in borrowed_books.items():
            if email == current_user_email:
                return books
