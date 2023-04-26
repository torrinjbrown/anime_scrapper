

#This is going to be the main code for the user interaction

#Creating a class for grabbing the title, season and rating of the anime
class intro:
    def __intit__(title, season, rating):
        self.title = title
        self.season = season
        self.rating = rating

def welcome():
    ask = input("Hello welcome to the anime reccomendation list, would you like to have a reccomendation? ")
    if ask == "yes":
        print("Welcome") 
              

welcome()           
# if the user say that they want a score of 8 print from anime scrapper


    # Returning the object as a string which will be helpful def __str__(self):
        