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
    colName = report_df.columns[1]
    rename = f'{report_df.columns[0]}-{report_df.columns[1]}%'
    diffs = report_df.apply(np.diff, axis=1).astype(float)    
    return pd.Series(data=report_df[[colName]].applymap(lambda x : (x / diffs)*(1/100)).astype(float)[colName]).map('{}%'.format).rename(rename) # Returns as a dataframe, so needed to select '2015' column in order to turn it into a series.
    # Regex with the column names passed with report_df , use it to rename the series
    # Outside of function handles the input 


if __name__ == "__main__":
    df = pd.read_csv(wheat_dataset_dir())
    df = df.rename(mapper=renameColMapper, axis=1)
    columns = df.filter(regex='[0-9]', axis=1).columns # Select columns to assign munging to. Lets filtered out columns persist.
    df[columns] = df.filter(regex='[0-9]', axis=1).applymap(func=mungeObjs)
    df[columns] = df.filter(regex='[0-9]', axis=1).select_dtypes(object).astype(float)
    
    countrys = ['Canada']
    country_df = df.query('Country == @countrys').filter(regex='[0-9]')
    country_years = country_df.columns
    for i in range(2, len(country_years)):
        yr_report = processReport(country_df[[country_years[i], country_years[i-1]]])
        country_df = pd.concat([country_df, yr_report], axis=1)
        
    #canada_report = processReport(df.query('Country == @countrys')[['2014', '2015']])
    df = pd.concat([df, country_df], axis=1)
    print(df)
