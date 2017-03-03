class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.book_list = []
        
    def add_book(self, book):
        self.book_list.append(book)
        
    def get_books(self):
        return self.book_list 
        
        
    def search_books(self, title=None, author=None):
        search_result = []
        
        for book in self.book_list:
            if title is not None and title.lower() in book.title.lower():
                search_result.append(book)
            if author is not None and author == book.author:
                search_result.append(book)
        return search_result
        
    
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books
    
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
