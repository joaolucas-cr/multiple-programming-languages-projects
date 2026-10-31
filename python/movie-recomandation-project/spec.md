
# Movie Recommendation System

## Project 3 — Python

**Difficulty:** Intermediate (7/10)  
**Estimated Time:** 12–20 hours  
**Language:** Python  
**Interface:** Command Line (CLI)

---

## 1. Project Overview

Develop a movie recommendation system that analyzes movie information and suggests movies based on similarity and user preferences.

The application must allow users to search for movies, filter by genre, rate movies, and receive personalized recommendations.

The project introduces machine learning concepts, data processing, similarity algorithms, and persistent storage.

## 2. Technologies

- Python 3
- Pandas
- Scikit-learn
- JSON
- CSV
- MovieLens or TMDB dataset

## 3. Functional Requirements

### FR-01: Load Movie Dataset

The application must load movie information from a CSV file.

Each movie should contain:

- Unique movie ID
- Title
- Genre(s)
- Description
- Average rating

The system must validate the dataset and handle missing information.

### FR-02: Search Movies

Users must be able to search for movies by title.

Requirements:

- Case-insensitive search
- Partial title matching
- Display matching movies
- Handle searches with no results

### FR-03: Genre Filtering

Users must be able to filter movies by genre.

Requirements:

- Display available genres
- Support movies with multiple genres
- Return all movies matching the selected genre
- Handle invalid genres

### FR-04: Movie Similarity

The system must calculate similarity between movies using their descriptions and genres.

Requirements:

- Convert textual movie information into numerical features
- Implement TF-IDF vectorization
- Calculate cosine similarity
- Rank movies by similarity score
- Exclude the selected movie from its own recommendations

### FR-05: Movie Recommendations

Users must be able to select a movie and receive five similar recommendations.

Each recommendation must display:

- Movie title
- Genre(s)
- Average rating
- Similarity score

If fewer than five eligible movies exist, return the available results.

### FR-06: User Ratings

Users must be able to rate movies.

Requirements:

- Ratings range from 1 to 5
- Support updating existing ratings
- Associate ratings with movie IDs
- Reject invalid ratings
- Save ratings persistently

### FR-07: Personalized Recommendations

The system must generate recommendations based on movies previously rated by the user.

Requirements:

- Analyze positively rated movies
- Compare candidate movies against user preferences
- Rank recommendations using similarity scores
- Exclude movies already rated by the user
- Handle users without rating history

The recommendation strategy must be documented.

### FR-08: Persistent Storage

User ratings must be stored in a JSON file.

Requirements:

- Load existing ratings at startup
- Save new or updated ratings
- Handle missing storage files
- Handle malformed JSON gracefully
- Avoid duplicate ratings for the same movie

### FR-09: Dataset Statistics

The application must display:

- Total number of movies
- Number of movies per genre
- Average movie rating
- Highest-rated movie
- Lowest-rated movie

Statistics requiring ratings must handle missing or unavailable rating values.

### FR-10: Command-Line Interface

Implement an interactive terminal menu.

Example:

```text
=================================
      MOVIE RECOMMENDER
=================================

1. Search Movies
2. Browse by Genre
3. Recommend Similar Movies
4. Rate a Movie
5. Personalized Recommendations
6. View Statistics
7. Exit

Select an option:
```

The application must continue running until the user selects Exit.

## 4. Non-Functional Requirements

### NFR-01: Code Organization

- Separate business logic from storage logic
- Use functions and classes where appropriate
- Avoid unnecessary code duplication
- Use descriptive names

### NFR-02: Error Handling

Handle:

- Invalid menu selections
- Missing files
- Invalid movie IDs
- Invalid ratings
- Empty search results
- Missing dataset fields
- Empty recommendation results

### NFR-03: Performance

- Avoid recalculating vector representations unnecessarily
- Load the dataset once during initialization
- Keep recommendation queries reasonably responsive
- Avoid storing redundant data

### NFR-04: Data Integrity

- Movie IDs must remain unique
- User ratings must reference valid movies
- Updates must not create duplicate ratings
- Storage operations must preserve valid existing data

## 5. Suggested Architecture

