import pandas as pd

df = pd.read_csv("Sales Dataset.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.info())
