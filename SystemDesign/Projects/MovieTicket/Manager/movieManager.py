class MovieManager:
    def __init__ (self):
        self.user = None
        self.selected_movies = []
    def add_movies(self,movie):
        self.selected_movies.append(movie)

    def get_selectedMovies(self):
        return self.selected_movies
    def get_user(self):
        return self.user
