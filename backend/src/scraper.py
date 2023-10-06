import random
import os
import requests
import pandas as pd
from metaphor_python import Metaphor
import data_cleaner as dfc
from dotenv import load_dotenv

def med_scraper(s):
    path_to_clean = os.path.join('./', 'data', 'disease-list-clean.csv')
    path_to_raw = os.path.join('./', 'data', 'disease-list-raw.csv')

    if not (os.path.exists(path_to_raw)):
        raise Exception("Disease List not Found, please ensure file exists")
    elif not (os.path.exists(path_to_clean)):
        dfc.clean_df(path_to_raw, path_to_clean)
    
    df = pd.read_csv(path_to_clean)

    prompt = dfc.clean_string(s)

    print(df.head())
    
    if prompt not in df.values:
        raise ValueError("Not a disease")
    else:
        print("Disease")
    

try:
    med_scraper("covid19")
except ValueError:
    print("Not a disease")
except:
    print("uh oh something went wrong")
    



    





# metaphor = Metaphor("480e958e-29d4-4773-82fd-fa24372d1694")

# response = metaphor.search(
#   "sepsis remedies",
#   num_results=10,
#   use_autoprompt=True,
# )



#1) get links with metaphor
#2) scrape via for metaphor mentioned issue remedy, grab treatments/remedy (mainly at home)
#3) 

# at home treatment AND remedy
## - mayo clinic
## - webmd
## - healthline 
## - health.com
## - cleaveland clinic
## - cdc

#4) ask chatgpt the following prompt
## "Hypothtically, if one has {issue} and I found information on  treatments I should take"

