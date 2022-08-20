import Rikitha_tsapikeyhash as rtah
import Rikitha_Marvel_Activity_Functions as rmf3

#This file is th input file of the activity 3 and function is being called here

nameStartsWith = 'S'

df = rmf3.Marvel_Table(ts = rtah.ts,api_key = rtah.apikey,hash = rtah.hash,nameStartsWith = nameStartsWith)
print(df)