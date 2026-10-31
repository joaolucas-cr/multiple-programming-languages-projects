from .recommandation import getSimilarity
from .ratings import getRatings, saveRating, getRatingsAndMovies
import numpy as np
class CLI():
    def __init__(self, arguments: list[str], movie_collection):
        match arguments[0]:
            case "search":
                movie_collection.search(arguments[1])

            case "search-genre":
                results = movie_collection.search_by_genre()
                print("Results:\n", results)

            case "similarity":
                movieId = arguments[1]
                index = movie_collection.movies_df.index[movie_collection.movies_df['movieId'] == int(movieId)][0]
                print('Movie Selected: ', movie_collection.movies_df.iloc[index]['title'])
                suggestions = getSimilarity(movie_collection.movies_df, [index])
                print(suggestions)

            case "rate":
                movieId = arguments[1]
                rating = arguments[2]
                saveRating(movieId, rating)

            case "recommend": 
                ratings = getRatings()
                moviesRated = getRatingsAndMovies(movie_collection)['movieId']
                indexes = [i for i in movie_collection.movies_df.index[movie_collection.movies_df['movieId'].isin(moviesRated)]]
                similarity = getSimilarity(movie_collection.movies_df, indexes, list(ratings.values())) 
                print(similarity)

            case 'see-rate':
                print(getRatingsAndMovies(movie_collection))

            case "stats":
                ratings = getRatings()
                print("Movies: ", len(movie_collection.movies_df))
                genres = movie_collection.getGenres()
                print("Genre:")
                for genre in genres:
                    print(f"   {genre} - {len(movie_collection.movies_df[movie_collection.movies_df['genres'].str.contains(genre, regex=False)])}")
                avg = np.average(list(ratings.values()))
                print("Average:", avg)
                sortedRates = sorted(ratings.items())
                highestId = sortedRates[-1][0]
                lowestId = sortedRates[0][0]
                print("Highest rated: ", movie_collection.movies_df[movie_collection.movies_df["movieId"] == int(highestId)])
                print("Lowest rated: ", movie_collection.movies_df[movie_collection.movies_df["movieId"] == int(lowestId)])




    