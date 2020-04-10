{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import datetime as dt\n",
    "import os\n",
    "os.listdir(r\"C:\\Users\\Pratik Pednekar\\Desktop\\Insight challenge\\Data\")\n",
    "cwd = os.getcwd()\n",
    "cwd\n",
    "inputfile = r\"C:\\Users\\Pratik Pednekar\\Desktop\\Insight challenge\\Data\"\n",
    "#for file in os.listdir(inputfile):\n",
    "    #df1=pd.read_csv(r\"C:\\Users\\Pratik Pednekar\\Desktop\\Insight challenge\\Data\\data_trial.csv\",encoding=\"ISO-8859-1\",usecols=['Date received','Product','Company'])\n",
    "url = 'https://github.com/pratik-pednekar/Insight_Challenge/tree/master/input/complaints.csv'\n",
    "df = pd.read_csv(url, error_bad_lines=False,encoding=\"ISO-8859-1\",usecols=['Date received','Product','Company'])\n",
    "df2=df1.copy()\n",
    "df2['Year']=df2['Date received'].str.split(\"-\", n = 1, expand = True)[0]\n",
    "df2=df2.drop('Date received',axis=1) #dropping date received\n",
    "df2['Product'] = df2['Product'].str.lower()\n",
    "df2['Company'] = df2['Company'].str.lower()\n",
    "i=0\n",
    "for group, frame in df2.groupby(['Year','Product']):\n",
    "    (unique, counts) = np.unique(frame['Company'], return_counts=True)\n",
    "    no_complains=sum(counts)\n",
    "    no_companies=len(unique)\n",
    "    #print(group)\n",
    "    #print(\"Total no. of complains\",no_complains)\n",
    "    #print(\"No of companies:\",no_companies)\n",
    "    #print(\"highest % of complaints dir towards a single company:\",max(counts)/sum(counts)*100)\n",
    "    #print(\"----------------------\")\n",
    "    if i==0:\n",
    "        df3=pd.DataFrame({'Year and Product':[group[0]+\" \" + group[1]],'No. of complains':no_complains,'No. of companies':no_companies,'Highest % of complaints for single company':max(counts)/sum(counts)*100})\n",
    "        #print(df3)\n",
    "    else:\n",
    "        df3=df3.append({'Year and Product':group[0]+\" \" + group[1],'No. of complains':no_complains,'No. of companies':no_companies,'Highest % of complaints for single company':max(counts)/sum(counts)*100},ignore_index=True)\n",
    "        #print(df3)\n",
    "    i+=1\n",
    "df3.to_csv('report.csv', index=True,mode='a')\n",
    "    #print(df3) #Not saving correctly; only saves last entry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
