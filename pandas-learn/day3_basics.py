import pandas as pd

employees = [
[1,'Rahul'],
[2,'Ankit'],
[3,'Neha']
]

salaries = [
[1,40000],
[2,50000],
[3,60000]
]

df1 = pd.DataFrame(employees, columns=['EmpId', 'Name'])
df2 = pd.DataFrame(salaries, columns=['EmpId', 'Salary'])

mergedf = pd.merge(df1, df2, on='EmpId', how='outer')
# print(mergedf)

mergedf['Salary_Level'] = mergedf['Salary'].apply(lambda x: 'High' if x > 55000 else ('Low' if x < 45000 else 'Medium'))

print(mergedf)