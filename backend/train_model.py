import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv('../dataset/movies.csv')
ratings = pd.read_csv('../dataset/ratings.csv')

# Merge datasets
data = pd.merge(ratings, movies, on='movieId')

# Create user-movie matrix
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# Fill missing values with 0
user_movie_matrix = user_movie_matrix.fillna(0)

# Compute similarity between movies
movie_similarity = cosine_similarity(user_movie_matrix.T)

# Convert to dataframe
movie_similarity_df = pd.DataFrame(movie_similarity,
                                   index=user_movie_matrix.columns,
                                   columns=user_movie_matrix.columns)

# Save model
pickle.dump(movie_similarity_df, open('../models/recommender_model.pkl', 'wb'))

print("Model trained and saved successfully!")