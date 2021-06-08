import pandas as pd
import numpy as np
from justwatch import JustWatch as jw
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Create function to combine the values of important columns into a single string to be added to a list
def get_important_features(data):
	columns = ['genres', 'startYear', 'primaryName']
	important_features = []
	append_string = ''
	for i in range(0, data.shape[0]):
		append_string = ''
		for col in columns:
			if not (data[col][i] == 'nan' or data[col][i] == '\\N'):
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
			movie_title = df[df.row == item[0]]['primaryTitle'].values[0]
			print(f'{count + 1}: {movie_title}')
	print('\n')


if __name__ == "__main__":

	just_watch = jw(country='US')

	results = just_watch.search_for_item(query='the matrix')

	print(results['items'])
	exit()


	# Read data
	tsv_basic = pd.read_csv('main_data.tsv', sep='\t', usecols=['tconst', 'titleType', 'primaryTitle', 'startYear', 'genres'])
	tsv_crew = pd.read_csv('data_1.tsv', sep='\t', usecols=['tconst', 'directors'])
	#tsv_principals = pd.read_csv('data_2.tsv', sep='\t', usecols=['tconst', 'titleType', 'primaryTitle', 'startYear', 'genres'])
	tsv_names = pd.read_csv('data_3.tsv', sep='\t', usecols=['nconst', 'primaryName'])

	df = tsv_basic[tsv_basic['titleType'] == 'tvSeries'].reset_index()
	tsv_crew['directors'] = tsv_crew['directors'].str.split(',').str[0]
	tsv_crew = tsv_crew.join(tsv_names.set_index('nconst'), on='directors')
	df = df.join(tsv_crew.set_index('tconst'), on='tconst')
	df = df[df['directors'] != '\\N']

	print(df.head())
	df[df.shape[0]-1000:].to_csv('full_data.tsv', sep='\t')



	## Create new column with important feature column
	#df['important_features'] = get_important_features(df)

	## Get enumerated column for row number
	#df['row'] = np.arange(len(df))
	#df.set_index('row')

	## Convert the text into a matrix of token counts
	#cm = CountVectorizer().fit_transform(df['important_features'][:10000])

	## Get simularity matrixes
	#ed = euclidean_distances(cm)
	#cs = cosine_similarity(cm)

	## Ask user for title
	#title = input('Enter in a title: ')

	## Find this movie's ID
	#row_id = df[df.primaryTitle == title]['row'].values[0]

	#print_recommendations(ed, row_id, 'Euclidean')
	#print_recommendations(cs, row_id, 'Cosine')
	##print_recommendations(sm, row_id, 'Hybrid')
