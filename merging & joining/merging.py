import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID':[1,2,3,4],
    'Name':['Ramesh','Suresh','Varun','Kerry']
})

df_orders = pd.DataFrame({
    'CustomerID':[1,2,3,5],
    'OrderAmount':[250,150,200,350]
})

df_merged = pd.merge(df_customers,df_orders, on="CustomerID", how='inner')
print('inner join:')

print(df_merged)


df_merged = pd.merge(df_customers,df_orders, on="CustomerID", how='outer')
print('outer join:')

print(df_merged)


df_merged = pd.merge(df_customers,df_orders, on="CustomerID", how='left')
print('left join:')

print(df_merged)