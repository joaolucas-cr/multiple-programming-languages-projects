"""
COMMANDS: 
| `scrape` | Start a scraping session |
| `list` | Display stored books |
| `search` | Search saved books by title |
| `stats` | Display dataset statistics |
| `export` | Export saved records to CSV |
"""
from .scraper import scrape
from . import storage 

def processArguments(arguments=[""]):
    if(not isinstance(arguments, list)):
        raise ValueError("Arguments must be an array")
    arguments.pop(0)
    books = storage.getBooksObj()

    for i, argument in enumerate(arguments): 
        match argument:
            case "scrape":
                print("Starting scrape...")
                try:
                    if(len(arguments) > 1):
                        scrape(int(arguments[i+1]))
                    else:
                        scrape()
                except:
                    scrape()
            case "list":
                print("Listing:")
                for book in books:
                    print(book, "\n")
            case "search":
                print("Searching...")
                if len(arguments) == 1:
                    raise ValueError("No search term given")
                
                searchTerm = arguments[1]
                foundOne = False
                for book in books:
                    if searchTerm.lower() in book.title.lower():
                        print(book)
                        foundOne = True

                if not foundOne:
                    print("No books found for this search")
            case "stats":
                print("Loading stats...")
                totalBooks = len(books)
                prices = [book.price for book in books]
                totalInStock = len([book for book in books if book.availability == "IN_STOCK"])
                totalOutStock = len([book for book in books if book.availability == "OUT_OF_STOCK"])

                print("Total Numbers:", totalBooks)
                print("Avarage Price:", round((sum(prices) / totalBooks), 2))
                print("Minimum Price:", min(prices))
                print("Maximum Price:", max(prices))
                print("Number of in-stock books:", totalInStock)
                print("Number of out-of-stock books", totalOutStock)


            case "export":
                print("Exporting...")
                if len(arguments) == 1:
                    raise ValueError("No filename given")

                filename = arguments[1]
                with open(f"{filename}.csv", "w") as file:
                    content = "id,title,price,availability,product_url,rating\n"
                    for book in books:
                        content += ",".join(list([str(value) for value in book.toDict().values()]))
                        content += "\n"
                    file.write(content)
                print("DONE EXPORTING!")


