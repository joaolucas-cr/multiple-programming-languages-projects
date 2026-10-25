from uuid import uuid4 as generateUUID
from urllib import parse


class Book():
    def __init__(self, title: str, price: float, availability: str, product_url: str, rating: int, id: str=""):
        if(not title or not price or not availability  or not product_url or not rating):
            raise ValueError("missing parameter")

        if(not parse.urlparse(product_url).scheme):
            raise ValueError(f"{title}: Product URL must be an absolute url")
        if price < 0:
            raise ValueError(f"Price must not be negative")

        if availability != "IN_STOCK" and availability != "OUT_OF_STOCK":
            raise ValueError(f"Not valid value for availability")

        if rating < 1 or rating > 5:
            raise ValueError(f"Not valid rating. Rating must be between 1 and 5")
        if(id):
            self.id = id
        else:
            self.id = str(generateUUID())
        self.title = title
        self.price = price
        self.availability = availability
        self.product_url = product_url
        self.rating = rating

    def getIdentification(self):
        return f"{self.title}-{self.price}" 

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price, 
            "availability": self.availability,
            "product_url": self.product_url,
            "rating": self.rating
        }

    def __str__(self):
        return f"{self.id} - {self.title} - {self.price} - {self.availability} - {self.product_url} - {self.rating}"