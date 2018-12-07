
import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

#df = pd.read_csv('QueryResults.csv')
#print(df)

path = 'Users.xml'
dfcols = ['Id', 'AboutMe', 'Reputation']

root = et.parse(path)
rows = root.findall('.//row')

# NESTED LIST
xml_data = [[row.get('Id'), row.get('AboutMe'), row.get('Reputation')] 
            for row in rows]

df = pd.DataFrame(xml_data, columns=dfcols)
print(df)

path = 'Badges.xml'
dfacols = ['Id','Badge']

root = et.parse(path)
rows = root.findall('.//row')



# NESTED LIST
xml_data = [[row.get('UserId'),row.get('Name')] 
            for row in rows]

dfb = pd.DataFrame(xml_data, columns=dfacols)

trueu = pd.merge(df, dfb, on='Id', how='inner')
trueu.to_csv('users.csv', encoding='utf-8')

#about = df.loc[:,'AboutMe']
#doc_complete = df.loc[:,'AboutMe']
#doc_complete.fillna("", inplace=True)
#print(about)

path = 'Posts.xml'
dfpcols = ['Id','OwnerUserId', 'AcceptedAnswerId','DeletionDate', 'CreationDate', 'Tags', 'Score', 'ViewCount', 'Question','PostTypeId','AnswerCount']

root = et.parse(path)
rows = root.findall('.//row')

# NESTED LIST
xml_data = [[row.get('Id'),row.get('OwnerUserId'),row.get('AcceptedAnswerId'),row.get('DeletionDate'),row.get('CreationDate'),row.get('Tags'),row.get('Score'),row.get('ViewCount'),row.get('Body'),row.get('PostTypeId'),row.get('AnswerCount')] 
            for row in rows]


dfp = pd.DataFrame(xml_data, columns=dfpcols)
print(dfp)
notEm  = dfp['AnswerCount'] > 0
dpf =dfp.fillna(value=-1, inplace=True)
print('DFP2')
dfp[["PostTypeId", "AnswerCount"]] = dfp[["PostTypeId", "AnswerCount"]].apply(pd.to_numeric)
print(dfp)
dfp3 = dfp.loc[(dfp['PostTypeId'] == 1) & (dfp["AnswerCount"] > 0) & (dfp["AcceptedAnswerId"].astype(int) != -1) ]
print(dfp3)

path = 'Posts.xml'
dfacols = ['pId','OwnerUserId', 'Id', 'CreationDate', 'Tags', 'Score', 'ViewCount','PostTypeId','Answer']

root = et.parse(path)
rows = root.findall('.//row')

# NESTED LIST
xml_data = [[row.get('Id'),row.get('OwnerUserId'),row.get('ParentId'),row.get('CreationDate'),row.get('Tags'),row.get('Score'),row.get('ViewCount'),row.get('PostTypeId'),row.get('Body')] 
            for row in rows]

dfa = pd.DataFrame(xml_data, columns=dfacols)

dpa = dfa.fillna(value=-1, inplace=True)
dfa[["PostTypeId"]] = dfa[["PostTypeId"]].apply(pd.to_numeric)
dfa2 = dfa.loc[dfa['PostTypeId'] == 2]
print(dfa2)

true = pd.merge(dfp3, dfa2, on='Id', how='inner')
print(true)

true.to_csv('res.csv', encoding='utf-8')





