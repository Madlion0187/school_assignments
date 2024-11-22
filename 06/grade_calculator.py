class GradeCalculator:
    
    def __init__(self, testScore, devScore):
        self.testScore = testScore
        self.devScore = devScore
        
    def get_avg(self):
            return (self.testScore + self.devScore) / 2
        
    def get_score(self):
        avg = self.get_avg()
        
        if avg >= 90:
            return("Your grade is: 5")
        elif avg >= 80:
            return("Your grade is: 4")
        elif avg >= 70:
            return("Your grade is: 3")
        elif avg >= 60:
            return("Your grade is: 2")
        else:
            return("Your grade is: 1")
        
calculator = GradeCalculator(80, 75)    
print(calculator.get_score())