import joblib
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import heapq

cwd = os.getcwd()

MODEL = joblib.load(f"{cwd}/model.joblib")
DATA = pd.read_csv(f"{cwd}/movie_dataset.csv")




def generate_top_10_values(id,model,data):
	predictions = []
	movies = []
	for index,val in enumerate(model[id]):
		predictions.append((index,val))

	vals = heapq.nlargest(20,predictions,key= lambda x: x[1])

	title = {data.loc[id].title}

	for i in range(1,20):
		movies.append(data.loc[vals[i][0]].title)

	return movies,title




def get_id(data,name_of_movie):
	datas = data.loc[data['title'].str.lower().str.contains(name_of_movie)]
	return list(datas.index)





