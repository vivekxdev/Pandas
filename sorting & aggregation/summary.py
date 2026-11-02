import pandas as pd

data = {
    "Name": ["Rahul", "Jay", "Vijay", "Rohan"],
    "Salary": [50000, 60000, 70000, 80000],
    "Age": [25, 28, 30, 32]
}

df = pd.DataFrame(data)


avg_salary = df["Salary"].mean()

print(df)
print("Average Salary:", avg_salary)

min_age = df["Age"].min()
print("Min age:", min_age)


max_age = df["Age"].max()
print("Max age:", max_age)
