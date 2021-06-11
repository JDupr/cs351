from tkinter import *
from imdb import IMDb


ia = IMDb()
root = Tk()
root.geometry("500x700")


# stuff for movie text input
# prints movie text when search button is pressed

searchLabel = Label(root,text="Movie:")
searchLabel.place(x=0,y=2)

movieInput = StringVar(root)
movieText = Text(root, height = 1, width = 50)
movieText.place(x=45,y=5)

print(movieInput.get())
searchResults = Listbox(root,width=40)
searchResultsID = []
def searchButtonPress():
    movieInput.set(movieText.get("1.0","end").replace('\n',''))
    searchIA = ia.search_movie(movieInput.get())
    print(movieInput.get())
    val=1
    for i in searchIA:
        movie1 = ia.get_movie(i.movieID)
        print(movie1['title'], movie1['year'],i.movieID)
        searchResults.insert(val, movie1['title']+" "+ str(movie1['year']))
        searchResultsID.append(i.movieID)
searchButton = Button(root, text="Search",command=searchButtonPress)
searchButton.place(x=405,y=0)


#list of movies found in imdb search using provided input movie
#selected movie currently printed

def searchResultSelected(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        #label.configure(text=data)
        print(data)
        print(searchResultsID[index])
    else:
        #label.configure(text="")
        print("")
#searchResults = Listbox(root,width=40)
'''
searchResults.insert(1, "The Matrix (1999)")
searchResults.insert(2, "The Matrix (2016) (Short)")
searchResults.insert(3, "The Matrix (2004) (Short)")
searchResults.insert(4, "The Matrix Reloaded (2003)")
searchResults.insert(5, "The Matrix Revolutions (2003)")
searchResults.insert(6, "The Matrix Revisited (2001) (Video)")
'''
searchResults.place(x=45,y=30)
searchResults.bind("<<ListboxSelect>>", searchResultSelected)



#radio buttons
reccMovies = Label(root,text="Suggestions:")
reccMovies.place(x=0,y=210)
selection=""
def radioSel():
   #selection = "You selected option " + str(var.get())
   selection = str(var.get()+":")
   radioButtonSelection.config(text = selection)
n=0
var = IntVar()
R1 = Radiobutton(root, text = "The Matrix Reloaded", variable = var, value = 1,
                  command = radioSel)
R1.place(x=45,y=235+n)
n+=30
R2 = Radiobutton(root, text = "The Matrix Revolutions", variable = var, value = 2,
                  command = radioSel)
R2.place(x=45,y=235+n)
n+=30
R3 = Radiobutton(root, text = "The Matrix Revisited", variable = var, value = 3,
                  command = radioSel)
R3.place(x=45,y=235+n)
n+=30
R4 = Radiobutton(root, text = "The Dark Knight", variable = var, value = 4,
                  command = radioSel)
R4.place(x=45,y=235+n)
n+=30
R5 = Radiobutton(root, text = "Inception", variable = var, value = 5,
                  command = radioSel)
R5.place(x=45,y=235+n)
n+=30
R6 = Radiobutton(root, text = "Batman Begins", variable = var, value = 6,
                  command = radioSel)
R6.place(x=45,y=235+n)
n+=30
R7 = Radiobutton(root, text = "The Animatrix", variable = var, value = 7,
                  command = radioSel)
R7.place(x=45,y=235+n)
n+=30
R8 = Radiobutton(root, text = "The Lord of the Rings: The Fellowship of the Ring", variable = var, value = 8,
                  command = radioSel)
R8.place(x=45,y=235+n)
n+=30
R9 = Radiobutton(root, text = "The Dark Knight Rises", variable = var, value = 9,
                  command = radioSel)
R9.place(x=45,y=235+n)
n+=30
R10 = Radiobutton(root, text = "Blade Runner", variable = var, value = 10,
                  command = radioSel)
R10.place(x=45,y=235+n)
n+=30

radioButtonSelection = Label(root)
radioButtonSelection.place(x=45,y=535)


#movie description

movieDesc = Text(root, height = 5, width = 50)
movieDesc.insert(INSERT, "A thief who steals corporate secrets through the  use of dream-sharing technology is given the inve-rse task of planting an idea into the mind of a   C.E.O.")
movieDesc.place(x=45,y=565)


root.mainloop()