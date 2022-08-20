import sys
import requests
import json
import pandas as pd
import Rikitha_Marvel_Activity_Functions as rmf3



def Filter_Marvel_Table_Ac5(ts,apikey,hash,nameStartsWith,filter_col,filter=None):
    # This is the filter table which filters out the given data from df based on the given column
    #Since system inputs are taken, function of activity 3 is directly being called here 
    # and the inputs taken in the functions are different from that of activity 4

    #Calling function from activity 3
    df = rmf3.Marvel_Table(ts,apikey,hash,nameStartsWith)
    # print(df)

    print(f'filter col is {df[filter_col]}')
    df.columns =[column.replace(" ", "_") for column in df.columns]
    filter_col = filter_col.replace(" ","_")
    total_condition = filter_col+filter
    print(total_condition)
    return df.query(total_condition)



# nameStartsWith = 'r'
# print("about to enter the function")

#Taking input from the user from terminal
# ts = input("Input the timestamp:  ")
# apikey = input("Input the API Key:  ")
# hash = input("Input the hash:  ")
# nameStartsWith = (input("Input the starting letter of the name of characters:  ")).upper()


#python activity5.py "ts" "api_key" "hash" "nameStartsWith" "filter_column_name" "filter_condition"
if __name__ == "__main__":
    # Arguments passed in CLI will be stored in args.
    args = sys.argv[1:] # 1: because the first entry is the filename itself which is not needed.
    # If only 3 arguments are passed then the character_df_generator function will be called else the character_filter function is called
    if(len(args) == 4):
        print("Calling Marvel_Table function from activity 3")
        print(rmf3.Marvel_Table(*args))
    else:
        print("Calling Filter_Marvel_Table function")
        print(Filter_Marvel_Table_Ac5(*args))

