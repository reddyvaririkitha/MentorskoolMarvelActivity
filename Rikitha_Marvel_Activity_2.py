import requests
import json
import pandas as pd
import Rikitha_tsapikeyhash as rtah

# required constants
url = f'https://gateway.marvel.com:443/v1/public/characters?ts={rtah.ts}&apikey={rtah.apikey}&hash={rtah.hash}'
limit = 100
COLUMN_NAMES = ['Character Name','Number of Event appearances','Number of Series appearances','Number of Stories appearances','Number of comics appearances', 'Character_id']

# initializing the dataframe
df = pd.DataFrame(columns = COLUMN_NAMES)

a = "%" #Instead of going through every charecter, we can use % to get all charecters

# Outer loop which runs for all ascii characters to get all the marvel characters
for nameStartsWith in a:
    print(nameStartsWith)
    # final url = api to be sent
    final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}'
    # output from requests module
    output = requests.get(final_url)
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
    print(f'total number of marvel charecters = {n}')
    temp_n = n # this variable is created for the below loop
    offset = 0 # this is used in the api call
    # This loop runs until we get all the rows of the marvel characters of that particular alphabet store in the df
    while temp_n > limit:
        temp_n -= limit
        offset += limit
        #for every loop the offset gets increased and temp_n gets decreased.
        #rest of the code is same
        print(f'after entering the loop:temp_n = {temp_n},offset = {offset}')
        final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}&offset={offset}'
        output = requests.get(final_url)
        o = output.json()
        # print(f'o["data"]["count"] = {o["data"]["count"]}')
        for i in range(o["data"]["count"]):
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
df.to_csv("Rikitha_Marvel_Activity_2_csv.csv")
print(df)