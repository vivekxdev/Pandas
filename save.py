import pandas as pd

data = {
    "name":["Rahul","Ajay","Vijay"],
    "age":[22, 28, 31],
    "city":["Mumabai","Delhi","Noida"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("Output.csv", index=False)
df.to_excel("Output.xlsx", index=False)
df.to_json("Output.json", index=False)