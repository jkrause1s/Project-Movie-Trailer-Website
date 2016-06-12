import fresh_tomatoes
import media

#Create instances of movies to go on webpage 
catch_me_if_you_can = media.Movie("Catch+Me+If+you+can") #Must use + in place of spaces

inception = media.Movie("Inception")

da_vinci_code = media.Movie("Da+Vinci+Code")

the_social_network = media.Movie("The+Social+Network")

return_of_the_jedi = media.Movie("The+Return+of+the+Jedi")

spinal_tap = media.Movie("This+is+Spinal+Tap")

dirty_harry = media.Movie("dirty+harry")

anchorman = media.Movie("anchorman")

lord_of_the_rings = media.Movie("fellowship+of+the+ring")

#create list of movie instances to pass through for page creation
movies = [catch_me_if_you_can, inception, da_vinci_code,
          the_social_network, return_of_the_jedi, spinal_tap,
          dirty_harry, anchorman, lord_of_the_rings]

#Call function to pass movies in as arguement to create page

fresh_tomatoes.open_movies_page(movies)
