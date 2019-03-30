import pandas as pd 
import numpy as np
import hashlib
import time

tStart = time.time()
df = pd.read_csv('NameOfClickStreamDataFile.csv',header=0)

df['sessionID'] = df['uuid'].astype(str) + df['date'].astype(str)
sessionIDList = df['sessionID'].tolist()
clicked_epochList = df['clicked_epoch'].tolist()
unique_combinations = list(set(sessionIDList))

clicked_epochDict = {k:[] for k in unique_combinations}
sessionIdDict = {k:hashlib.md5(k.encode()).hexdigest() for k in unique_combinations}

for i,val in enumerate(sessionIDList):
	clicked_epochDict[val].append(clicked_epochList[i])
	tList = clicked_epochDict[val]
	if len(tList)==1: pass		
	elif (tList[-1] - tList[-2])>=900:
		temp = sessionIdDict[val]
		sessionIdDict[val] = hashlib.md5(temp.encode()).hexdigest()

	sessionIDList[i] = sessionIdDict[val]

df['sessionID'] = sessionIDList

df.to_csv('clickStreamWithSessionID.csv',header=True)
print('Script Took->',time.time()-tStart,' seconds')



