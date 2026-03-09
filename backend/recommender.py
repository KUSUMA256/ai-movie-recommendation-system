import pickle
import requests
import re

# Load trained similarity model
model = pickle.load(open('../models/recommender_model.pkl','rb'))

API_KEY = "dae7be9185e25edea3b7ef3ff7d08fc9"

def get_movie_details(movie):

    # Remove year or extra text
    movie_clean = re.sub(r"\(.*?\)", "", movie).strip()

    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_clean}"

    data = requests.get(url).json()

    if data["results"]:

        poster_path = data["results"][0]["poster_path"]
        rating = data["results"][0]["vote_average"]

        if poster_path:
            poster = "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            poster = ""

        return poster, rating

    return "", "N/A"


def recommend(movie_name):

    if movie_name not in model.columns:
        return []

    similar_movies = model[movie_name].sort_values(ascending=False)[1:6]

    results = []

    for movie in similar_movies.index:

        poster, rating = get_movie_details(movie)

        results.append({
            "title": movie,
            "poster": poster,
            "rating": rating
        })

    return results