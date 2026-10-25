from requests import request
from bs4 import BeautifulSoup
from .book import Book
from time import sleep
from sys import exit
from . import storage
PAGE_URL = "https://books.toscrape.com"
EXTENSION_URL = 'catalogue/page-'

def scrape_catalog(url):
    headers = {
        "User-Agent": "MyPythonScraper/1.0"
    }   
    response = request("GET", url, headers=headers)
    response.raise_for_status()
    if response.status_code == 429:
        exit()
    soup = BeautifulSoup(response.text, "html.parser")
    articlesEl = soup.find_all("article", class_="product_pod")
    
    print(f"found elements: {len(articlesEl)}")
    for articleEl in articlesEl:
        a = articleEl.find("h3").find("a")
        starsDiv = articleEl.find("p", class_="star-rating")
        rating = 0
        ratingStr = starsDiv.get("class")[1]
        match ratingStr:
            case "One": 
                rating = 1
            case "Two":
                rating = 2
            case "Three":
                rating = 3
            case "Four":
                rating = 4
            case "Five":
                rating = 5
        priceDiv = articleEl.find("div", class_="product_price").find("p", class_="price_color")
        instockDiv = articleEl.find("div", class_="product_price").find("p", class_="availability")
        title = a.get("title")
        price = float(priceDiv.text[2:])
        availability = instockDiv.text.strip().replace(" ", "_").upper()
        product_url = f"{PAGE_URL}/{a.get("href")}"
        try: 
            book = Book(title, price, availability, product_url, rating)
            storage.saveBook(book)
        except Exception as error:
            print(error)
            continue

    sleep(1)
    print(soup.title.text)

def scrape(pages: int=1):
    if isinstance(pages, str):
        return
    if pages < 1:
        pages=1
    if pages > 50:
        pages = 50
    storage.deleteALl()
    for page in range(pages):
        if page == 0:
            scrape_catalog(PAGE_URL)
        else:
            scrape_catalog(f"{PAGE_URL}/{EXTENSION_URL}{page+1}.html")
    print("Succesfully scraped!")