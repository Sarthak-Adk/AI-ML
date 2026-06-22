import pandas as pd

data = {
        'Name':['sarthak','sagar','prajon','ritik'],
        'Age':[22,23,22,None],
        'Salary':[50000,4000,None,None]
}

# reading data from sample file
sample_data = pd.read_csv('sample_data.csv')

print(sample_data)

df = pd.DataFrame(data)
print("Original DataFrame")
print(df)

# to watch the number of null data
# print(df.isnull().sum())

# to drop the data 
# df_drop = df.dropna()
# print(df_drop)

#to fill data
df['Age'] = df['Age'].fillna(df['Age'].mean()) 
df['Salary'] = df['Salary'].fillna(df['Salary'].mean()) 
print("\n updated data \n")
print(df)

# checking the missing value 

print(df.isnull().mean()*100)