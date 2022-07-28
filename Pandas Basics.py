#Excercise found on Keith Galli Youtube channel. link: https://www.youtube.com/watch?v=vmEHCJofslg


import pandas as pd
import openpyxl
import re

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv')


#1. Print top 5 rows
print(df.head(5))

#2.Printing column names
print(df.columns)

#3. Print All data from column name
print (df['Name'])

#4. Print Top 5 Names
print (df['Name'][0:5])
print (df.Name)

#5. Read more than 1 column
print (df[['Name','Type 1', 'HP']])

#6. Print each row for specific ID
print(df.iloc[2])
print(df.iloc[2:4])

#7. Read a specific location (R,C)
print(df.iloc[2,1])

#8. Access through all rows
for index, row in df.iterrows():
print(index, row['Name'])


#9. Word Search like a regex in SQL
print(df.loc[df['Type 1']== "Grass"])

#10. Sorting the Data
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))


#11. Summing the rows the old faschioned way and the more advanced one. Also Showing the whole dataframe.
#One way
df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
pd.options.display.max_columns = 15
pd.set_option('display.width', 200)
print(df.head(5))

#Other way
df['Total']=df.iloc[:,4:10].sum(axis=1)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 200)
print(df.head(5))

#12. Rearranging columns the way you want them to be with implementing show all columns from the previous excercise.
df['Total']=df.iloc[:,4:10].sum(axis=1)
cols = list(df.columns)
pd.options.display.max_columns = 15
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
pd.set_option('display.width', 200)
print(df)

#13. Saving to csv, excel, notepad document.
df.to_csv('modified.csv', index=False)
df.to_excel('modified.xlsx', index=False)
df.to_csv('modified.txt', index=False, sep='\t')


#14. Filtering rows based on more than 1 condition (using And/Or), reseting index.
pd.options.display.max_columns = 15
pd.set_option('display.width', 200)
new_df=df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']> 70)]
new_df=new_df.reset_index(drop=True)
print(new_df)

#15. Regex Filtering and changing column data(conditional formatting)
pd.set_option('display.width', 200)
df=df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(df)

df.loc[df['Type 1']== 'Fire', 'Type 1']='Flamer'
df.loc[df['Type 1']== 'Fire', 'Legendary']=True
print(df)

#17. Adding a change to more than 1 column
df.loc[df['Total']>500,['Generation', 'Legendary']]='TEST V'
print(df)


#18. Aggregate functions sum, mean, count.
pd.options.display.max_columns=15
pd.set_option('display.width',200)
df=df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
print(df)

df['Count']=1
df=df.groupby(['Type 1', 'Type 2']).count()['Count']
print(df)

#19. large dataframes
for df in pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv', chunksize=5):
print("Chunk DF")
print(df)

new_df=pd.DataFrame(columns=df.columns)
for df in pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv', chunksize=5):
results=df.groupby(['Type 1']).count()
new_df=pd.concat([new_df, results])
print(new_df)
