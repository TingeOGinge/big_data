import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

#Reading users file:
u_cols = ['user_id','age','sex','occupation','zip_code']
users = pd.read_csv('../../datasets/movie-lens/ml-100k/u.user', sep='|',names=u_cols,encoding='latin-1')
#Reading ratings file:
r_cols = ['user_id','movie_id','rating','unix_timestamp']
ratings = pd.read_csv('../../datasets/movie-lens/ml-100k/u.data',sep='\t',names=r_cols,encoding='latin-1')
#Reading items file:
i_cols = ['movie id','movie title','release date','video  release date','IMDb URL','unknown',
         'Action','Adventure','Animation','Children\'s','Comedy','Crime','Documentary','Drama',
         'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller', 'War','Western']
items = pd.read_csv('../../datasets/movie-lens/ml-100k/u.item',sep='|',names=i_cols,encoding='latin-1')
print(users.shape)
print(users.head())
print(ratings.shape)
print(ratings.head())
print(items.shape)
print(items.head())
#r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
#ratings_train = pd.read_csv('ml-100k/ua.base',sep='\t',names=r_cols,encoding='latin-1')
#ratings_test = pd.read_csv('ml-100k/ua.test',sep='\t',names=r_cols,encoding='latin-1')
#print(ratings_train.shape)
#print(ratings_test.shape)
n_users = ratings.user_id.unique().shape[0]
n_items = ratings.movie_id.unique().shape[0]
#the number of users and items/movies
data_matrix = np.zeros((n_users, n_items))
for line in ratings.itertuples():
    data_matrix[line[1]-1,line[2]-1] = line[3]
item_similarity = pairwise_distances(np.transpose(data_matrix), metric='cosine')
#calculate the item-item similarity, first transpose the matrix
print(item_similarity.shape)
#Now we have the similarity of the 1682 items
#please note here we only use the ratings as the attribute
#in a content based recommendation, it is expected that you
#define the attributes properly to represent the items
#for coursework, you need more than the ratings to measure the similarity
#don't just copy the codes here, but you can use most of them directly
#for your recommender system
def recommend_ratings_similar5(similarityMatrix,itemInd,labels):
    #item id from 0 to total_number-1
    array1d = similarityMatrix[itemInd,:]
    indices = array1d.argsort()[-5:]
    indices = indices[::-1]
    #the most similar 5
    print(array1d[indices])
    return labels[indices]

print(items.iloc[0]['movie title'])
print(recommend_ratings_similar5(item_similarity,0,items['movie title']))
print(items.iloc[999]['movie title'])
print(recommend_ratings_similar5(item_similarity,999,items['movie title']))
#the recommendation is not that good, right?
#check the reason yourself and let me know it should you need further help