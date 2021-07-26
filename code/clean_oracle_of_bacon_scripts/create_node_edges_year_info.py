#!/usr/bin/python

# DS4A Project
# Group 84
# Here we use the clean oracle of bacon dataset that only includes info
# on the nominees from the kaggle dataset


from os import path
import pandas as pd





clean_bacon_df_path = '../../data/oracle_of_bacon_data/clean_bacon_df.csv'
bacon_edges_path = '../../data/oracle_of_bacon_data/clean_data/edges_year.csv'
bacon_nodes_path = '../../data/oracle_of_bacon_data/clean_data/nodes_year.csv'




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

    films = df['title'].unique()
    

    # get actors per film
    for film in films:
        nominees = df[df['title'] == film]['name']
        nominees = nominees.reset_index(drop=True)

        # only include films with more than one nominees in it
        if len(nominees) != 1:
            for i in range(0, len(nominees)):
                for j in range(i+1, len(nominees)):
                    pairs = [[nominees[i], nominees[j], year]]
                    df1 = pd.DataFrame(pairs, columns = ['source', 'target','year'])
                    write_to_csv(df1, filepath)


def create_nodes_csv(df,filepath,year):
    '''
    Inputs: df - pandas DataFrame of nominee info
            filepath - string of output path

    This takes the nominee dataframe and converts
    to a smaller dataframe of two columns
    name and year nominee was in a film

    Returns: nothing
    '''

    nominees = df['name'].unique() 

    for nominee in nominees:
        df0 = [[nominee, year]]
        df1 = pd.DataFrame(df0, columns = ['name','year'])
        write_to_csv(df1, filepath)



clean_bacon_df = load_dataset(clean_bacon_df_path)
'''
print(a.head())
                   title  year      role                name
0  The Birth of a Nation  1915      star        Lillian Gish
1  The Birth of a Nation  1915      cast        Donald Crisp
2           Blade Runner  1982      star       Harrison Ford
3           Blade Runner  1982      star  Edward James Olmos
4           Blade Runner  1982  director        Ridley Scott
'''

print(min(clean_bacon_df.year))
#1812

#            title  year  role               name
#16808  Cop (film)  1812  star        James Woods
#this is an error in the bacon.txt data, ignore for now but only include movies after 
#1894, which is when the inventors of motion picture camera first shown commercially


# ONLY INCLUDE MOVIES 1894 AND AFTER BUT EXCLUDE MOVIES AFTER 2021
clean_bacon_df = clean_bacon_df[clean_bacon_df.year > 1894]
clean_bacon_df = clean_bacon_df[clean_bacon_df.year < 2022]
print(max(clean_bacon_df.year))
#2021
print(min(clean_bacon_df.year))
#1909


for year in range(min(clean_bacon_df.year),max(clean_bacon_df.year)+1):
    
    year_sub_df = clean_bacon_df[clean_bacon_df.year == year]
    
    # create edges
    create_edges_csv(year_sub_df,bacon_edges_path,year)

    #the nominees film info
    create_nodes_csv(year_sub_df,bacon_nodes_path,year)




# create edges
##create_edges_csv(clean_bacon_df,bacon_edges_path,year)
'''
               source              target
0        Lillian Gish        Donald Crisp
1       Harrison Ford  Edward James Olmos
2       Harrison Ford        Ridley Scott
3  Edward James Olmos        Ridley Scott
4         Gene Wilder       Madeline Kahn
'''

# create nodes
#per person condence film info into nested dictionary with each dictionary having
#the nominees film info
##create_nodes_csv(clean_bacon_df,bacon_nodes_path),year)
