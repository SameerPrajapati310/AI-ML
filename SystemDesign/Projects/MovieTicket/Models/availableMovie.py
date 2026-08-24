from Models.movie import Movie
class AvailableMovies:
    def __init__ (self):
        self.movies = []
    def add_movies(self,movie):
        print(movie)
        self.movies.append(movie)
    def get_movies(self):
        return self.movies
    def search_movie(self,name):
        for movie in self.movies:
            if name == movie.get_name():
                print(movie.get_name())
                print(movie.get_price())
                return movie