# %%

import pandas as pd
import pathlib as Path
import re
import numpy as np

def dataset_path():
    return r'D:\d_downloads\Kaggle Datasets\heart_disease_risk\Heart_Disease_Prediction.csv'



df = pd.read_csv(filepath_or_buffer=dataset_path())

# %%

dfFemale = df.query('Sex == 0')
#print(dfFemale.head())

sseries = pd.Series(np.zeros(df.index.size))
dfFemale = df.where(df['Sex'] == sseries).dropna(axis=0, how='all')
#print(dfFemale.head())


locational_boolean = pd.Series(df['Sex'] == 0)
dfFemale = df.loc[locational_boolean, :]
#print(dfFemale.head())

# %%

# One-hot Heart Disease col for range calculation
# Important since we can use Heart Disease as a predictor too


dfRanges = pd.get_dummies(df['Heart Disease'])
df['Heart Disease'] = dfRanges['Presence']

# %%
def getColumnRange(col):
    #print(type(col))
    range = int(col.max()) - int(col.min())
    return range


# axis = index, applies function to each column...

ranges = df.apply(axis='index', func=getColumnRange)
#print(ranges)


def getColumnStandardDeviation(col):
    mean = col.mean()
    reimannSumSqDist = 0
    for index, value in col.items():
        reimannSumSqDist = reimannSumSqDist + (value - mean)
    # Warning. Is array-like. Ints work, but here our numbers need float precision, therefore decimal place may be cause of warning
    return np.sqrt((reimannSumSqDist/(len(col) - 1)))




standardDeviations = df.apply(axis='index', func=getColumnStandardDeviation)
print(standardDeviations)


# %%
