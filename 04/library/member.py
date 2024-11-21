class Member:
    
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self):
        return f"{self.name}"