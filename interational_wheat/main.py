# Run reports based on year over year and find neat new statistics based on other perspective angles other than year over year fluctuation on a country
# Ideas : 


import pandas as pd
import pathlib as Path
import re
import numpy as np


def wheat_dataset_dir():
    return r'D:\d_downloads\Kaggle Datasets\International wheat production statistics.csv'

def renameColMapper(x):
    return re.split('\[[0-9]\]', x)[0]

def mungeObjs(x):
    regex = '\[[0-9]\]'
    return re.split(regex, str(x))[0]

def processReport(report_df):
    diffs = report_df.apply(np.diff, axis=1).astype(float)      
    return pd.Series(data=report_df[['2015']].applymap(lambda x : (x / diffs)*(1/100)).astype(float)['2015']).map('{}%'.format).rename('14-15') # Returns as a dataframe, so needed to select '2015' column in order to turn it into a series.
    # Regex with the column names passed with report_df , use it to rename the series
    # Outside of function handles the input 


if __name__ == "__main__":
    df = pd.read_csv(wheat_dataset_dir())
    df = df.rename(mapper=renameColMapper, axis=1)
    columns = df.filter(regex='[0-9]', axis=1).columns # Select columns to assign munging to. Lets filtered out columns persist.
    df[columns] = df.filter(regex='[0-9]', axis=1).applymap(func=mungeObjs)
    df[columns] = df.filter(regex='[0-9]', axis=1).select_dtypes(object).astype(float)
    countrys = ['Canada']
    canada_report = processReport(df.query('Country == @countrys')[['2014', '2015']])
    df = pd.concat([df, canada_report], axis=1)
    print(df)
