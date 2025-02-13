
from book import BookManagement
from member import Member
from borrowings import Borrowings

book = BookManagement()
member = Member()
borrow = Borrowings()

ids_book = book.getIds()
titles = book.getTitles()
authors = book.getAuthors()
genres = book.getGenres()

ids_member = member.getIds()
names = member.getNames()
phones = member.getPhones()

booksList = borrow.getBooks()
memberBorrowingList = borrow.getMembers()
titleBookBorrowingList = borrow.getTitleBookBorrowing()
borrowDateList = borrow.getBorrowDate()
returnDateList = borrow.getReturnDate()



    ######################## Book ##########################
# print(book.addBook("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
# print(book.removeBook(12))

# print(book.searchTitleBook("To Kill a Mockingbird", titles, authors, genres))
# print(book.searchAuthorBook("J.K. Rowling", titles, authors, genres))
# print(book.searchGenreBook("Mystery", titles, authors, genres))

# print(book.updateTitle(7, "1984", ids_book, authors, genres))
# print(book.updateAuthor(5, "George Orwell", ids_book, titles, genres))
# print(book.updateGenre(5, "Dystopian", ids_book, titles, authors))

# print(book.getAllBooks(titles, authors, genres))

        #################### Member ############################
# print(member.addMember("Alice Johnson", "0123456789"))
# print(member.viewMember(2, names, phones))
# print(member.updateName(3, "Michael Smith", ids_member, phones))
# print(member.updatePhone(3, "0987654321", ids_member, names))

        ######################## Borrowing #######################
# print(borrow.borrowBook(2, 10, "6/7/20003", "6/8/2003", booksList, memberBorrowingList))
# print(borrow.historyBook(5))
# borrow.historyMember(2)
