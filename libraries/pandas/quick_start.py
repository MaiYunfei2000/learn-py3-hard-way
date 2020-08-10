# Pandas 入门

import numpy as np
import pandas as pd

# 01
# [What kind of data does pandas handle? — pandas 1.1.0 documentation](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented)

# use a Python dictionary of lists to create a pandas dataframe
df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
             "Allen, Mr. William Henry",
             "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]
})

print(df)
print()

# each column in a DataFrame is a Series
print("df['Age']:\n", df["Age"])
print(type(df["Age"]))
print()

# create a Series from scratch as well
ages = pd.Series([22, 35, 58], name="Age")
print("ages:\n", ages)
print()

# the maximum Age (two equal expressions)
print(df["Age"].max())
print(ages.max())
print()

# basic statistics
print("basic statistics:\n", df.describe())
print(type(df.describe()))
print()


# 02
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented

# load the csv file 
titanic = pd.read_csv("titanic.csv")
print("titanic:\n", titanic)
print()

# see the first 8 rows of a pandas DataFrame
print(titanic.head(8))
# last 4 rows
print(titanic.tail(4))
print()

# check on datatype
print(titanic.dtypes)

# the titanic data as a spreadsheet
titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)

# read the excel
titanic = pd.read_excel('titanic.xlsx', sheet_name='passengers')
print()

# technical summary of a DataFrame
print(titanic.info())