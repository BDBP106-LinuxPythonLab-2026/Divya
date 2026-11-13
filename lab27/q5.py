import pandas as pd

df = pd.read_csv('diabetes.csv')
print(df.columns.tolist())

print(df.head(10))

print(df["Blood Pressure"].mean())

print(df.iloc[:4,2:5])

