import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_dashboard.csv")

print(df)

# Sales Trend
plt.figure(figsize=(8,4))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()

# Profit Trend
plt.figure(figsize=(8,4))
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("profit_chart.png")
plt.show()

# Customers
plt.figure(figsize=(8,4))
plt.plot(df["Month"], df["Customers"], marker="s")
plt.title("Customer Growth")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("customer_growth.png")
plt.show()