import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("house_rent_data.csv")

print(df.head())
print("Average Rent:", df["Rent_INR"].mean())

# Bar chart
df.groupby("Location")["Rent_INR"].mean().plot(kind="bar")
plt.title("Average Rent by Location")
plt.show()

# Scatter plot
plt.scatter(df["Size_sqft"], df["Rent_INR"])
plt.xlabel("Size")
plt.ylabel("Rent")
plt.show()

# # Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()