import pandas as pd

df = pd.read_csv("amazon_laptop_cleaned.csv")

print("\nHighest Average Price Brand:")
print(df.groupby("Brand")["Price"].mean().sort_values(ascending=False).head(1))

print("\nHighest Average Rating Brand:")
print(df.groupby("Brand")["Rating"].mean().sort_values(ascending=False).head(1))

print("\nTop 5 Highest Rated Laptops:")
print(df.sort_values("Rating", ascending=False).head(5)[["Title","Rating"]])

print("\nPrice vs Rating Correlation:")
print(df["Price"].corr(df["Rating"]))

print("\nRAM Distribution:")
print(df["RAM"].value_counts())

print("\nMost Common Screen Size:")
print(df["Screen"].value_counts().head(1))

print("\nLaptops under ₹50,000:")
print(df[df["Price"] < 50000].shape[0])
