import pandas as pd

# Load dataset
df = pd.read_csv("customer_churn.csv")

print("Dataset Shape:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nChurn Count")
print(df["Churn"].value_counts())

print("\nAverage Monthly Charges")
print(df.groupby("Churn")["MonthlyCharges"].mean())

print("\nContract Type")
print(df.groupby("Contract")["Churn"].value_counts())