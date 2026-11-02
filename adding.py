import pandas as pd 

employee_data = {
    "Name":["Jay","Rahul","Jack","Vijay","Rohan","Suman","Mahi"],
    "Age":[25,28,31,27,39,51,19],
    "Salary":[50000, 700000, 800000, 70000, 49500, 250000, 82000],
    "Performence":[78,84,90,75,82,89,95]
}

df = pd.DataFrame(employee_data)
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

df.insert(0, "Employee_id", [10,20,30,40,50,60,70])
print(df)