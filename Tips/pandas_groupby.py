import pandas as pd

sales_data = [
    {'product': 'Laptop', 'region': 'North', 'revenue': 1200},
    {'product': 'Phone', 'region': 'South', 'revenue': 800},
    {'product': 'Laptop', 'region': 'East', 'revenue': 1500},
    {'product': 'Tablet', 'region': 'North', 'revenue': 300},
    {'product': 'Phone', 'region': 'West', 'revenue': 900},
    {'product': 'Tablet', 'region': 'South', 'revenue': 400}
]

# The 10-line vanilla Python approach
total_revenue_by_product = {}

for row in sales_data:
    product = row['product']
    revenue = row['revenue']
    
    # Check if we've seen this product before
    if product in total_revenue_by_product:
        total_revenue_by_product[product] += revenue
    else:
        # If it's a new product, initialize it
        total_revenue_by_product[product] = revenue

print(total_revenue_by_product)
# Output: {'Laptop': 2700, 'Phone': 1700, 'Tablet': 700}

# Assume we loaded our data into a DataFrame
df = pd.DataFrame(sales_data)

# The 1-line Pandas approach
total_revenue = df.groupby('product')['revenue'].sum()

print(total_revenue)