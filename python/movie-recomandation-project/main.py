from src.moviescollection import MoviesCollection
from src.cli import CLI
from src.recommandation import getSimilarity
import sys


def main():
    movies_collection = MoviesCollection("./src/data/movies.csv", "./src/data/ratings.csv")
    movies_collection.load()
    arguments = sys.argv
    arguments.pop(0)
          
    cli = CLI(arguments, movies_collection)


if __name__ == "__main__":
    main()