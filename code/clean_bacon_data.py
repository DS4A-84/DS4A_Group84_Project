#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data to convert to dataframe



# Import Python Modules
from functools import reduce
import json
from os import path
import pandas as pd




# Data
bacon_data_path = 'data/bacon.txt'
clean_bacon_df_path = 'data/clean_bacon_df.csv'
kaggle_data_path = 'data/the_oscar_award_corrected.csv'

categories_interest = ['ACTOR',
                       'ACTRESS',
                       'ACTOR IN A LEADING ROLE',
                       'ACTRESS IN A LEADING ROLE',
                       'ACTOR IN A SUPPORTING ROLE',
                       'ACTRESS IN A SUPPORTING ROLE',
                       'DIRECTING',
                       'DIRECTING (Comedy Picture)',
                       'DIRECTING (Dramatic Picture)']


def load_txt_data(filepath):
    '''
    Inputs: filepath - str path to input data

    input data is in a txt file

    returns: output data is a readlines object
             of the text file
    '''

    a = open(filepath, 'r', encoding="utf8")
    return a.readlines()


def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


def blob_to_list(lines):
    '''
    Input: lines - readlines object
           filepath - str of output path

    Takes lines input and formats it to a python dictionary
    only keeps lines that are json blobs

    returns:  list of dictionaries formatted strings
    '''

    dict = {
        "INFOBOX: ":"",
        "=>":":",
        "[[": "",
        "]]":"",
        "\n":""
        }

    result = []
    for i in lines:
        if 'INFOBOX' in i or '{"title' in i :

            #check for directors, year in line
            if 'directors' in i and 'year' in i[-20:]:
                # clean the line
                i = reduce(lambda x, y: x.replace(y, dict[y]), dict, i)
                i = json.loads(i)
                result.append(i)

    return result


def create_info_title_pair_list(list):
    '''
    inputs -  list of strings in dictionary format

    takes in  list
    infobox and title adds sequential
    pairs to output list

    returns: a nested list of correctly sequential
    movie info/title movie dictionaies
    '''

    result = []
    temp = []

    for f in list:

        if len(temp) == 0:
            # check if input is infobox
            if "directors" in next(iter(f)):
                temp.append(f)

        elif len(temp) == 1:
            #check if input is title
            if "title" in next(iter(f)):
                # check if directors match
                if temp[0]['directors'] == f['directors']:
                    temp.append(f)
                    result.append(temp)
            temp = []
    return result


def seq_list_to_nominees_df(list, k_names, filepath):
    '''
    Inputs: list - nested list of sequential info/title
            k_names - pandas series of kaggle nominee names
            filepath - an output filepath as a string

    this takes the info/title nested list and converts
    to pandas dataframe
    writes outpandas dataframe with 4 columns with each row
    being a name and info on the film they participated
    only nominees from kaggle dataset are included in this data

    returns: nothing
    '''


    #break down name values to dataframe
    #what if cast is empty
    for film in list:
        t_df=""
        i,t = film

        # create dataframe from t dictionary
        cast_dir = ""
        if 'cast' in t.keys():
            cast_dir = t['cast']+t['directors']
        else:
            cast_dir = t['directors']
        t_df = pd.DataFrame({'title':[t['title']]*len(cast_dir),
                             'year':[t['year']]*len(cast_dir),
                             'role':['cast']*len(cast_dir),
                             'name':cast_dir
                             })

        # fill in director role
        t_df.loc[t_df['name'].isin(i['directors']),'role'] = "director"

        # fill in star actor role if it exists in i dictionary
        if 'stars' in i.keys():
            t_df.loc[t_df['name'].isin(i['stars']),'role'] = "star"

        # only include row of the dataframe where the names match
        # the kaggle nominee dataset names
        t_df = t_df[t_df['name'].isin(kaggle_names)]
        if len(t_df)!=0:
            write_to_csv(t_df,filepath)

        # check if names in kaggle data exist in this dataframe
        #temp=[]
        #for i in t_df['name']:
        #    if len(k_names[k_names==i])!=0:
        #        temp.append(i)
        #        if len(temp) == 2:
        #            write_to_csv(t_df,filepath)
        #            break

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

# load bacon and kaggle datasets
raw_bacon_data = load_txt_data(bacon_data_path)
kaggle_data = load_dataset(kaggle_data_path)

# prepare kaggle nominee names
kaggle_data = kaggle_data[kaggle_data['category'].isin(categories_interest)]
kaggle_names = kaggle_data['name'].drop_duplicates()


# clean list of info/title string dictionaies
clean_bacon_data = blob_to_list(raw_bacon_data)
#print(len(clean_bacon_data))
#256992
# convert from non sequential info/title list into sequential nested lists
bacon_pair_list = create_info_title_pair_list(clean_bacon_data)
#print(len(bacon_pair_list))
#123409
# create pandas dataframe of movie info for nominees
seq_list_to_nominees_df(bacon_pair_list, kaggle_names,clean_bacon_df_path)
#45964

#Joel Coen is missing for no country for old men
# check get_bacon_conflict_names.py
