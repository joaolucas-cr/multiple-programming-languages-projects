import pandas as pd

class MoviesCollection():
    def __init__(self, movies_filepath: str, rating_filepath: str):
        if not movies_filepath:
            raise ValueError("Missing movies file path.")
        if not rating_filepath:
            raise ValueError("Missing rating file path.")
        
        self.movies_filepath = movies_filepath
        self.rating_filepath = rating_filepath

    def load(self):
        movies_df = pd.read_csv(self.movies_filepath)
        rating_df = pd.read_csv(self.rating_filepath)

        rating_df = rating_df.drop_duplicates()
        rating_df = rating_df.dropna()

        movies_df = movies_df.drop_duplicates()
        movies_df = movies_df.dropna()

        self.movies_df = movies_df
        self.rating_df = rating_df


    def search(self, search_term: str) -> list[str]:
        searched = self.movies_df[self.movies_df["title"].str.contains(search_term)]
        print(f"Searched for \"{search_term}\" and found:")
        print(searched.to_string(index=False))

    def getGenres(self) -> list[str]:
        return self.movies_df["genres"].str.split("|").explode().unique()

    def search_by_genre(self) -> list[str]:
        genres = self.getGenres()
        print("Genres: ",", ".join(genres))
        genreSelected = input("type the genre you want: ")
        if(not genreSelected in genres): 
            raise ValueError("Genre not supported.")
        return self.movies_df[self.movies_df['genres'].str.contains(genreSelected)].to_string(index=False)



