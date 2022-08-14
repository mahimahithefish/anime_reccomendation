import streamlit as st
import pickle
import pandas as pd

df = pd.read_csv('animes.csv')

image_urls = df['img_url'].tolist() # image urls
uid = df['uid'].tolist() # anime ids
titles = df['title'].tolist() # anime titles

def rec_anime(current_anime):
    anime_index = anime[anime['title'] == current_anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]

    reccomended_animes = []
    for i in anime_list:
        anime_id = i[0]
        reccomended_animes.append(anime.iloc[i[0]].title)
    return reccomended_animes

anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Anime Advisor')

current_anime = st.selectbox('What Anime are you currently watching?', anime['title'].values)

if st.button('Recommend anime✨'):
    reccomendations = rec_anime(current_anime)
    for i in reccomendations:
        # st.write(i)
        recc_titles = []
        recc_posters = []
        for index in range(len(titles)):
            # if titles[index] == i:
            #     st.image(image_urls[index],width=200,caption=st.write(i))
            if titles[index] == i:
                recc_posters.append(image_urls[index])
                recc_titles.append(titles[index])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header(recc_titles[0])
            st.image(recc_posters[0])
