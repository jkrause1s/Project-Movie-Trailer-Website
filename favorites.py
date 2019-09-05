import fresh_tomatoes
import media

#Create instances of movies to go on webpage 
 #Must use + in place of spaces
movie_list = ["Catch+Me+If+you+can", "Raiders+of+the+Lost+Ark", "Da+Vinci+Code", "The+Social+Network", 
            "The+Return+of+the+Jedi", "This+is+Spinal+Tap", "dirty+harry","anchorman:", "fellowship+of+the+ring"]

movies = [media.Movie(x) for x in movie_list]

#Call function to pass movies in as arguement to create page

fresh_tomatoes.open_movies_page(movies)
