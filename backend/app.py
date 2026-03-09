from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

from recommender import recommend

app = Flask(__name__)
CORS(app)

movies = pd.read_csv('../dataset/movies.csv')
ratings = pd.read_csv('../dataset/ratings.csv')


@app.route('/')
def home():
    return "AI Movie Recommendation API Running"


# Recommendation API
@app.route('/recommend/<path:movie_name>')
def get_recommendation(movie_name):

    results = recommend(movie_name)

    return jsonify({
        "recommendations": results
    })


# Search autocomplete
@app.route('/search/<query>')
def search(query):

    movie_list = movies['title'].tolist()

    result = [m for m in movie_list if query.lower() in m.lower()]

    return jsonify(result[:10])


# Trending movies
@app.route('/trending')
def trending():

    data = pd.merge(ratings, movies, on='movieId')

    top = data.groupby('title')['rating'].count().sort_values(ascending=False).head(10)

    return jsonify(list(top.index))


if __name__ == "__main__":
    app.run(debug=True)