__author__ = "JC, Udacity"
__credits__ = ["JC, Udacity"]
__license__ = "GPL"
__version__ = "1.0"

import media
import fresh_tomatoes

""" data structure to store your favorite movies, including movie title, box art URL and a YouTube link to the movie trailer. """

#Creatting Movie instances of my favorite movies.

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

about_time = media.Movie("About Time" ,
                         "Tim discovers he can travel in time and change" +
                         " what happens and has happened in his own life.",
                         "http://www.impawards.com/intl/uk/2013/posters/about_time.jpg",
                         "https://www.youtube.com/watch?v=T7A810duHvw")


straight_outta_compton = media.Movie("Straight Outta Compton",
                                     "The group NWA emerges from the mean"+
                                     " streets of Compton in Los Angeles, California.",
                                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA5MzkyMzIxNjJeQTJeQWpwZ15BbWU4MDU0MDk0OTUx._V1_.jpg",
                                     "https://www.youtube.com/watch?v=rsbWEF1Sju0")

get_out = media.Movie("Get Out",
                      "It's time for a young African American to meet with his"+
                      " white girlfriend's parents for a weekend.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNTE2Nzg1NjkzNV5BMl5BanBnXkFtZTgwOTgyODMyMTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")
                      

talladega_nights = media.Movie("Talladega Nights",
                                "#1 NASCAR driver Ricky Bobby stays atop the heap"+
                                " thanks to a pact with his best friend and teammate,"+
                                " Cal Naughton, Jr.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BNzAzOTk1OTIyM15BMl5BanBnXkFtZTcwNDIzNTQzMQ@@._V1_SY1000_SX673_AL_.jpg",
                                "https://www.youtube.com/watch?v=-zPcMma_C7A")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt"+
                           " to ensure humanity's survival.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ")
						   
						   
movies = [avatar, about_time, straight_outta_compton, get_out, talladega_nights, interstellar]


fresh_tomatoes.open_movies_page(movies)   #Display the set of movies on the website.
