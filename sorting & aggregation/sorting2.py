import pandas as pd

data = {
    "Name":["Arun","Varun","Tarun"],
    "Age":[28,22,34],
    "Salary":[20000,25000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by=['Age', 'Salary'], ascending=[True,True], inplace=True)
print('Sorted Age by descending:')
print(df)