# These lists and dictionaries are the program's memory while running. they are loaded from the files to remember users from previous runs

bookrecord = []
librecord = []
custrecord = []
borrowed_books = {} # each key is a user's email, and the respective value is a list of lists of books (and book info) borrowed by them
borrowing_log = []