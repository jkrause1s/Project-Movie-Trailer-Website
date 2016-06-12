import json
import urllib2
import webbrowser
                          
#Class that will pull all movie details based on title
#Uses The Movie Database(TMDb) API to pull movie details found at https://themoviedb.org

class Movie():
    api_key = "?api_key=739e431e725c6c73ac6705ca9764a173"  #get an API key from TMDb
    url = "https://api.themoviedb.org/3/"  #common URL for all API calls
    poster_link = "https://image.tmdb.org/t/p/original/"
    
    def __init__(self, movie_title):  #Only requirement to create an instance of movie is the movie title
        self.movie_title = movie_title
        self.movie_id = self.get_movie_id()  #loads API and sets id as attribute
        self.movie_details = self.load_movie_info()  #stores full movie details
        self.title = self.movie_details['title']  #searches detail for movie title
        self.trailer_url = self.get_trailer()  #gets youtube URL for movie trailer
        self.poster_url = Movie.poster_link + self.movie_details['poster_path']  #gets movie poster url from dict
        self.storyline = self.movie_details['overview']  #pulls storyline from dict
        self.release_date = self.fix_date(self.movie_details['release_date'])  #pulls release date from dict
        
    def get_movie_id(self):  #Uses the movie_title to query TMDb API
        obj = urllib2.urlopen(Movie.url+"search/movie" + Movie.api_key + "&query="
                              + self.movie_title)  # Uses movie_title to search Db
        data = json.load(obj)  #loads movie dictionary from API
        movie_id = str(data['results'][0]['id'])  #Pulls movie id from dict
        return movie_id  #Movie_id is necessary to get most info
    
    def load_movie_info(self):  #won't work to get trailer due to API
        #pull full detail dictionary for specific movie ID
        get_info = urllib2.urlopen(Movie.url + "movie/" +
                                   self.movie_id + Movie.api_key)
        detail = json.load(get_info)
        return detail
    
    def get_trailer(self):
        info = urllib2.urlopen(Movie.url + "movie/" + self.movie_id + "/videos" + Movie.api_key)
        youtube = "https://www.youtube.com/watch?v="
        detail = json.load(info)
        return youtube + str(detail['results'][0]['key'])

    #take date argument year-month-day to return Month Year
    def fix_date(self, date):
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November",
                  "December"]
        date = str(date)
        first = date.find('-')
        second = date[first + 1:].find('-')
        month_num = int(date[first+1: first+1+second])
        month = months[month_num -1]
        year = date[:first]
        return month + " " + year

    #shortens storyline of movie to 125 characters. Too long distorts title container
    def shorten_story(self, storyline):
        return storyline[:124]+"..."
               
        
    def show_trailer(self):
        webbrowser.open(self.get_trailer())
        
