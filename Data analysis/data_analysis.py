import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

top_product = df.loc[df["Sales"].idxmax(), "Product"]
highest_profit = df.loc[df["Profit"].idxmax(), "Product"]
best_category = (
    df.groupby("Category")["Sales"]
      .sum()
      .idxmax()
)

print("Top Sales Product:", top_product)
print("Highest Profit Product:", highest_profit)
print("Best Category:", best_category)

# Visual chart
category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(3,3))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    explode=[0.1, 0, 0],  # highlight best category
    shadow=True,
    startangle=90,
    textprops={"fontsize": 6}
)

plt.title("Sales Contribution by Category")

plt.tight_layout()
plt.savefig("sales_chart.png", dpi=300)