```text
movie-recommender/
├── main.py
├── models/
│   └── movie.py
├── services/
│   ├── recommender.py
│   └── statistics.py
├── storage/
│   └── storage.py
├── data/
│   ├── movies.csv
│   └── ratings.json
├── requirements.txt
└── README.md
```

This structure is a recommendation, not a strict requirement.

## 6. Recommendation Algorithm

### 6.1 Content-Based Filtering

The recommendation system must use movie attributes to identify similar movies.

Suggested process:

1. Load movie descriptions and genres.
2. Clean and normalize textual data.
3. Combine relevant text features.
4. Convert text into TF-IDF vectors.
5. Calculate cosine similarity.
6. Rank candidate movies.
7. Return the five highest-ranked eligible movies.

### 6.2 Personalized Recommendations

Suggested process:

1. Load user ratings.
2. Identify movies rated positively.
3. Calculate similarity between those movies and other movies.
4. Weight similarity scores according to user ratings.
5. Aggregate the weighted scores.
6. Exclude already-rated movies.
7. Return the five highest-ranked recommendations.

The implementation must define how positive ratings and rating weights are interpreted.

## 7. Data Requirements

The selected dataset must provide enough information to support the required features.

Required fields:

| Field | Type | Description |
|---|---|---|
| movie_id | Integer/String | Unique identifier |
| title | String | Movie title |
| genres | String/List | Movie genres |
| description | String | Movie summary |
| rating | Float | Average movie rating |

If the dataset lacks required information, the developer must document how that information is obtained or how the dataset is adapted.

## 8. Testing Requirements

The application must be tested against the following scenarios.

### Dataset Tests

- Valid dataset loads successfully
- Missing dataset file
- Missing required columns
- Duplicate movie IDs
- Empty dataset

### Search Tests

- Exact title search
- Partial title search
- Case-insensitive search
- Nonexistent movie

### Recommendation Tests

- Valid movie ID
- Invalid movie ID
- Selected movie is excluded
- Results are ordered by similarity
- Fewer than five eligible movies

### Rating Tests

- Valid rating
- Invalid rating
- Update existing rating
- Save and reload ratings
- Invalid movie ID

### Personalized Recommendation Tests

- No user ratings
- One positively rated movie
- Multiple positively rated movies
- All candidate movies already rated

## 9. Development Milestones

### Milestone 1 — Data Management

- [ ] Select and download a movie dataset
- [ ] Implement dataset loading
- [ ] Validate required fields
- [ ] Implement movie search
- [ ] Implement genre filtering

### Milestone 2 — Recommendation Engine

- [ ] Implement text preprocessing
- [ ] Implement TF-IDF vectorization
- [ ] Implement cosine similarity
- [ ] Rank movies by similarity
- [ ] Return five recommendations

### Milestone 3 — User Preferences

- [ ] Implement movie ratings
- [ ] Implement JSON persistence
- [ ] Support updating ratings
- [ ] Implement personalized recommendations
- [ ] Exclude previously rated movies

### Milestone 4 — Application Integration

- [ ] Build the CLI menu
- [ ] Integrate all features
- [ ] Implement dataset statistics
- [ ] Add input validation
- [ ] Handle application errors

### Milestone 5 — Testing and Documentation

- [ ] Test all functional requirements
- [ ] Test edge cases
- [ ] Create README.md
- [ ] Document installation instructions
- [ ] Document recommendation algorithms
- [ ] Verify application execution

## 10. Completion Criteria

The project is complete when:

1. All functional requirements are implemented.
2. The application runs through the terminal.
3. Users can search and filter movies.
4. The system recommends similar movies.
5. Users can save and update ratings.
6. Personalized recommendations work.
7. Data persists between executions.
8. Invalid inputs do not crash the application.
9. All required tests pass.
10. The repository includes documentation.

---

## 11. Optional Extensions

These features are not required for project completion.

- Collaborative filtering
- Multiple user profiles
- Recommendation explanations
- Movie poster integration
- Recommendation history
- REST API
- Web interface
- Recommendation evaluation metrics
- Hybrid recommendation algorithms

---

## 12. Project Constraints

- The core application must be written in Python.
- The interface must work without a web browser.
- User ratings must persist locally.
- Recommendation calculations must use actual movie features.
- Recommendations must not be randomly generated.
- Required features must not depend on paid APIs.
- The application must be executable using documented setup instructions.
