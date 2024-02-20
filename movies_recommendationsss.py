
import numpy as np
import pandas as pd
import ast
import nltk
import sklearn


movies = pd.read_csv('/content/tmdb_5000_movies.csv')  # reading data frames from csv file

credit= pd.read_csv('/content/tmdb_5000_credits.csv')  # reading data frames from csv filer

movies.head(1) # showing data frames

credit.head(1) # simjilar showing data frames

movies = movies.merge(credit,on ='title')

movies.head(1)

# what coloums we have to keep  lets make a list
#genres
#id
#keywords
#title
#overview
#cast
#crew
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

movies.head()

movies.isnull().sum()

movies.dropna(inplace=True)

movies.duplicated().sum()

movies.iloc[0].genres

#[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]
# i want above data in following manner
#['action',adventure','fantasy', ets]
# so i will create an helper function which weill tajkeout the name data

def convert(obj):
  L=[]
  for i in ast.literal_eval(obj):
    L.append(i['name'])
  return L

movies['genres']=movies['genres'].apply(convert)

movies.head()

movies['keywords']=movies['keywords'].apply(convert) #similary for keywords we use function and just keep after name

movies.head()

def convert3(obj): # we are making this function to take name of atleast 3 cast members
  L=[]
  counter =0
  for i in ast.literal_eval(obj):
    if counter != 3:
      L.append(i['name'])
      counter+=1
    else :
      break

  return L

movies['cast']=movies['cast'].apply(convert3)

movies.head()

movies['crew'][0]

def fetch_director(obj): #this function will takout the director names from crew content
  L=[]
  for i in ast.literal_eval(obj):
      if i['job']=='Director':
        L.append(i['name'])
        break
  return L

movies['crew']=movies['crew'].apply(fetch_director)

movies.head()

# now everything is convert in list so we can compare with data sets , now only  overwie is remaning so---
#--- we have to convert it  into list with following function
# lambda is special function to convert it into split
movies['overview'].apply(lambda x :x.split())

movies['overview']=movies['overview'].apply(lambda x :x.split())

movies.head()

# now our next step will be takeouting space oin lists of keywords ,cast ,crew, .... for exmaple cast is Sam worghitnon so recommendation system will -
#---two tags which will be sam and warghinton , so if any other one name is sam and last name is differnt so it will confuse in those two tags--
# hence we will remove space from this words so our recommendation will work better
#so there is function of lambda which will remove the space

movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])

movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies.head()

movies['tags']= movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']

movies.head()

new_df = movies[['movie_id','title','tags']]

new_df['tags']=new_df['tags'].apply(lambda x: " ".join(x))

new_df.head()

import nltk

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
  y=[]
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)

new_df['tags']=new_df['tags'].apply(stem)

#here we convert tags into a string where we added everything overview,keywords,cast,crew
new_df['tags'][0]

new_df['tags']=new_df['tags'].apply(lambda x:x.lower())

new_df.head()

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')

cv.fit_transform(new_df['tags']).toarray()

vectors=cv.fit_transform(new_df['tags']).toarray()

cv.get_feature_names_out()

ps.stem('loving')

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]

def recommend(movie):
  movie_index=new_df[new_df['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  for i in movies_list:
    print(new_df.iloc[i[0]].title)
    print()

recommend('Batman Begins')

import pickle

pickle.dump(new_df,open('movies.pkl','wb'))

new_df['title'].values

pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))

pickle.dump(similarity,open('similarity.pkl','wb'))

