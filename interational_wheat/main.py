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
    return pd.Series(data=report_df[[colName]].apply(lambda x : ( diffs / x))[colName].astype(float)).map('{}%'.format).rename(rename) # Returns as a dataframe, so needed to select '2015' (colName) column in order to turn it into a series.
    # Regex with the column names passed with report_df , use it to rename the series
    # Outside of function handles the input 

def selectCountries(countries, user_countries):
    if(len(user_countries) == 0):
        return
    buildMask = (countries == user_countries[0])
    for i in range(1, len(user_countries)):
        mask = (countries == user_countries[i])
        buildMask = buildMask | mask
    return buildMask    

if __name__ == "__main__":
    df = pd.read_csv(wheat_dataset_dir())
    df = df.rename(mapper=renameColMapper, axis=1)
    columns = df.filter(regex='[0-9]', axis=1).columns # Select columns to assign munging to. Lets filtered out columns persist.
    df[columns] = df.filter(regex='[0-9]', axis=1).applymap(func=mungeObjs)
    df[columns] = df.filter(regex='[0-9]', axis=1).select_dtypes(object).astype(float)

    # works, but want mask to be buildable
    #mask = (df['Country'] == 'Canada') | (df['Country'] == 'United States')
    #print(df[mask])

    
    canadaUS = df[selectCountries(df['Country'], ['Canada', 'United States', 'Spain'])]# Following below example, as our goal was to create a boolean series
    #print(canadaUS)
    country_years = canadaUS.columns
    for i in range(3, len(country_years)):
        yr_report = processReport(canadaUS[[country_years[i], country_years[i-1]]])
        canadaUS = pd.concat([canadaUS, yr_report], axis=1)


    data = df[selectCountries(df['Country'], ['Canada', 'United States', 'Spain'])]
    #print(data.stack().head(50)) # Repeatable indexes per row of original dataframe.

    #print(data.pivot(index=['1996', '1997', '2018', '2019'], columns='Country').head(20))

    #print(data.swapaxes(axis1=1, axis2=0)) # Physical rotate - when you want a columns values (each row of a column) to be the columns. Great for having countrys become their own column.
                                                                                # It'll take all column values of a row though, so the real columns will be the index i.e. 1,2,3, but underneath that will match.
    #user_list = ['Canada', 'United States']
    #country_s = df['Country']
    #mask = (country_s == user_list[0]) | (country_s == user_list[1])
    #g = country_s.where(mask) == df['Country'] # Really unecessary, above is equivalent. Can use multiple columns - if so, df['Country'] would no longer work, it'd need to be same size.
    ##print(g)
    #print(df[g])
   #_countries_series = df['Country']
   #_countries_series[(_countries_series == 'Canada') | _countries_series == 'United States']
   #
   #boolSeries = df[mask]
   #print(boolSeries)
    
    #countrys = ['Canada', 'United States']
    #country_df = df.query('Country == @countrys[0] | Country == @countrys[1]').filter(regex='[0-9]')
    #country_years = country_df.columns
    #print(country_years)
#
    #all_df = df.filter(regex='[0-9]')
    #all_years = all_df.columns 
#
    ##for i in range(2, len(country_years)):
    ##    yr_report = processReport(country_df[[country_years[i], country_years[i-1]]])
    ##    country_df = pd.concat([country_df, yr_report], axis=1)    
    ###canada_report = processReport(df.query('Country == @countrys')[['2014', '2015']])
#
    #for i in range(2, len(all_years)):
    #    yr_report = processReport(all_df[[all_years[i], all_years[i-1]]])
    #    all_df = pd.concat([all_df, yr_report], axis=1)
#
#
    #print(all_df.filter(regex='19'))
    ##df = pd.concat([df, all_df], axis=1) # Concatenating this with this, duplicate year columns appear
    ##print(df)
##
    ##denmark = ['Denmark']
    ##print(df.query('Country == @denmark').filter(regex='19'))
