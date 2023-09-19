class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
    def set_page(self,new_page):
        self.pages = new_page


# Usage:

book2 = Book("The Alchemist","Paulo Coelho",208)
print(book2.get_info())
book2.set_page(200)
print(book2.get_info())
