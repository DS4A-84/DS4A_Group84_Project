#!/usr/bin/python

# DS4A Project
# Group 84
# using node/edge info to create network graph
# and do social network analysis

from os import path
import pandas as pd

bacon_graph_data_path = '../data/oracle_of_bacon_data/clean_data/graph_data.csv'
nominee_count_data_path = '../data/nominations_count.csv'
nominee_count_degree_data_path = '../data/nominee_degree_counts_data.csv'


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



degree_df = load_dataset(bacon_graph_data_path)
count_df = load_dataset(nominee_count_data_path)

print(degree_df.info())
print(count_df.info())


df = pd.merge(count_df, degree_df, how='left', left_on=['name','year_film'], right_on = ['name','year'])
print(len(df))

# Count total NaN at each column in a DataFrame
print(" \nCount total NaN at each column in a DataFrame : \n\n",
      df.isnull().sum())
#only 33 missing in degreee and year

df1 = df[df.year.notnull()]
print(len(df1))
print(" \nCount total NaN at each column in a DataFrame : \n\n",
      df1.isna().sum())



null_data = df[df.isnull().any(axis=1)]
print(null_data)

df1.year = df1.year.astype(int)
df1.degree = df1.degree.astype(int)

write_to_csv(df1,nominee_count_degree_data_path)
