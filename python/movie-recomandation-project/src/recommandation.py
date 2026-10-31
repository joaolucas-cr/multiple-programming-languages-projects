from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vectorizer = TfidfVectorizer(stop_words="english")

def getSimilarity(movies: object, index: list[int] = [0], rating: list[int] = None) -> list[str]:
    movies['features'] = movies['genres'].fillna("").str.replace("|", " ", regex=False)
    tfMatrix = vectorizer.fit_transform(movies['features'])
    print(index)
    similarities = cosine_similarity(tfMatrix[index], tfMatrix)

    weightedScores = np.average(
        similarities,
        axis=0,
        # weights=[5]
    )

    if rating:
        weightedScores = np.average(
            similarities,
            axis=0,
            weights=rating
        )
    else: 
        weightedScores = np.mean(similarities, axis=0)


    rankedIndex = (np.argsort(weightedScores)[::-1])
    topFive = [
        i for i in rankedIndex
            if not i in index
    ][:5]

    movies_suggestions = [
        movies.iloc[i] for i in topFive
    ]

    return movies_suggestions


    
    