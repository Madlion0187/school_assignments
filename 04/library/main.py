from book import Book
from member import Member
from book_rent import Book_rent

book1 = Book(1, "The lord of the rings", "J.R.R. Tolkien")
book2 = Book(2, "Song of ice and fire", "George R.R. Martin")

member1 = Member(1, "Frank Smith", "frank@gmail.com")

book_rent = Book_rent(member1, book2, "2024-11-20")

print(book_rent)

