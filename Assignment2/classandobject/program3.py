#Library management system
class Book():
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f'Details of book: Title of Book {self.title} author is {self.author} and isbn is {self.isbn}')
        
book=Book("Ramayana","valmiki",191)
book.display()
        