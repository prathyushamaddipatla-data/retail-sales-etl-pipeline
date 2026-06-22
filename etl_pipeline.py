import pandas as pd

# Read dataset
df = pd.read_csv("Sales Dataset.csv")

# Show number of rows and columns
print("Dataset Shape:")
print(df.shape)

# Show column names
print("\nColumns:")
print(df.columns)

# Remove unwanted index column
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

print("\nDataset cleaned successfully!")
print("\nRevenue by Product Category:")

category_sales = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)
