# This script has only been ran once as a means to clean the disease-list dataset 
# and output it for use in scraper.py

import pandas as pd
import string
import numpy as np
import re

def clean_string(s):
    ''' clean's string which involves lower-casing, removing spaces, punc '''
    
    clean_s = s.lower().replace(" ", "")
    clean_s = clean_s.translate(str.maketrans('', '', string.punctuation))
    return clean_s


def clean_df(import_path, export_path):
    
    ''' function that cleans the disease-list-raw dataset in /data/disease-list-raw
    and outputs a cleaned version with no duplicates, spacing and punctuation'''

    disease_list = pd.read_csv(import_path)

    #drop duplicates
    df_clean = disease_list.drop_duplicates()

    #cast as string, lower-casing, removing spaces, punc
    df_clean['disease'] = df_clean['disease'].astype('string')
    df_clean['disease'] = df_clean['disease'].apply(lambda x: clean_string(x))

    df_clean.to_csv(export_path, index=True)

    return None
