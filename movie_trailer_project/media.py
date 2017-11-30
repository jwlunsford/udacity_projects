import webbrowser


class Movie:
    '''movie class represents a Movie object.
    arguments::
          movie_title:       the movie's title (string)
          movie_storyline:   a short summary of the movie (string)
          poster_image:      url for the poster image on Wikipedia
          trailer_youtube:   url for the trailer on Youtube'''    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        '''method to diplay the trailer using the url
           found in the trailer_youtube attribute.'''        
        webbrowser.open(self.trailer_youtube_url) 
    
    