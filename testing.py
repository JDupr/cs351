from graph import Graph
import pandas as pd


def get_important_features(data):
    columns = ['primaryTitle','tconst','crew','genres']
    important_features = []
    temp = []
    append_string = ''
    for i in range(0, data.shape[0]):
        for col in columns:
            temp.append(data[col][i])
        important_features.append(temp.copy())
        temp.clear()
    return important_features


if __name__ == "__main__":
	# df = pd.read_csv("full_data0.tsv",sep='\t')
	# for X in range(1,10):
		# temp = pd.read_csv(f"full_data{X}.tsv",sep='\t')
		# df = pd.concat([df, temp])
		# print(df.shape)
	# del df['Unnamed: 0']
	# del df['Unnamed: 0.1']
	# df.set_index('index')
	# df.to_csv('full_data.tsv', sep='\t')
	
    graph = Graph()
    df = pd.read_csv("full_data.tsv",sep='\t')

    unsortedList = get_important_features(df)
    sorted_list = sorted(unsortedList, key=lambda x:x[1])

    crew_edges = open("crew_edges.txt","a")
    genre_edges = open("genre_edges.txt","a")

    l = len(sorted_list)
    index = 1
    entry_temp = 1
    for entry in sorted_list:
        movie_name = entry[0]
        movie = entry[1]
        crew = str(entry[2]).split(',')
        genres = entry[3].split(',')
        for index in range(0,l-1):
            if(any(item in crew for item in str(sorted_list[index][2]).split(',')) and movie != sorted_list[index][1]):
                graph.add_edge(movie_name, sorted_list[index][0])
                crew_edges.write(movie_name+'%'+sorted_list[index][0]+'\n')
            elif(genres != ['\\N'] and any(item in genres for item in sorted_list[index][3].split(',')) and movie != sorted_list[index][1]):
                graph.add_edge(movie_name, sorted_list[index][0])
                genre_edges.write(movie_name+'%'+sorted_list[index][0]+'\n')
        print(f'Entry done #{entry_temp}')
        entry_temp += 1

    crew_edges.close()
    genre_edges.close()

    for i in range(100):
        for node in graph.nodes:
            node.update_pagerank(0.15, len(graph.nodes))
        graph.normalize_pagerank()
    arr = graph.get_pagerank_list()
    with open('graph.txt', 'w+') as file:
        file.write(str(arr))

    graph.sort_nodes()
