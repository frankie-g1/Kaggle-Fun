# %%
import pandas as pd
import numpy as np

df = pd.read_csv('D:\d_downloads\Kaggle Datasets\International wheat production statistics.csv')

# %%
countrys = ['Canada']
df = df.query('Country == @countrys').filter(regex='[0-9]')
print(df)
print(type(df))
df[['1997', '1996']]
# %%

# Check out Country column, or see if you can transpose it

countrys = wheat_df['Country']
print(countrys)
print(type(countrys))

# %%
country = ['Canada']
row = wheat_df.query('Country == @country')
#print(row)
#print(type(row))
s = pd.Series(data=row.iloc[0])
print(s)
# %%
# Focusing on one row, in this case Canda

# Mask way - Those filtered out become NaN

mask = (wheat_df['Country'] == 'Canada')
wheat_df_mask = wheat_df.where(mask)
wheat_df_mask.head()


# Query way. This reduces the dataframe to 1 row

countrys = ['Canada']
canada_df = wheat_df.query('Country == @countrys')
print(canada_df.head())

# %%
# working with canada_df 
#print(canada_df.head())
## Accesss the columns
can_cols = canada_df.columns
#print(can_cols)
#
#print(canada_df[can_cols[0]])
#print(canada_df['2014[3]'])

# Cleaning up column names
import re 
regex = '\[[0-9]\]' # Find the occurence of [number] if it exists, and we always take first slice.
def renameCol(col_name):
    return re.split(regex, col_name)[0]

canada_df = canada_df.rename(mapper=renameCol, axis=1, inplace=False)


# %% 

# Change year col's values into numbers
regex = '[0-9]'
canada_df = canada_df.filter(regex=regex, axis=1).select_dtypes('object').astype(float)


# %%

#print(twoYears)

# Labmda produces output based on 1 to X columns existing, or does an aggregate individually on each column. 
# Be able to control this, by controlling the input passed to the lambda funbction, by for instance, passing a specific dataframe to it.
diff = canada_df[['2015', '2014']].apply(np.diff, axis=1).astype(float)
canada_df['2015perc'] = canada_df[['2015']].applymap(lambda x : diff / x)
print(canada_df)


