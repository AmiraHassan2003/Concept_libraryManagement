
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
# print(book.addBook("title1", "author1", "genre1"))
# print(book.removeBook(12))

# print(book.searchTitleBook("www", titles, authors, genres))
# print(book.searchAuthorBook("a1", titles, authors, genres))
# print(book.searchGenreBook("333", titles, authors, genres))

# print(book.updateTitle(7, "qqqqq", ids_book, authors, genres ))
# print(book.updateAuthor(5, "sss", ids_book, titles, genres))
# print(book.updateGenre(5, "gggg", ids_book, titles, authors))

# print(book.getAllBooks(titles, authors, genres))

        #################### Member ############################
# print(member.addMember("mmmm", "012345"))
# print(member.viewMember(2, names, phones))
# print(member.updateName(3, "nenen", ids_member, phones))
# print(member.updatePhone(3, "11111", ids_member, names))

        ######################## Borrowing #######################
# print(borrow.borrowBook(2, 10, "6/7/20003", "6/8/2003", booksList, memberBorrowingList))
# print(borrow.historyBook(5))
# borrow.historyMember(2)
