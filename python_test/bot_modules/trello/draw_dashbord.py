import matplotlib as mpl
import pandas as pd
import numpy as np
import json
from get_trelo_score import get_trello_data


# trello_data = get_trello_data()
# with open ('trello_data.txt','w') as file:
#     file.write(json.dumps(trello_data))
with open('trello_data.txt','r') as file:
    trello_data = json.load(file)

max_len = max([len(i[2]['who']) if i[2]['who'] else 0 for i in trello_data])    # Find maximum members per card for set
                                                                                #    index dataframe dimension

indeces1 = [el[0] for el in trello_data]                                        # First column of index dataframe
indeces2 = pd.DataFrame(index =range(len(indeces1)),columns = range(max_len)).fillna(0)     # Rest index_dataframe columns
for i in range(max_len):                                                        # Fill rest columns with respect of number
                                                                                #    of members (max_len) 
    indeces2.iloc[:,i] = [  el[2]['who'][i] 
                              if el[2]['who'] and len(el[2]['who']) > i 
                              else None 
                              for el in trello_data]

data = [  (el[1],el[2]['time_start'],el[2]['time_close']) 
              for el in trello_data]
indeces = pd.MultiIndex.from_frame(indeces2)
frame = pd.DataFrame(data,indeces)

print(frame[0]['Wombat(Олег)'])