import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Create function to combine the values of important columns into a single string to be added to a list
def get_important_features(data):
	columns = ['genres', 'year']
	important_features = []
	append_string = ''
	for i in range(0, data.shape[0]):
		append_string = ''
		for col in columns:
			append_string += f'{data[col][i]} '
		important_features.append(append_string)

	return important_features


def print_recommendations(matrix, row_id, type):
	# Create a list of enumerations for the similarity score
	scores = list(enumerate(matrix[row_id]))
	sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
	sorted_scores = sorted_scores[1:]

	print(f'Top 10 Recommendations ({type}): ')
	for count, item in enumerate(sorted_scores):
		if count == 10:
			break
		else:
			movie_title = df[df.row == item[0]]['title'].values[0]
			print(f'{count + 1}: {movie_title}')
	print('\n')


if __name__ == "__main__":

	# Read data
	df = pd.read_csv('movies.csv')

	# Create new column with important feature column
	df['important_features'] = get_important_features(df)

	# Get enumerated column for row number
	df['row'] = np.arange(len(df))

	# Convert the text into a matrix of token counts
	cm = CountVectorizer().fit_transform(df['important_features'])

	# Get simularity matrixes
	ed = euclidean_distances(cm)
	cs = cosine_similarity(cm)
	sm = ed + cs

	# Ask user for title
	title = input('Enter in a title: ')

	# Find this movie's ID
	row_id = df[df.title == title]['row'].values[0]

	print_recommendations(ed, row_id, 'Cosine')
	print_recommendations(cs, row_id, 'Euclidean')
	print_recommendations(sm, row_id, 'Hybrid')
