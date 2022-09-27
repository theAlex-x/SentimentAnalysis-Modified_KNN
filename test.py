# Example of getting neighbors for an instance
from math import sqrt
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import euclidean_distances

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    return euclidean_distances(row1,row2)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = []
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = []
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Test distance function
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

df = pd.read_csv('output/Clean_text_Sentiment.csv')
X = df['text']
y = df['Sentiment']

enc = LabelEncoder()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tf = TfidfVectorizer()
X_train = tf.fit_transform(X_train)
X_test = tf.transform(X_test)
y_train = enc.fit_transform(y_train)

#neighbors = get_neighbors(dataset, dataset[0], 3)
#for neighbor in neighbors:
	#print(neighbor)

neighbors = get_neighbors(X_train, X_test[0], 3)
ts = 0
for neighbor in neighbors:
    ts += neighbor

print(ts)