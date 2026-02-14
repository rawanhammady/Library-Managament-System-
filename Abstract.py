# Blueprint for the methods that can be called by customers and librarians

from abc import ABC, abstractmethod

class CustomersBluePrint(ABC):
    '''Blue print for all methods that can be called by customers'''

    @abstractmethod
    def add_customer_to_memory(self,name,email):
        '''Adds user to memory'''
        pass
    @abstractmethod
    def borrow_book(self):
        '''Allows customers to borrow a book by enetring the ID of the book'''
        pass
    @abstractmethod
    def return_book(self):
        '''Allows customers to return a book by enetring the ID of the book'''
        pass
    @abstractmethod
    def view_available_books(self):
        '''Shows all available books and their relevant information (ID, price, etc...)'''
        pass

    @abstractmethod
    def view_borrowed_books(self):
        '''Shows all borrowed books byt the current user'''
        pass


class LibrariansBluePrint(ABC):
    '''Blue print for all methods that can be called by libraraians'''

    @abstractmethod
    def add_librarian_to_memory(self,name:str,email:str):
        '''Adds user to memory'''
        pass

    @abstractmethod
    def view_customers_record(self):
        ''' Allows librarians to view the names and emails of all customers that have used the system '''
        pass
    @abstractmethod
    def view_librarians_record(self):
        '''Allows librarians to view the names and emails of all librarians that have used the system'''
        pass
    @abstractmethod
    def view_all_books(self):
        '''Allows user to view all books'''
        pass

    @abstractmethod
    def view_borrowed_books(self,current_user_email:str):
        '''Allows user to view books borrowed by an individual by entering their email'''
        pass

    @abstractmethod
    def add_books(self,title:str,author:str,price:float,quantity:int):
        '''Allows librarians to add books to the system. User will be asked to enter relevant book information. 
        Book ID is automatically generated'''
        pass
