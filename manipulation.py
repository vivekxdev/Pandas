import pandas as pd 

employee_data = {
    "Name":["Jay","Rahul","Jack","Vijay","Rohan","Suman","Mahi"],
    "Age":[25,28,31,27,39,51,19],
    "Salary":[50000, 700000, 800000, 70000, 49500, 250000, 82000],
    "Performence":[78,84,90,75,82,89,95]
}

df = pd.DataFrame(employee_data)
print("Sample_dataframe:")
print(df)

print("Names (Single column return series: )")
name = df['Name']
print(name)

subset = df[["Name", "Salary"]]
print('\nSubset with Name and salary:')
print(subset)

high_salary = df[df['Salary'] > 50000]
print('Employee with salary > 50000')
print(high_salary)                                          

filtered = df[(df['Age'] > 30 ) & (df['Salary'] > 50000)]
print(f"Employee list Age > 30 + Salary > 50000")
print(filtered)