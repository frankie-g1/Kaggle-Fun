# 13 features to help us tinker with varying models parameters and model types (# of variables or type of model too)


import pandas as pd
import pathlib as Path
import re
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import tree

def filePath():
    return r'D:\d_downloads\Kaggle Datasets\heart_disease_risk\Heart_Disease_Prediction.csv'

if __name__ == "__main__":
    
    df = pd.read_csv(filePath(), header=0)

    df = df[df.columns[~df.columns.isin(['index'])]]

    y = pd.get_dummies(df[df.columns[df.columns.isin(['Heart Disease'])]])
    y = y['Heart Disease_Presence']


    x = df[df.columns[~df.columns.isin(['Heart Disease'])]]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)

    print(clf.predict(np.array([[80, 1, 1, 130, 270, 0, 2, 120, 0, 0.3, 2, 3, 7]]))[0]) 

    # Thallium Heart feature



    #x_train, x_test, y_train, y_test = train_test_split(test_df, df['Heart Disease'])
#
    #LogReg = LogisticRegression(solver='lbfgs')
#
    #LogReg.fit(x_train, y_train)
#
    #LogReg.predict(np.array([[80, 1, 1, 130, 270, 0, 2, 120, 0, 0.3, 2, 3, 0]]))