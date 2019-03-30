import pandas as pd 
import numpy as np 
import time
from matplotlib import pyplot as plt
import os

def normalize(v,valueList):
    minval = min(valueList)
    maxval = max(valueList)
    return ((v-minval)/(maxval-minval))

tStart = time.time()
print('Script Started...Please Wait')
df = pd.read_csv('transactions.csv',header=0)
if not os.path.isfile('./Visualizations'):
    os.mkdir('./Visualizations') 

df['category'] = df['category'].str.replace(r' +', '-')
categories = list(df.category.unique())

# print('Unique Categories are->',categories)

df['date'] = df['date'].astype(str)
df['date'] = [val[:-3] for val in df['date']] #Only need the Year and Month for seasonality

# print('DF Head->')
# print(df.head())

resultDict = {k:{y:{} for y in list(df['date'].unique())} for k in categories}
seasonalScoresDict = {k:{y:0 for y in list(df['date'].unique())} for k in categories}
for category in categories:
    # print('For Category->',category)
    dfTempMain = df[df['category']== category].copy()
    yearMonths = list(dfTempMain['date'].unique())
    for yearMonth in yearMonths:        
        dfTemp = dfTempMain[dfTempMain['date']==yearMonth].copy()        
        dfTemp['count'] = dfTemp['product_id'].map(dfTemp['product_id'].value_counts())
        dfTemp.sort_values('count',inplace=True,ascending=False)
        dfTemp.reset_index(drop=True)
        dfTemp = dfTemp[~(dfTemp['count']<20)] #Atleast 30 purchases to form a trend
        if len(dfTemp):
            # print('\n\tduring '.upper(),yearMonth)
            res = dfTemp['product_id'].value_counts().to_dict()
            resultDict[category][yearMonth] = res
            seasonalScoresDict[category][yearMonth] += len(res)
            productCountPairs = [[product,count] for product,count in resultDict[category][yearMonth].items()]
            products = [pair[0] for pair in productCountPairs]
            counts = [pair[1] for pair in productCountPairs]
            plt.pie(counts, labels=products,autopct='%1.1f%%') 
            plt.axis('equal')
            plt.savefig('./Visualizations/'+category+'('+yearMonth+').png', bbox_inches='tight')
            plt.clf()

        
    resultDict[category] = {k:v for k,v in resultDict[category].items() if len(v)>0}
    netScoreList =list(seasonalScoresDict[category].values())
    seasonalScoresDict[category] = {k:normalize(v,netScoreList) for k,v in seasonalScoresDict[category].items() if v>0}
    # print('------------------------------------')

print('Visualizations Generated in ./Visualizations Folder!')
print('SEASONAL SCORES:')
for cat in seasonalScoresDict:
    print('Category:',cat)
    for season,score in seasonalScoresDict[cat].items():
        print('\tSeason:{0} Score:{1}'.format(season,score))
print('Script Took->',time.time()-tStart,' seconds to execute!')

