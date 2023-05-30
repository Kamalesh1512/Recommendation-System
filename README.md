# Recommeder-System
Movie Recommender System (content Based)

Main focus of our recommendation system is to filter and predict only those movies which a user would prefer given some data about the user him or herself.

The algorithm recommends movies that are similar to the ones that a user has liked in the past.
This similarity (generally cosine similarity) is computed from the data we have about the items as well as the user’s past preferences.

Project Flow:
Data collection --> Data Preprocessiong --> Model Building --> Website -->deployment

Dataset used : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Model build using a Text-vectorization method called CountVectorizer from sklearn.feature_extraction.text

Website created using a Streamlit web-framework and hosted with the help of streamlit sharing




