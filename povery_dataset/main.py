import pandas as pd
import numpy as np
import re

def dataset_dir():
    return r'D:\d_downloads\Kaggle Datasets\poverty dataset\poverty.csv'


def bucket(x):
    if(x > 10):
        return 1
    if(x > 5):
        return 2
    return 3


def addSuffix(x):
    if(re.search('[03456789]', str(str(x)[-1:]))):
        return str(x) + 'th'
    if(re.search('1', str(x)[-1:])):
        if(len(str(x)) == 1 or str(x)[-2:] != '1'):
            return str(x) + 'st'
        return str(x) + 'th'
    if(re.search('2', str(str(x)[-1:]))):
        return str(x) + 'nd'
    if(re.search('3', str(str(x)[-1:]))):
        return str(x) + 'rd'
    
    
def percentageOfBucket(df, rank):    
    num = 0
    denom = df['povertyBucket'].size
    for i in range(0, df['povertyBucket'].size):
        if(df['povertyBucket'].iloc[i] <= rank):
            num = num + 1
    return re.search('[0-1]?[0-9][0-9]\.[0-9][0-9]', str(float(num / denom) * 100))[0] + '%'

if __name__ == "__main__":
    df = pd.read_csv(dataset_dir())
    
    dfPercent = df.sort_values(by = 'Percent in Poverty', axis=0, ascending=False)

    #df_2013 = df.query('Year == 2013')

    dfPercent['povertyBucket'] = pd.Series(dfPercent['Percent in Poverty'].apply(func=bucket))

    dfPercent['percentRank'] = np.arange(len(dfPercent.index))
    dfPercent['percentRank'] = dfPercent['percentRank'].apply(lambda x : x + 1)
    dfPercent['percentRank'] = dfPercent['percentRank'].apply(func=addSuffix)


    # Calculate what percentage of states in 2013 are in the level 1 bucket... for fun
        # What percentage of states = # of states in level 1 / all states of all levels


    dfPercent2013 = dfPercent.query('Year == 2013')

   
    # Calculate which states in 2013 have level 1
    x = percentageOfBucket(dfPercent2013, 1)
    print(x)


    #Work with group by aggregates and see what calculations you can do on the fly

    
    



