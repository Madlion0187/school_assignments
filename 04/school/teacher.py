class Teacher:
    
    def __init__(self, id, name, depart):
        self.id = id
        self.name = name
        self.depart = depart
        
    def __str__(self):
        return f"{self.name}"