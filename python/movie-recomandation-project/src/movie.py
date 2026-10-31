class Movie():
    def __init__(self, id: str, title: str, genre: str, description: str, rating: str):
        if any([id, title, genre, description, rating], None):
            raise ValueError("Missing arguments.")

        self.id = id
        self.title = title
        self.genre = genre
        self.description = description
        self.rating = rating
