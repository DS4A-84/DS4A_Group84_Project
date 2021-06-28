#!/usr/bin/python

# DS4A Project
# Group 84
# add extra info to nodes



from os import path
import pandas as pd

kaggle_data_path = '../../data/kaggle_oscar_award_data/the_oscar_award_corrected.csv'


categories_interest = ['ACTOR',
                       'ACTRESS',
                       'ACTOR IN A LEADING ROLE',
                       'ACTRESS IN A LEADING ROLE',
                       'ACTOR IN A SUPPORTING ROLE',
                       'ACTRESS IN A SUPPORTING ROLE',
                       'DIRECTING',
                       'DIRECTING (Comedy Picture)',
                       'DIRECTING (Dramatic Picture)']


def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df

# load bacon and kaggle datasets
kaggle_data = load_dataset(kaggle_data_path)

# Remove whitespace from name
kaggle_data['name'] = kaggle_data['name'].apply(lambda x: x.strip())

# prepare kaggle nominee names
kaggle_data = kaggle_data[kaggle_data['category'].isin(categories_interest)]
