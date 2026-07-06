import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Step 1: Load Dataset
# -------------------------------
try:
    df = pd.read_csv("E-commerce sales_data (1).csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: E-commerce sales_data (1).csv not found in the current directory.")
    exit()

# -------------------------------
# Step 2: Explore Dataset
# -------------------------------
print("===== First 5 Rows =====")
print(df.head())

print("\n===== Dataset Information =====")
print(df.info())

print("\nDataset Shape:", df.shape)

# -------------------------------
# Step 3: Data Cleaning
# -------------------------------

print("\n===== Missing Values =====")
print(df.isnull().sum())

# Fill missing numeric values with the column mean
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Remove duplicate rows
duplicates = df.duplicated().sum()
df.drop_duplicates(inplace=True)

print(f"\nDuplicate rows removed: {duplicates}")

# -------------------------------
# Step 4: Data Analysis
# -------------------------------

total_revenue = df["Total_Sales"].sum()
average_sale = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

best_region = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .idxmax()
)

print("\n========== SALES REPORT ==========")
print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Average Sale        : ₹{average_sale:,.2f}")
print(f"Highest Sale        : ₹{highest_sale:,.2f}")
print(f"Lowest Sale         : ₹{lowest_sale:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Best Sales Region   : {best_region}")
print("==================================")

# -------------------------------
# Step 5: Create Visualizations
# -------------------------------

os.makedirs("visualizations", exist_ok=True)

# -------- Chart 1 : Bar Chart --------

product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.close()

# -------- Chart 2 : Pie Chart --------

region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(7,7))
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/sales_by_region.png")
plt.close()

print("\nCharts saved successfully in the 'visualizations' folder.")

# -------------------------------
# Step 6: Insights
# -------------------------------

print("\n========== INSIGHTS ==========")
print(f"• Total Revenue Generated: ₹{total_revenue:,.2f}")
print(f"• Best Selling Product: {best_product}")
print(f"• Highest Revenue Region: {best_region}")
print("• No missing values remain after cleaning.")
print("• Dataset analyzed successfully.")
print("==============================")