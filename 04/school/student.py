class Student:
    
    def __init__(self, id, name, average):
        self.id = id
        self.name = name
        self.average = average
        
    def __str__(self):
        return f"{self.name}"