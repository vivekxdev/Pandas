import pandas as pd 

employee_data = {
    "Name":["Jay","Rahul","Jack","Vijay","Rohan","Suman","Mahi"],
    "Age":[25,28,31,27,39,51,19],
    "Salary":[50000, 700000, 800000, 70000, 49500, 250000, 82000],
    "Performence":[78,84,90,75,82,89,95]
}

df = pd.DataFrame(employee_data)
print(df)

df.loc[4, "Salary"] = 52000
print(df)

df.loc[3, "Name"] = "Ajay"
print(df)