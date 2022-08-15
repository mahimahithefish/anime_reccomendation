# Anime Recommendation System (Anime Advisor)

This web app reccomends user with top 3 animes based on what they are currently watching. This reccomender system is based on the content-based filtering system where it attempts to guess what a user may like based on that user's activity. This type of filtering makes recommendations by using keywords and attributes assigned to objects in a database.

## Data Processing 
Before cleaning the data, we removed rows that contained empty or duplicated fields. After this step, we had approximately 15,000 animes. 
### Generating Tags
In the dataset the following attributes were used to create tags for each anime: synoposis, genre. These two attributes were then concatenated and cleaned. 
### Data Cleaning 
In the data cleaning stage, we have converted all the tags into lower case letters. Stopwords were removed using the Python Gensim library. Punctutation marks and numbers were retained. 
### Stemming
All the tags undergone stemming. Stemming is used to simplify each word in a sentece to its common base form without taking account of the context of the words with in the sentence. We used PorterStemmer from the nltk library to complete this. Porterstemer uses the Porter's algorithm which has list of 5 rules, that are applied sequentially to reduce the words to its base form.

## Data Modeling 

### Vecorization 
We converted the tags into TF-IDF matrices. TF-IDF stands for term frequency-inverse document frequency and it is a measure that can quantify the importance of string representations in a document. This was done by using the sklearn library.

### Cosine Similarity 
Each of the anime tag vectors were compared to other anime vector tags. Proceeded to calculate the cosine distance using the Sklearn library. The distance between vectors is an inverse relationship, where the increase in distance correspond to less similarity. For each anime, the list of distances between other anime tag vectors were ordered in descending order. We selected the first three values which corresponded to the top 3 reccomended anime. 

## UI 
The Web app was created using the python streamlit library. This allowes for user to type or select an anime that they are currently watching and will generate top 3 similar animes. The poster images were provided in the dataset.

<p align="center">
  <img width="400" height="600" src="https://github.com/mahimahithefish/anime_reccomendation/blob/main/images/Screen%20Shot%202022-08-14%20at%203.00.41%20PM.png" >
</p>

## Libraries 
- NumPy
- Pandas
- Re
- NLTK
- Gensim
- sklearn
- StreamLit
- Pickle

## Resources
- [Anime dataset w/ MyAnimeList Reviews](https://www.kaggle.com/datasets/marlesson/myanimelist-dataset-animes-profiles-reviews)
- [CampusX reccomender system](https://www.youtube.com/watch?v=1xtrIEwY_zY)

