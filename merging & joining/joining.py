import pandas as pd

employees = pd.DataFrame({
    "Employee": ["Rahul", "Jay", "Vijay"]
})

projects = pd.DataFrame({
    "Project": ["Website", "Mobile App"]
})

result = pd.merge(employees, projects, how="cross")

print(result)