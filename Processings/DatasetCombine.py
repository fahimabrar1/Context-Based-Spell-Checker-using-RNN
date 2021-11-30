import os
import pandas as pd
#cwd = os.path.abspath('D:\Python\Context Based Spell Checker using RNN\Test Sheets')
cwd = os.path.abspath('D:\Python\Context Based Spell Checker using RNN')
files = os.listdir(cwd)

print(files)


## Method 2 gets all sheets of a given file
df_total = pd.DataFrame()
df_total['wordList'] =[]
for file in files:                         # loop through Excel files
    if file.endswith('.csv'):
        print(file)
        path = cwd + '\\' +file
        temp_df = pd.read_csv(path)
        df_total = pd.concat([df_total,temp_df] )
        

print(df_total)
df_total.to_csv('corpusDhakaTribune_2.csv')
