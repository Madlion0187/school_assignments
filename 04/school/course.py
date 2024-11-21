class Course:
    
    def __init__(self, id, name, teacher):
        self.id = id
        self.name = name
        self.teacher = teacher
        
    def __str__(self):
        return f"{self.name}"