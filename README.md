# Anime Recommendation System (Anime Advisor)

This web app reccomends user with top 3 animes based on what they are currently watching. This reccomender system is based on the content-based filtering system where it attempts to guess what a user may like based on that user's activity. This type of filtering makes recommendations by using keywords and attributes assigned to objects in a database.

## Data Processing 
Before cleaning the data we removed rows that contained empty or duplicated fields. After this step, we had approximately 15,000 animes. 
### Generating Tags
In the dataset the following attributes were used to create tags for each anime: synoposis, genre. These two attributes were concatenated and cleaned. 
### Data Cleaning 
In the data cleaning stage, we have coverted all the thags into lower case letters. Stopwords were removed using the Python Gensim library. Punctutation marks and numbers we retained. 
### Stemming
All the tags undergone stemming. Stemming is used to simplify each word in a sentece to its common base form without taking account of the context of the words with in the sentence. We used PorterStemmer from the nltk library to complete this. Porterstemer uses the Porter's algorithm which has list of 5 rules, that are applied sequentially to reduce the words to its base form.

## Data Modeling 

### Vecorization 

### Cosine Similarity 

## UI 
The Web app was created using the python stramlit library. This allowes for user to type or select an anime that they are currently watching and will generate top 3 similar animes. 

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

