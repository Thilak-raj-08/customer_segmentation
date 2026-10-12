import pandas as pd

df = pd.read_csv("customer_data.csv")
print("Shape :", df.shape)
print("Data Types :", df.dtypes)
print(df.head(5))

print()
age_mask = df["Age"] > 40
above_40_customers = df[age_mask]
print(above_40_customers.head(5))
print(len(above_40_customers))

print()
high_income_mask = df["Income"] > 100000
high_income_customers = df[high_income_mask]
print(high_income_customers.head(5))
print(len(high_income_customers))

print()
high_spending_mask  = df["Purchase_Amount"] > 50000
high_spending_customers = df[high_spending_mask]
print(high_spending_customers.head(5))
print(len(high_spending_customers))

print()
colombo_mask = df["City"] == "Colombo"
colombo_customers = df[colombo_mask]
print(colombo_customers.head(5))
print(len(colombo_customers))

print()
both_mask = high_income_mask & high_spending_mask
high_income_high_spending_customers = df[both_mask]
print(high_income_high_spending_customers.head(5))
print(len(high_income_high_spending_customers))

print()
no_purchase_mask = df["Purchase_Amount"] == 0
no_purchase_customers = df[no_purchase_mask]
print(no_purchase_customers.head(5))
print(len(no_purchase_customers))

print()
def classify_customer(amount):
    if amount > 50000:
        return "Premium"
    elif amount >= 10000:
        return "Regular"
    else:
        return "Low Value"

df["Customer_Category"] = df["Purchase_Amount"].apply(classify_customer)
print(df[["Customer_ID", "Purchase_Amount", "Customer_Category"]].head(10))

print()
category_counts = df["Customer_Category"].value_counts()
print(category_counts)
print("Total Customers:", category_counts.sum())
df.to_csv("customers_segmented.csv", index=False)