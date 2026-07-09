import pandas as pd

df = pd.read_csv("sales_locations.csv")

print("Dataset Shape")
print(df.shape)

print("\nTotal Sales")
print(df["Sales"].sum())

print("\nHighest Sales City")
print(df.loc[df["Sales"].idxmax()])

print("\nAverage Sales")
print(df["Sales"].mean())

print("\nTop 5 Cities")
print(df.sort_values("Sales", ascending=False).head())