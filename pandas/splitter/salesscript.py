import pandas as pd
from pandas import DataFrame, Series
import os
from glob import glob

#%%

def retrieveFilesRecursively(PATH = None, extensions = ['csv', 'xls', 'xlsx']):
    '''
    Returns a list of file strings of a given path (recursively) that match a certain extension
    '''
    result = [] #initialise to empty string
    if PATH is None:
        PATH = os.getcwd() + '/input/'
        
    for ext in extensions:
        result += [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.' + ext))]
        
    return result

def readAndAggregateData(fileList):
    dfList = []
    for fileName in fileList:
        dfList.append(pd.read_excel(fileName))
    
    return pd.concat(dfList)
    
def filterBySplitter(df):
    filt = df['Legal Description'].str.contains('L[0-9]*-|&|,', na=False)
    return df[filt]

def filterByVacantLand(df):
    filt = df['Property Type'].str.contains('Vacant Land', na=False)
    return df[filt]

def outputData(df, PATH = None):
    if PATH is None:
        PATH = os.getcwd() + '/output/'
        
    #for suburb, group in df.groupby('Locality'):
        #group.to_excel(PATH + suburb + '.xlsx', sheet_name='Sheet1')
    df.to_excel(PATH + 'results.xlsx', sheet_name='Sheet1')

if __name__ == "__main__":
    rawFiles = retrieveFilesRecursively()
        
    df = readAndAggregateData(rawFiles)
    
    filteredDf = filterBySplitter(df)
    
    outputData(filteredDf)



