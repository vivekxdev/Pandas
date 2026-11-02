# Row-wise concatenation (axis=0)
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Rahul", "Jay"],
    "Age": [25, 28]
})

df2 = pd.DataFrame({
    "Name": ["Vijay", "Rohan"],
    "Age": [30, 32]
})

result = pd.concat([df1, df2], axis=0)

print(result)






# Column-wise concatenation (axis=1)
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Rahul", "Jay", "Vijay"]
})

df2 = pd.DataFrame({
    "Salary": [50000, 60000, 70000]
})

result = pd.concat([df1, df2], axis=1)

print(result)











# Important parameters of pd.concat()
# Parameter	                  Purpose
# objs	                      DataFrames or Series to combine
# axis=0	                  Combine rows vertically
# axis=1	                  Combine columns horizontally
# ignore_index=True	          Reset the resulting index
# join="outer"	              Keep all columns (default)
# join="inner"	              Keep only common columns