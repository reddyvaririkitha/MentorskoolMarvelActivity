import requests
import json
import pandas as pd
import Rikitha_tsapikeyhash as rtah
import Rikitha_Marvel_Activity_Functions as rmf3

nameStartsWith = 'm'
#Calling function from activity 3
df = rmf3.Marvel_Table(rtah.ts,rtah.apikey,rtah.hash,nameStartsWith)
# print(df)

#Callling function from activity 4
df_ac4 = rmf3.Filter_Marvel_Table(df=df,filter_col='Number of Comics appearances',filter='<=60')
# df=df,filter_col='Character Name',filter='.str.startswith("Z")'
print(df_ac4)