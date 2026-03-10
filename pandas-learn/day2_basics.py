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
# pd.merge(left_df, right_df, on='column_name')
empdf = pd.DataFrame(employees, columns=['EmpId', 'Name'])

salarydf = pd.DataFrame(salaries, columns=['EmpId', 'Salary'])

# df = pd.merge(empdf, salarydf, on='EmpId')

# inner join return only matching rows
df =  pd.merge(empdf, salarydf, on='EmpId', how='inner')

#left join keep all rows from left table
df =  pd.merge(empdf, salarydf, on='EmpId', how='left')

#right join keep all rows from right table
df =  pd.merge(empdf, salarydf, on='EmpId', how='right')

#outer join keep all rows from both table
df =  pd.merge(empdf, salarydf, on='EmpId', how='outer')

print(df)