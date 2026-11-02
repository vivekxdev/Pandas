import pandas as pd 
import json

with open("employees_large_sample.json", "r") as file:
    data = json.load(file)
print(type(data))
print(data)

df = pd.read_json("employees_large_sample.json")

print("First 5 Rows:")
print(df.head(5))

print("\n last 5 Rows:")
print(df.tail(5))
