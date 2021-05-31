# -*- coding: utf-8 -*-
"""movie_pred_notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fvk9pBHWKfT0yqLKpIbuJbGX8QmzXpL5
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("/content/movie_dataset.csv")
df = df.fillna("")

df.head()

def combine_data(df):
    return f"{df['title']} {df['genres']} {df['director']} {df['keywords']}"

df['Combined'] = df.apply(combine_data,axis=1)

vectorizer = CountVectorizer().fit_transform(df['Combined'])

cosine_similarity(vectorizer)[0]

max = 0
index = 0
preds = []
for i , val in enumerate(cosine_similarity(vectorizer)[80]):
  preds.append((i,val))
  
preds.sort(key = lambda x: x[1], reverse=True)

print(preds[0:10])

print(f"Title name {df.loc[80].title}")
for i in range(0,10):
  if i == 0:
    continue
  else:
    print(f"{i}. {df.loc[preds[i][0]].title}")

def get_results(search_query):
  return df.loc[df['title'].str.lower().str.contains(search_query)]

dfx = get_id("jurassic park")
print(dfx)

def generate_predictions(model,df,main_df):
  as_list = list(df['index'])
  for j in as_list:
    preds = []
    for index, val in enumerate(model[j]):
      preds.append((index,val))
    
    preds.sort(key= lambda x : x[1], reverse=True)
    print(f"Title name {main_df.loc[j].title}")
    for k in range(0,10):
      if k == 0:
        continue
      else:
        print(f"{k}. {main_df.loc[preds[k][0]].title}")

generate_predictions(dfx,df)

df.loc[94]

import pickle
import sys
model = cosine_similarity(vectorizer)
pickle.dump(model,open("model.sav",'wb'))

imported_model = pickle.load(open("model.sav",'rb'))
print(sys.getsizeof(imported_model))
dfi = get_id("hobbit")
generate_predictions(imported_model,dfi,df)
