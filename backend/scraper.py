import random
import os
import requests
import openai
import pandas as pd
import re
from metaphor_python import Metaphor
import data_cleaner as dfc
import functools
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {
    "METAPHOR_API_KEY" : os.getenv("METAPHOR_API_KEY"),
    "OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY")
}

re_html = re.compile('<.*?>') 

def remove_html(content):
    cleantext = re.sub(re_html, ' ', content)
    cleantext = re.sub('\n', ' ', cleantext)
    cleantext = re.sub('\t', ' ', cleantext)
    return cleantext


def med_scraper(condition):
    
    path_to_clean = os.path.join('./', 'data', 'disease-list-clean.csv')
    path_to_raw = os.path.join('./', 'data', 'disease-list-raw.csv')



    if not (os.path.exists(path_to_raw)):
        raise Exception("Disease List not Found, please ensure file exists")
    elif not (os.path.exists(path_to_clean)):
        dfc.clean_df(path_to_raw, path_to_clean)
    
    df = pd.read_csv(path_to_clean)

    condition = dfc.clean_string(condition)
    
    if condition not in df.values:
        raise ValueError("Not a disease")
    
    prompt = condition + " home remedies and treatment"
    
    
    metaphor = Metaphor(API_KEYS["METAPHOR_API_KEY"])

    response_meta = metaphor.search(
        prompt,
        num_results=5,
        use_autoprompt=False,
    )

    # print(response)
    response_ids = [result.id for result in response_meta.results]

    response_cont = metaphor.get_contents(response_ids)

    # content_extract = [content.extract for content in contents]
    # print(response_cont.contents)

    response_val = [remove_html(content.extract) for content in response_cont.contents]

    # str_content2 = ""
    # for val in response_val:
    #     print(val)
    #     print("\n\n=====================================================\n\n")
    #     str_content2 = str_content2 + "\n" +val 
    # print(response_val)

    str_content = functools.reduce((lambda s1, s2: s1 + ' \n\n ' + s2), response_val)
    # print(str_content)
    #plug this into chat gpt and ask to summarize this


    #open ai

    openai.api_key = API_KEYS["OPENAI_API_KEY"]

    gpt_init_prompt = f"I have {condition}, using ONLY the article info below (do not type anything else). Give me an overview of {condition}, things I should be aware of and then list the exact remedies it is recommending."
    
    gpt_prompt = gpt_init_prompt + "\n\n" + str_content
    
    response_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content" : gpt_prompt}]
    )

    return response_gpt.choices[0].message.content

    
    



    





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

