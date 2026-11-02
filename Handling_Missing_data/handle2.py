import pandas as pd 

employee_data = {
    "Name":["Jay","Rahul","None","Vijay","Rohan","Suman","Mahi"],
    "Age":[25,28,None,27,39,51,19],
    "Salary":[50000, 700000, None, 70000, 49500, 250000, 82000],
    "Performence":[78,84,None,75,82,89,95]
}

df = pd.DataFrame(employee_data)
print(df)

df.fillna(0, inplace=True)
print(df)


df['Age'].fillna(df['Age'].mean())
print(df)

