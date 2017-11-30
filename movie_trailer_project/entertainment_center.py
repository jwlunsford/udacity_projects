import fresh_tomatoes
from media import Movie


#  Movie Class Instances
big_lebowski = Movie(
    "The Big Lebowski",
    "A movie about a middle aged slacker who is a victim of " 
    "all sorts of mishaps and random adventures.",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")


empire_strikes_back = Movie(
    "The Empire Strikes Back",
    "A movie about good versus evil in a galaxy " 
    "far, far away.",
    "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
    "https://www.youtube.com/watch?v=96v4XraJEPI")
                                
office_space = Movie(
    "Office Space",
    "An unmotivated office employee lives care free after " 
    "he is hypnotized.",
    "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
    "https://www.youtube.com/watch?v=dMIrlP61Z9s")   
                    
jason_bourne = Movie(
    "Jason Bourne",
    "An ex-CIA assassin searches for information about his "
    "past life.",
    "https://upload.wikimedia.org/wikipedia/en/b/b2/Jason_Bourne_%28film%29.jpg",
    "https://www.youtube.com/watch?v=F4gJsKZvqE4")
                    
the_internship = Movie(
    "The Internship",
    "Two middle-aged men compete for an intern position "
    "at Google after being fired from their jobs.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",
    "https://www.youtube.com/watch?v=cdnoqCViqUo")
                        
the_breakfast_club = Movie(
    "The Breakfast Club",
    "Five high school students with nothing in common "
    "spend a Saturday in detention.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/The_Breakfast_Club.jpg",
    "https://www.youtube.com/watch?v=BSXBvor47Zs")
                            
# create a list of the movie classes to be sent as an argument
# to the open_movies_page function.
                        
movies_list = [big_lebowski, empire_strikes_back, office_space, 
              jason_bourne, the_internship, the_breakfast_club]
              
fresh_tomatoes.open_movies_page(movies_list)


