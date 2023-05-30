import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('movie-recommender')
selected_movie = st.selectbox("Select the movie",
                      movies['title'].values)
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=332dca06f080cbc7772a81c2086e8546&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    movies_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=(lambda x:x[1]))[1:6]
    rec_list=[]
    poster_lst=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        rec_list.append(movies.iloc[i[0]].title)
        poster_lst.append(fetch_poster(movie_id))
    return rec_list,poster_lst
if st.button("Recommend"):
   names,posters= recommend(selected_movie)
   col1, col2,col3,col4,col5 = st.columns(5,gap="small")
   with col1:
       col1.text(names[0])
       col1.image(posters[0])
   with col2:
       col2.text(names[1])
       col2.image(posters[1])
   with col3:
       col3.text(names[2])
       col3.image(posters[2])
   with col4:
       col4.text(names[3])
       col4.image(posters[3])
   with col5:
       col5.text(names[4])
       col5.image(posters[4])

