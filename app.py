import streamlit as st
import pickle

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.write(type(similarity))
st.write(similarity)
st.write("Available titles:", movies['title'].head())

movies_list = movies['title'].values
similarity = similarity['title'].values

st.header("Movie Recommendation System")
selectValue = st.selectbox("Select a movie", movies_list)
st.write("Movie selected:", selectValue)


def recommend(movie):
    index = movies[movies['title'] ==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommended_movies = []
    for i in distance[0:5]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button("Recommend"):
    movie_name = recommend(selectValue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])