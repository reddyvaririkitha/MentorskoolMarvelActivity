import requests
import json
import pandas as pd

# This file contains the function of activity 3 and activity 4. 

# ----------------------------------------Activity - 3------------------------------------------


# Created Exception for not passing the parameter
class ParameterNotPassedException(Exception):
    def __init__(self,msg):
        self.msg = msg
        print(msg)


def Marvel_Table(ts=None,api_key=None,hash=None,nameStartsWith='%'):    
    # Function - This helps in getting the marvel charecters for a particular alphabet
    # Arguments - ts = TimeStamp, api_key = public key of the marvel account,
    #             hash = md5 conversion of timestamp,public and private keys,
    #             nameStartsWith = starting letter of the marvel characters 
    # Returns the dataframe along with creating a csv file with the data

    #Checking if any argument is not given and raising the created exception
    if ts == None:
        raise ParameterNotPassedException("Timestamp not found")
    elif api_key == None:
        raise ParameterNotPassedException("API KEY ie, Public Key not found")
    elif hash == None:
        raise ParameterNotPassedException("Hash not found")
    
    # required constants
    limit = 100
    COLUMN_NAMES = ['Character Name','Number of Event appearances','Number of Series appearances','Number of Stories appearances','Number of comics appearances', 'Character_id']
    
    # initializing the dataframe
    df = pd.DataFrame(columns = COLUMN_NAMES)
    
    #urls and apis
    url = f'https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={api_key}&hash={hash}'
    final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}'
    output = requests.get(final_url)
    # print(output.status_code)
    o = output.json()

    # o["data"]["count"] gives the total number of marvel characters present with the given alphabet
    for i in range(o["data"]["count"]):
        # Taking all the results obtained for the given alphabet into char_list
        char_list = o["data"]["results"]
        # adding all the data of a row into df2 and then adding it to the main df
        df2 = pd.DataFrame({
                'Character Name':char_list[i]["name"],
                'Number of Event appearances': char_list[i]["events"]["available"],
                'Number of Series appearances': char_list[i]["series"]["available"],
                'Number of Stories appearances': char_list[i]["stories"]["available"],
                'Number of Comics appearances': char_list[i]["comics"]["available"],
                'Character_id': char_list[i]["id"]
        },index = [i])
        df = pd.concat([df,df2])

    # The above code gave only 100 rows of data as the limit for this API is only 100.
    # So the df contains 1st 100 rows of that particular character
    print(f'Before entering loop, df.shape[0] = {df.shape[0]}\n')
    n = o['data']['total']
    print(f'total charecters = {n}')
    temp_n = n # this variable is created for the below loop
    offset = 0 # this is used in the api call
    # This loop runs until we get all the rows of the marvel characters of that particular alphabet store in the df
    while temp_n > limit:
        # print("entered the loop")
        temp_n -= limit
        offset += limit
        #for every loop the offset gets increased and temp_n gets decreased.
        #rest of the code is same
        print(f'after entering the loop:temp_n = {temp_n},offset = {offset}')
        final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}&offset={offset}'
        output = requests.get(final_url)
        # print(output.status_code)
        o = output.json()
        print(f'o["data"]["count"] = {o["data"]["count"]}')
        for i in range(o['data']['count']):
            char_list = o["data"]["results"]
            df2 = pd.DataFrame({
                    'Character Name':char_list[i]["name"],
                    'Number of Event appearances': char_list[i]["events"]["available"],
                    'Number of Series appearances': char_list[i]["series"]["available"],
                    'Number of Stories appearances': char_list[i]["stories"]["available"],
                    'Number of Comics appearances': char_list[i]["comics"]["available"],
                    'Character_id': char_list[i]["id"]
            },index = [i+offset])
            df = pd.concat([df,df2])
        print(f'df.shape[0] in the loop = {df.shape[0]}\n')
    
    #Finally everything in the dataframe is stored in a csv file
    df.to_csv(f"Rikitha_Marvel_Characters_With_{nameStartsWith}_csv.csv")
    return df


# ----------------------------------------Activity - 4------------------------------------------

def Filter_Marvel_Table(df,filter_col,filter=None):
    # This is the filter table which filters out the given data from df based on the given column
    print(f'filter col is {df[filter_col]}')
    df.columns =[column.replace(" ", "_") for column in df.columns]
    filter_col = filter_col.replace(" ","_")
    total_condition = filter_col+filter
    print(total_condition)
    return df.query(total_condition)