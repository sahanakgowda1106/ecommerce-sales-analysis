import pandas as pd
import numpy as np

np.random.seed(42)

n = 1200

data = {
    "Order ID": np.arange(1001, 1001+n),
    "Order Date": pd.date_range(start="2022-01-01", periods=n, freq='D'),
    "Ship Date": pd.date_range(start="2022-01-03", periods=n, freq='D'),
    "Country": np.random.choice(["India", "USA", "UK", "Canada", "Australia"], n),
    "Segment": np.random.choice(["Consumer", "Corporate", "Home Office"], n),
    "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Printer", "Accessories"], n),
    "Sales": np.round(np.random.uniform(100, 5000, n), 2),
    "Profit": np.round(np.random.uniform(-500, 1500, n), 2),
    "Discount": np.round(np.random.uniform(0, 0.5, n), 2),
    "Quantity": np.random.randint(1, 10, n)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("ecommerce_sales_data.csv", index=False)

print("Dataset created successfully!")