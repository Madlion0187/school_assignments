class Grade:
    
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
        
    def __str__(self):
        return f"{self.grade}"
        