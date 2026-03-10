import pandas as pd

# data = {
#     "Name": ["John", "Sam", "Alex"],
#     "Age": [25, 30, 35],
#     "Salary": [50000, 60000, 80000]
# }

# df = pd.DataFrame(data)

# print(df)

# print(df.head(2))
# print(df.tail(2))

# print(df.info())

# print(df.describe())

# print(df['Age'])

# print(df[['Name','Salary']])

# print(df[df['Age'] > 28])

# df['Bonus'] = df['Salary']*0.25

# print(df)

# x = df[['Age', 'Salary']].values
# y = df['Bonus'].values

# print(x)
# print(y)

data = [
['Rahul','IT',40000],
['Ankit','HR',50000],
['Neha','IT',60000],
['Pooja','HR',55000],
['Rohit','IT',45000]
]

df = pd.DataFrame(data, columns=['Name', 'Department', 'Salary']) # create dataframe

# print(df)

# print(df[:2]) # first two rows

# print(df['Age']) # only age col

# print(df[df['Salary'] > 55000])

# df['Tax'] = df['Salary'] * 0.2




# print(df.groupby('Department')['Salary'].agg(['mean','max','min','count']))




