import pandas as pd

data = {
    "Name": ["Rahul", "Jay", "Vijay", "Rohan", "Rohit"],
    "Salary": [50000, 60000, 70000, 80000, 65000],
    "Age": [25, 28, 30, 32, 28]
}

df = pd.DataFrame(data)
grouped = df.groupby('Age')['Salary'].sum()
print(grouped)