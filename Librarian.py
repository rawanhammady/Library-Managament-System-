# Methods that can be called by librarians

from Abstract import LibrariansBluePrint
from library_memory import *
from file_handling import *

librarians = []

class Librarian(LibrariansBluePrint):
    '''All methods that can be used by librarians'''

    def __init__(self, name: str, email: str):
        super().__init__()
        self.__lib_name = name
        self.__lib_email = email

    def add_librarian_to_memory(self,name:str,email:str):
        librecord.append([name,email])

    def view_customers_record(self):
        return load_user_info(custrecord,"customer")

    def view_librarians_record(self):
        return load_user_info(librecord,"librarian")
    
    def view_all_books(self):
        return bookrecord
    
    def view_borrowed_books(self,current_user_email:str):
        user_books = []
        for email, books in borrowed_books.items():
            if email == current_user_email:
                for book in books:
                    user_books.append([book[0],book[1]])
        return user_books
    
    def add_books(self,title:str,author:str,price:float,quantity:int):
        if (not isinstance(title,str)) or (not isinstance(author,str)) or (not isinstance(price,float)) or (not isinstance(quantity,int)):
            raise ValueError

        new_id = bookrecord[-1][0] + 1
        for book in bookrecord:
            if new_id == book[0]:
                return False
        bookrecord.append([new_id,title,author,price,quantity])
        save_new_book(new_id,title,author,price,quantity)
        return True
