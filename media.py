__author__ = "JC, Udacity"
__credits__ = ["JC, Udacity"]
__license__ = "GPL"
__version__ = "1.0"

import webbrowser

class Movie():

    """ Movie class.

    Attributes:
        title = title of the movie.
        storyline = brief explanation of the movies plot.
        poster_image_url = image of the movies poster.
        trailer_youtube_url = video of the movie's trailer.
        show_trailer = plays the movie's trailer based on trailer_youtube_url.

    """

    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
