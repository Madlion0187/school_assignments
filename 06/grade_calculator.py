class GradeCalculator:
    
    def __init__(self, testScore, devScore):
        self.testScore = testScore
        self.devScore = devScore
        
    def get_avg(self):
            return (self.testScore + self.devScore) / 2
        
    def get_score(self):
        avg = self.get_avg()
        
        if avg >= 90:
            return("5")
        elif avg >= 80:
            return("4")
        elif avg >= 70:
            return("3")
        elif avg >= 60:
            return("2")
        else:
            return("1")
        
    def __str__(self):
        return f"Your grade is: {self.get_score()}"
        
calculator = GradeCalculator(80, 75)    
print(calculator)