import json
from .book import Book

filePath = "./objects/db.json"
def _readFile():
    with open(filePath, "r") as file:
        return json.load(file)

def getBooks():
    books = _readFile()
    return books["books"]

def _writeFile(content):
    with open(filePath, "w") as file:
        return json.dump({"books":content}, file, indent=True)
    
def saveBook(book):
    books = getBooks()
    if any(bk["id"] == book.id for bk in books):
        return
    if any(bk['title'] == book.title for bk in books):
        return
    books.append(book.toDict())
    _writeFile(books)

def deleteALl():
    _writeFile([])

def getBooksObj():
    books = getBooks()
    return [Book(book['title'], book['price'], book['availability'], book['product_url'], book['rating'], id=book['id']) for book in books]
