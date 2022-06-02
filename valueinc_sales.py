# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:09:07 2022

@author: janee
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read csv

data = pd.read_csv('transaction.csv')

# was only reading one column, not registering correct seperator ';'
# since its default is ','
# declaring correct seperator for file below 

data = pd.read_csv('transaction.csv', sep = ';')

# summary of the data
data.info()

# Working with calculations
# Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem *NumberofItmesPurchased
# variable dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchansed = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchansed 

# Adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

#can also be written as
#data['CostPerTransaction'] =  data['CostPerItem'] *  data['NumberOfItemsPurchased']


#Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']



# Profit Calculation = Sales - Costs

data['ProfitsPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


# Markup = (Sales - costs) / Costs
data['MarkUp'] = (data['SalesPerTransaction'] -data['CostPerTransaction']) / data['CostPerTransaction']
#can also be written as
# data['MarkUp'] =  data['ProfitsPerTransaction'] / data['CostPerTransaction']


# Rounding MarkUp

roundmarkup = round(data['MarkUp'], 2)

#To change data in data file
data['MarkUp'] = round(data['MarkUp'], 2)


#Combining data fields


my_date = 'Day' + '-' + 'Month' + '-' + 'Year'


#Checking columns data type
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

#Using iloc to view specific columns/rows

data.iloc[0]  #views the row with index = 0
data.iloc[0:3]  #views first 3 rows
data.iloc[-5:]  #views last 5 rows

data.head(5)  #first 5 rows

data.iloc[:,2]  #views all rows on the second column

data.iloc[4,2] #fourth row, second column


#Using split to split the client keyword field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

#creating new columns for the split columns in ClientKeywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]


#Using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()


#How to merge files

#Bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

#Merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')


#Dropping columns

# df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#export into a CSV

data.to_csv('ValueInc_Cleaned.csv', index = False) #will not include index row







































