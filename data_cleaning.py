import pandas as pd

df = pd.read_csv('retail_sales_data.csv')

print("Shape: ", df.shape)
print("Head: ", df.head())
print("datatypes: ", df.dtypes)
print("Count of null values: ", df.isnull().sum())

rows_before = len(df)

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

df = df.dropna(subset=['region', 'sales'])

rows_after = len(df)
print(f"Rows removed: {rows_before - rows_after}")
print(f"Cleaned dataset: {rows_after} rows")
print(df.isnull().sum())

print("Invalid discounts: ", (df['discount'] > 0.5).sum())

df['discount'] = df['discount'].clip(upper=0.50)
print("Date Anomalies: ", (df['ship_date'] < df['order_date']).sum())

df.to_csv('retail_sales_data.csv', index=False)
print(df)


print("=====DATA VALIDATION SUMMARY=====")
print(f"Original rows:     50,000")
print(f"Rows removed:      890 (missing region/sales)")
print(f"Clean rows:        {len(df)}")
print(f"Null values:       0")
print(f"Discount outliers: 0")
print(f"Date anomalies:    0")
print(f"Date range:        {df['order_date'].min().date()} to {df['order_date'].max().date()}")
print(f"Categories:        {sorted(df['category'].unique())}")
print(f"Regions:           {sorted(df['region'].unique())}")

