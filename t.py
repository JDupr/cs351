import pandas as pd

df = pd.read_csv("full_data.tsv",sep='\t')
df.head()

def get_important_features(data):
    columns = ['primaryTitle','primaryName']
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
    df = pd.read_csv("full_data.tsv",sep='\t')
    df.head()

    unsortedList=get_important_features(df)

    sorted_list = sorted(unsortedList, key=lambda x:x[1])
    #for i in sorted_list:
    #    print(i)

    file1 = open("edges.txt","a")
    l = len(sorted_list)
    index=1
    for entry in sorted_list:
        movie = entry[0]
        director = entry[1]
        for index in range(0,l):
            if(index < l and director == sorted_list[index][1] and movie != sorted_list[index][0]):
                file1.write(movie+'%'+sorted_list[index][0]+'\n')

            #print(movie+','+sorted_list[index][0])

    file1.close()

