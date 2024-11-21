class Book_rent:
    
    def __init__(self, member, book, rent_start_date, rent_end_date = "2024-12-31"):
        self.member = member
        self.book = book
        self.rent_start_date = rent_start_date
        self.rent_end_date = rent_end_date
        
    def __str__(self):
        return f"{self.member} rented {self.book} from {self.rent_start_date} until {self.rent_end_date}"