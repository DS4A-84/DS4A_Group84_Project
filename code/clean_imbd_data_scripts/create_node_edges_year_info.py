#!/usr/bin/python

# DS4A Project
# Group 84
# Here we use the clean oracle of bacon dataset that only includes info
# on the nominees from the kaggle dataset


from os import path
import pandas as pd
import time


name_title_processed_path = '../../data/imbd_data/name_title_processed.csv'
nodes_df_path = '../../data/imbd_data/nodes.csv'
edges_df_path = '../../data/imbd_data/edges.csv'




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


def create_edges_csv(df,filepath,year):
    '''
    Inputs: df - pandas dataframe
            filepath - python string

    this will take the nominees per film title
    and create link between every nominee in that movie
    saves output as dataframe with columns source target
    and year info. Write the output per year to edge folder

    Returns: nothing
    '''

    films = df['tconst'].unique()
    

    # get actors per film
    for film in films:
        people = df[df['tconst'] == film]['nconst']
        people = people.reset_index(drop=True)
        # only include films with more than one nominees in it
        if len(people) != 1:
            for i in range(0, len(people)):
                for j in range(i+1, len(people)):
                    pairs = [[people[i], people[j], year]]
                    df1 = pd.DataFrame(pairs, columns = ['source', 'target','year'])
                    write_to_csv(df1, filepath)


def create_nodes_csv(df, filepath):
    '''
    takes a pandas dataframe
    and extracts names
    uses filepath to write output
    '''
    df = df[['nconst','film_year']].drop_duplicates()
    write_to_csv(df,filepath)





# MAIN
df = load_dataset(name_title_processed_path)

time_start= time.time()


# create edges
for year in range(min(df.film_year),max(df.film_year)+1):
    
    year_sub_df = df[df.film_year == year]
    # create edges
    create_edges_csv(year_sub_df,edges_df_path,year)


#the nominees film info
create_nodes_csv(df,nodes_df_path)

time_end = time. time()
print(time_end - time_start)

