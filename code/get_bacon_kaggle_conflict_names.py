#!/usr/bin/python

# DS4A Project
# Group 84
# Checks for nominees of interest in bacon website and replaces kaggle dataset names with those in bacon


import itertools as itr
import numpy as np
from os import path
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




# Global Vars

# change to the path of the chromedriver on your computer
driver_path = "C:\Program Files (x86)\chromedriver.exe"

# changes not needed
dataset_file_path = "data/the_oscar_award.csv"
problem_names_path = "data/check.csv"
corrected_names_path = "data/corrected_names.csv"
corrected_dataset_path = "data/the_oscar_award_corrected.csv"
categories_interest = ['ACTOR',
                       'ACTRESS',
                       'ACTOR IN A LEADING ROLE',
                       'ACTRESS IN A LEADING ROLE',
                       'ACTOR IN A SUPPORTING ROLE',
                       'ACTRESS IN A SUPPORTING ROLE',
                       'DIRECTING',
                       'DIRECTING (Comedy Picture)',
                       'DIRECTING (Dramatic Picture)']



# Functions
def get_nominees_links(nominee1, nominee2, driver):
    """
    Inputs:
    nominee1 - python string
    nominee2 - python string

    The selenium module is used to navigate
    https://oracleofbacon.org/
    using the function inputs to fill in
    the textboxes

    Returns: an integer for connection found
             0 for no  connection found
             9999 for nominee(s) not in database
    """

    # Select advance checkbox
    driver.find_element_by_id("morebutton").click()
    if not driver.find_element_by_name("rt1").is_selected():
        driver.find_element_by_name("rt1").click()
    if not driver.find_element_by_name("rt2").is_selected():
        driver.find_element_by_name("rt2").click()

    # Fill in textbox with nominees and find link
    inputElement = driver.find_element_by_id("a")
    inputElement.clear()
    inputElement.send_keys(nominee1)

    inputElement = driver.find_element_by_id("b")
    inputElement.clear()
    inputElement.send_keys(nominee2)
    inputElement.send_keys(Keys.ENTER)


    # get result
    res = driver.find_element_by_id("main").text
    res = res.split(".")[0]

    # case nominee not found in database
    if "The Oracle cannot find" in res:
        return 9999

    # connection found
    if any(map(str.isdigit, res)):
        number = [int(word) for word in res.split() if word.isdigit()][0]
        return number

    # no connection found
    return 0


def check_name_exists_on_bacon(df, filepath):
    '''
    inputs: pandas dataframe of nominees

    checks if name exists in oracleofbacon
    writes a csv of names to check

    returns: nothing
    '''

    # Load oracle of bacon webpage
    driver = load_webpage(driver_path)

    # Drop duplicate names and reset the index
    df = df.drop_duplicates('name')

    # Sort dataframe by names in alphabetical order
    #df = df.sort_values(by = 'name')

    # Reset dataframe index after the sorting
    df = df.reset_index(drop=True)

    # get just names column
    df = df['name']

    # check name exists in oracleofbaron
    for i in df:
        links = get_nominees_links(i, "Kevin Bacon",driver)
        time.sleep(random.randint(1,3))
        if links == 9999:
            problem_names = pd.DataFrame({'problem_names':[i]})
            write_to_csv(problem_names, filepath)

    # Exit webpage
    driver.quit()


def fix_problem_names(df1,df2,filepath):
    '''
    Inputs: df1 - original pandas df
            df2 - pandas df of correct
                  nominee names

    This takes the original
    dataframe and replaces the problem
    names with the ones in the
    corrected names DataFrame

    for names with more than two people
    the entries are copied and the original
    and copied entries each recieve
    one of the names

    writes the output to a csv file

    Returns: nothing
    '''

    # replacement dict
    dict = df2.set_index('problem_names')['name'].to_dict()

    # replace problem names using replacement dict
    df1['name'] = df1['name'].replace(dict)

    # output fixed of original dataframe with fixed nominee names
    write_to_csv(df1,filepath)


def write_to_csv(df,filepath):
    '''
    input: a pandas DataFrame

    writes to a csv file
    in same diretory as this script

    returns: nothing
    '''
    # if no csv exists
    if not path.exists(filepath):
        df.to_csv(filepath,index=False)
    else:
        df.to_csv(filepath, mode='a', header=False,index=False)


def load_webpage(filepath):
    driver = webdriver.Chrome(filepath)
    driver.get('https://oracleofbacon.org/')
    return driver


def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


# load dataset
nominees_df = load_dataset(dataset_file_path)

# Drop any category not in categories_interest
nominees_int_df = nominees_df[nominees_df['category'].isin(categories_interest)]

## Check names exist in Oracle of bacon, output will be a csv
#check_name_exists_on_bacon(nominees_int_df, problem_names_path)

# corrected_names_path was created by adding another column to check.csv
# with names checked for spelling on oracle of bacon
# Fix dataset by placing in correct nominee names
#fix_problem_names(nominees_df, load_dataset(corrected_names_path),
#                    corrected_dataset_path)
