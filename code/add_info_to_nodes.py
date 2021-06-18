#!/usr/bin/python

# DS4A Project
# Group 84
# add extra info to nodes



import pandas as pd




bacon_nodes_path = 'data/bacon_nodes.csv'
kaggle_data_path = 'data/the_oscar_award_corrected.csv'



def add_nominee_info_by_key(node_df,info_df,new_key_name,key_col,name_col):
    '''
    Input: node_df - pd df of nodes csv, nominee name column is 'name'
           info_df - additional pd df data to add

    info_df can be any number of columns as long as
    it has the following; a column of nominee names
    each row is a single piece of information about a nominee,
    also there should be a column to use as a key to store this info
    for example

    films             year           name
    fast and furious  2019           Tom Hanks
    007               2020           Tom Hanks
    The Matrix        1999           Gordon Ramsey

    Returns: pandas dataframe of updated nodes
    The_Input:
    data_of_birth    name
    1970             Tom Hanks
    1980             Gordon Ramsey
    The_Result:
    films                                     data_of_birth           name
    {fast and furious:[2007], 007:[2020]}         1970             Tom Hanks
    {The Matrix:[1999]}                           1980           Gordon Ramsey
    '''


    names = node_df['name'].drop_duplicates()
    info_df_cols = info_df.columns


    info_df = info_df[info_df[name_col].isin(names)]

    for i in names:
        df = info_df[info_df[name_col]==i]
        info = [dict(zip(df.title, zip(df.role,df.year)))]
        df1 = pd.DataFrame({'name':nominee,'films':films_info})
        write_to_csv(df1, filepath)



    return node_df



def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


# load nodes
nodes = load_dataset(bacon_nodes_path)

# add kaggle awards data
kaggle_data = load_dataset(kaggle_data_path)
add_nominee_info_by_key(nodes,kaggle_data,"awards","film","name")
