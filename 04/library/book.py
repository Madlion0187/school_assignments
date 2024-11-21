class Book:
    
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title}"