import json

def getRatings()-> object:
    with open('./src/data/ratings.json', 'r') as file:
        ratings = json.load(file)
        return (ratings)


def saveRating(movieId: str, rating: int):
    ratings = getRatings()
    rating = int(rating)
    if rating < 1 or rating > 5:
        raise ValueError("Rating out of the range (1-5)")
    ratings[movieId] = rating
    with open('./src/data/ratings.json', 'w') as file:
        json.dump(ratings, file)


def getRatingsAndMovies(movies_collection):
    ratings = getRatings()
    moviesIds = [int(i) for i in list(ratings.keys())]
    mv =  movies_collection.movies_df[movies_collection.movies_df['movieId'].isin(moviesIds)]
    return mv
         
