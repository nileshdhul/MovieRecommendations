import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
genres=pickle.load(open('movies.pkl','rb'))
movies=pickle.load(open('movies_.pkl','rb'))
cv=pickle.load(open('cv.pkl','rb'))

st.title("movie Recommender System")
s=""
for i in genres:
    s+=i+" "


txt = st.text_area('Enter the Genres of movies that you want to see such as :'+s, '''
     
     ''')
txt1 = st.text_area('Enter the actors name (name and surname without space) whose movies you want to seefor ex:(akshaykumar) :', '''

     ''')
txt2= st.text_area('Enter the name of directors (name and surname without space)whose movies  you want to see for ex:(martinscorsese) :', '''

     ''')
txt3= st.text_area('Enter the description of movies you want to see some keywords for ex(magic,crime,drama,power production company(disney ,fox) etc) :', '''

     ''')



movies_dsc=txt+txt1+txt2+txt3
movies_dsc=movies_dsc.lower()

def recommend(movies_dsc):
    new_movie=movies
    df2 = {'title': 'new_movie', 'tags': movies_dsc}
    df = pd.DataFrame(df2, index=[0])
    new_movie = new_movie.append(df2, ignore_index = True)
    x=cv.fit_transform(new_movie['tags']).toarray()
    similarity_n=cosine_similarity(x)
    def recommend_new(movie):
        movie_index=new_movie[new_movie['title']==movie].index[0]
        # print(movie_index)
        distances=similarity_n[movie_index]
        # print(distances)
        movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]
        for i in movie_list:
            print(movies.iloc[i[0]].title)
            st.write(movies.iloc[i[0]].title)
    recommend_new("new_movie")

if st.button('recommend'):
    recommend(movies_dsc)