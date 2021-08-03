#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from os import path
import numpy as np

name_title_processed_path='../../data/imbd_data/name_title_processed.csv'
degree_df_path = '../../data/imbd_data/network_degree_data.csv'
name_title_degree = '../../data/imbd_data/name_title_degree_data.csv'



def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df



def write_to_csv(df,filepath):
    '''
    input: df - a pandas DataFrame
           filepath - an output filepath as a string

    writes to a csv file
    in same diretory as this script

    returns: nothing
    '''
    # if no csv exists
    if not path.exists(filepath):
        df.to_csv(filepath,index=False)
    else:
        df.to_csv(filepath, mode='a', header=False,index=False)



# load data
people_df = load_dataset(name_title_processed_path)
degree_df = load_dataset(degree_df_path)



print(people_df.head())
print(degree_df.head())



# merge names with title dataframe
df = pd.merge(people_df, degree_df, how='left', left_on=['nconst','film_year'], right_on = ['nconst','year'])





write_to_csv(df,name_title_degree)
