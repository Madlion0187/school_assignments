class Book:
    
    avaible = 20
    
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"My favorite book is {self.title} by {self.author}.\n We have {self.avaible} books."
    
book1 = Book(1, "The lord of the rings", "J.R.R. Tolkien")

print(book1)