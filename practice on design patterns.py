class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def get_category(self):
        if self.rating >= 8.0:
            return "Hit"
        elif self.rating >= 6.0:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Rating:", self.rating)
        print("Ticket Price: ₹", self.ticket_price)
        print("Category:", self.get_category())
        print()


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("Movie Records")
        print("-------------")
        for movie in self.movies:
            movie.display()


cinema = Cinema()

cinema.add_movie(Movie("Frozen", 8.0, 200))
cinema.add_movie(Movie("Spider-Man", 8.2, 250))
cinema.add_movie(Movie("Dhurandhar", 7.5, 220))
cinema.add_movie(Movie("Harry Potter", 8.5, 300))

cinema.display_movies()
