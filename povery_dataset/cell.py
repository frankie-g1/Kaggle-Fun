# %%

import pandas as pd
import numpy as np
import re

def dataset_dir():
    return r'D:\d_downloads\Kaggle Datasets\poverty dataset\poverty.csv'


df = pd.read_csv(dataset_dir())

# %% 

print(df.head())
# %%
df = df.sort_values(by = 'Percent in Poverty', ascending=False, axis=0)
df['placement'] = np.arange(len(df.index)) # don't wrap right side with pd.Series... placement'd be the index
df['placement'] = df['placement'].apply(lambda x : x + 1)

columns = df.columns.to_list()

columns = columns[:-1] # Must be a two step process, or else its assignment becomes None type
columns.insert(0, df.columns.to_list()[-1])

df = df[columns] # list reordering fashion. All keys must exist


# re running always takes last column and places it first, due to memory of df persisting of each iterative run
# %%

def suffix(value):
    value = str(value)
    match = re.search('[1]', value[-1])
    match2 = re.search('[2]', value[-1])
    match3 = re.search('[3]', value[-1])
    if(match):
        if(len(value) > 1):
            if(value[-2] == '1'):
                return value + 'th'
        return value + 'st'
    if(match2):
        return value + 'nd'
    if(match3):
        return value + 'rd'
    return value + 'th'

df['placement'] = df['placement'].apply(func=suffix)

print(df['placement'])

# %%

def unapply(value):
    value = str(value)
    match = re.search('[a-zA-Z]', value)
    if(match):
        value = value[0:match.span()[0]]
    return value

df['placement'] = df['placement'].apply(func=unapply)

print(df['placement'])

# %%
