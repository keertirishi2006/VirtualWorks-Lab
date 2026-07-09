import pandas as pd

df = pd.read_csv("website_traffic.csv")

print("Dataset Shape")
print(df.shape)

print("\nTotal Page Views")
print(df["PageViews"].sum())

print("\nAverage Session Duration")
print(df["SessionDuration"].mean())

print("\nAverage Bounce Rate")
print(df["BounceRate"].mean())

print("\nMost Visited Page")
print(df.groupby("Page")["PageViews"].sum().sort_values(ascending=False))