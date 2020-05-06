import pandas as pd
import numpy as np

df1 = pd.read_csv('./complaints.csv', error_bad_lines=False,encoding="ISO-8859-1",usecols=['Date received','Product','Company'])
df2=df1.copy()
df2['Year']=df2['Date received'].str.split("-", n = 1, expand = True)[0]
df2=df2.drop('Date received',axis=1) #dropping date received
df2['Product'] = df2['Product'].str.lower()
df2['Company'] = df2['Company'].str.lower()
i=0
for group, frame in df2.groupby(['Year','Product']):
    (unique, counts) = np.unique(frame['Company'], return_counts=True)
    no_complains=sum(counts)
    no_companies=len(unique)
    #print(group)
    #print("Total no. of complains",no_complains)
    #print("No of companies:",no_companies)
    #print("highest % of complaints dir towards a single company:",max(counts)/sum(counts)*100)
    #print("----------------------")
    if i==0:
        df3=pd.DataFrame({'Year and Product':[group[0]+" " + group[1]],'No. of complains':no_complains,'No. of companies':no_companies,'Highest % of complaints for single company':max(counts)/sum(counts)*100})
        #print(df3)
    else:
        df3=df3.append({'Year and Product':group[0]+" " + group[1],'No. of complains':no_complains,'No. of companies':no_companies,'Highest % of complaints for single company':max(counts)/sum(counts)*100},ignore_index=True)
        #print(df3)
    i+=1
df3.to_csv('./report.csv', index=True,mode='a')
    #print(df3) #Not saving correctly; only saves last entry
