import pyttsx3
import time
import pandas as pd
from tabulate import tabulate

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)

# Function to get user's choice
def get_choice(prompt):
    engine.say(prompt)
    engine.runAndWait()
    choice = input(prompt)
    return choice

# Function to display options and get user's choice
def display_options(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choice = get_choice("\nEnter your choice here: ")
    time.sleep(0.1)
    return choice

# Welcome message
print("\nWelcome to the IMDB Scraper!")
engine.say("Welcome to the IMDB Scraper!")
print("Today is a pleasant day to watch movies!\n")
engine.say("Today is a pleasant day to watch movies! Here are some options for you:")

# Display sorting options
options = [
    "By Genre",
    "List of Top movies of all time",
    "List of Top Box Office movies this weekend",
    "List of Most popular movies of all time",
    "Would you like to go into the Indian movie database?",
    "See your watchlist\n"
]

# Get user's choice
choice = display_options(options)

# Handle user's choice
if choice == '1':
    import new_sim
elif choice == '2':
    import Topmovies
elif choice == '3':
    import Topboxoffice
elif choice == '4':
    import Popularmovie
elif choice == '5':
    import Indianmovie

elif choice == '6':
    with open('watchlist.txt') as f:
        datafile = f.readlines()
        dict = {"Movie Name": datafile}
        df = pd.DataFrame(dict)
        print(tabulate(df, headers='keys', tablefmt='psql'))
        engine.say("Here is your watchlist")
        print("\nThank you for using the IMDB scraper! ")
        engine.say("Thank you for using the IMDB scraper! Have a nice day! see you soon!")
        engine.runAndWait()
        exit(1)
 
    

# Prompt for movie details
b = get_choice("Do you want to see the details for any movie? (Press 1 for yes, 0 for no): ")
time.sleep(1)
if b == '1':
    import movie_search_main
    print("\nDo you want to add the movie in your watchlist?")
    print("Press 1 for yes and 0 for no")
    engine.say("Do you want to add the movie in your watchlist?")
    engine.say("Press 1 for yes and 0 for no")
    engine.say("Enter your choice here: ")
    engine.runAndWait()
    c=int(input("Enter your choice here: "))
    if c==1:
        def check():
            with open('watchlist.txt') as f:
                datafile = f.readlines()
            for line in datafile:
                if movie_search_main.name in line:
            # found = True # Not necessary
                    return True
            return False  
        fptr=open("watchlist.txt","a")
        if (check()==False):
            fptr.write(movie_search_main.name + "\n")
        else:
            print("Movie already exists in watchlist")
            engine.say("Movie already exists in watchlist")
            engine.runAndWait()
        fptr.close()


print("\nThank you for using the IMDB scraper! ")
engine.say("Thank you for using the IMDB scraper! Have a nice day! see you soon!")
engine.runAndWait()
