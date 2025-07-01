# PANDAS
# Data Manipulation package 
import pandas as pd
a1 = [0, 2, 3, 4]
a2 = [10, 20, 30 ,40]
a3 = list(range(4))

# Creating a data frame using explicit lists
# Dataframe is a pandas object
# Contains rows and columns 
df = pd.DataFrame(columns = ['X1', 'X2', 'X3'])
df['X1'] = a1
df['X2'] = a2
df['X3'] = a3
print(df)

# Giving Index values
df_new = pd.DataFrame(columns = ['X1', 'X2', 'X3'], index = [101, 102, 103, 104])  # Create an empty dataframe with specified index
print(df_new)
df_new["X1"] = a1  
df_new["X2"] = a2  
df_new["X3"] = a3
print(df_new)

# Accessing columns
print(df_new.X1)
#Or 
#This is the most efficient way
print(df_new["X1"])
print(df_new[["X1", "X2"]])

# Accessing elements using ".iloc" : accessing each cell by row and column index values1
# iloc is calling using indexing
df_new.iloc[0:3, 1] # Column can be called with only index postion when we use iloc ,here 1 is column index position
df_new.iloc[:,:] # to get entire data frame 
# loc is via rows and column names
df_new.loc[101:103, ["X1", "X2"]] # column can be called with only names when we use loc , here [X1,X2]

# Statistics
df['X3'].mean()  # Calculate the mean of column 'X3'
df['X3'].median()  # Calculate the median of column 'X3'
df['X1'].mode()  # Calculate the mode of column 'X3'
df.describe()  # Generate descriptive statistics of the dataframe

# Merge operation using pandas
# It works like checks the common eliments in X1 and give only those rows
df1 = pd.DataFrame({"X1": [1, 2, 3], "X2": [4, 8, 12]})  # Creating DataFrame df1
df2 = pd.DataFrame({"X1": [1, 2, 3, 4], "X3": [14, 18, 112, 15]})  # Creating DataFrame df2
merge = pd.merge(df1, df2, on = "X1")  # Merge df1 and df2 on column 'X1'
print(merge)

# Replace index name
df = pd.DataFrame({"X1": [1, 2, 3], "X2": [4, 8, 12]})  # Creating DataFrame df
df
df.set_index("X1", inplace = True)  # Assigning index names using column 'X1'
df

# Change the column names 
df = pd.DataFrame({"X1": [1, 2, 3], "X2": [4, 8, 12]})  # Creating DataFrame df
df = df.rename(columns = {"X1":"X3","X2":"X4"})  # Renaming columns 'X1' to 'X3' and 'X2' to 'X4'
print(df)

Concatenate = pd.concat([df1, df2])  # Concatenating df1 and df2
print(Concatenate)


import numpy as np
import pandas as pd

# Creating DataFrame df with columns 'grade1' and 'grade2'
x1 = [1, 2, 3, 4, 5, np.nan]
x2 = [np.nan, 11, 12, 100, np.nan, 200] #np.nan is an empty value
df = pd.DataFrame()
df['grade1'] = x1
df['grade2'] = x2
print(df)

# Finding null values
df.isna().sum()  # Counting null values in each column
df.dropna()  # Dropping rows with null values

# WAYS OF CREATING DATAFRAMES
df = pd.DataFrame(
    {"a" : [4, 5, 6],
     "b" : [7, 8, 9],           
     "c" : [10, 11, 12]},
    index = [1, 2, 3])  # Creating DataFrame df using dictionary and specifying index
print(df)

# Another way to create DataFrame
df = pd.DataFrame(
    [[4, 7, 10],
     [5, 8, 11],
     [6, 9, 12]],
    index = [1, 2, 3],
    columns = ['a', 'b', 'c'])  # Creating DataFrame df using list of lists and specifying column names
print(df)

# Creating Series 'a', 'b', 'c'
a = pd.Series([50, 40, 34, 30, 22, 28, 17, 19, 20, 13, 9, 15, 10, 7, 3])
a.plot()  # Plotting Series 'a'
a.plot(figsize = (8, 6), color = 'green', title = 'line plot', fontsize = 12)  # Plotting Series 'a' with customizations
b = pd.Series([45, 22, 12, 9, 20, 34, 28, 19, 26, 38, 41, 24, 14, 32])
c = pd.Series([25, 38, 33, 38, 23, 12, 30, 37, 34, 22, 16, 24, 12, 9])
# Creating DataFrame 'd' with Series 'a', 'b', 'c'
d = pd.DataFrame({'a': a, 'b': b, 'c': c}, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(d)
d.plot.area(figsize = (9, 6), title = 'Area plot')  # Plotting area plot for DataFrame 'd'
d.plot.area(alpha = 0.4, color = ['coral', 'purple', 'lightgreen'], figsize = (8, 6), fontsize = 12)  # Plotting area plot with customizations


############## Reading External File ##############
import pandas as pd
help(pd.read_csv)
# Import data (.csv file) using pandas. We are using mba data set
mba = pd.read_csv(r"C:\Users\rahul\Downloads\Exploratory Data Analysis\Dataset\education.csv")
print(mba)
mba.groupby('gmat').count()  # Group 'mba' DataFrame by 'gmat' column and count occurrences of each value
mba.groupby('gmat').count()['datasrno']  # Group 'mba' DataFrame by 'gmat' column, count occurrences of each value, and then select 'datasrno' column
list(mba.groupby('gmat'))  # Convert the grouped DataFrame into a list
mba.groupby('gmat').sum().sort_values(by = 'workex')  # Group 'mba' DataFrame by 'gmat' column, sum the values for each group, and sort by 'workex' column
mba.groupby('gmat').sum().sort_values(by = 'workex', ascending = False)  # Group 'mba' DataFrame by 'gmat' column, sum the values for each group, and sort by 'workex' column in descending order
