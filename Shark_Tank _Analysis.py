import pandas as pd

df = pd.read_csv("Shark Tank India Dataset.csv")
print(df)

print(df.head())

# Check the number of rows and columns 
print(df.shape)

# See all column names
print(df.columns)

# Check the missing values
print(df.isnull().sum())

# To check duplicate 
print(df.duplicated().sum())

# Check the deal column
print(df["deal"].value_counts())

# Create a readable Deal Status
df["Deal_Status"] = df["deal"].map({
    1: "Deal",
    0: "No Deal"
})

print(df[["brand_name", "deal", "Deal_Status"]].head(10))

# Calculate Deal Success Rate
Deal_rate =df["deal"].mean() * 100
print("Deal Success rate: ", round(Deal_rate ,2), "%")

# Look at investment amounts
print(df["deal_amount"].describe())

# Find total investment
Total_Investment=df["deal_amount"].sum()
print("Total_Investment :",Total_Investment)

# Find average investment
Average_Investment=df["deal_amount"].mean()
print("Average Investment :",Average_Investment)

# Find median investment
Median_Investment=df["deal_amount"].median()
print("Median_Investment :",Median_Investment)

Top_deals =df.sort_values(
    by="deal_amount",
    ascending=False
)
print(Top_deals[[
    "brand_name",
    "idea",
    "deal_amount",
    "deal_equity"
]].head(10))

# Checking important Numeric column
print(df[[
    "pitcher_ask_amount",
    "ask_equity",
    "ask_valuation",
    "deal_amount",
    "deal_equity",
    "deal_valuation"
]].describe())

# Checking the values zeros
print((df[[
    "pitcher_ask_amount",
    "ask_equity",
    "ask_valuation",
    "deal_amount",
    "deal_equity",
    "deal_valuation"
]] == 0).sum())


# Create Industry
def classify_industry(idea):

    idea = idea.lower()

    if any(word in idea for word in [
        "food", "momo", "pickle", "snack", "drink",
        "beverage", "chocolate", "ice cream", "coffee"
    ]):
        return "Food & Beverage"

    elif any(word in idea for word in [
        "skin", "beauty", "cosmetic", "makeup", "hair"
    ]):
        return "Beauty & Personal Care"

    elif any(word in idea for word in [
        "app", "software", "tech", "technology", "digital"
    ]):
        return "Technology"

    elif any(word in idea for word in [
        "bike", "vehicle", "car", "mobility"
    ]):
        return "Transportation"

    elif any(word in idea for word in [
        "education", "learning", "student", "school", "child"
    ]):
        return "Education"

    elif any(word in idea for word in [
        "travel", "tourism", "hotel"
    ]):
        return "Travel & Tourism"

    else:
        return "Other"


df["Industry"] = df["idea"].apply(classify_industry)

print(df[[
    "brand_name",
    "idea",
    "Industry"
]].head(50))

# Check our new industries
print(df["Industry"].value_counts())

# Industry-wise investment
industry_investment = df.groupby("Industry")["deal_amount"].sum()
print(industry_investment.sort_values(ascending=False))

# Industry-wise number of deals
Industry_deals=df.groupby("Industry")["deal"].sum()
print(Industry_deals.sort_values(ascending=False))

# Industry deal success rate
industry_success = df.groupby("Industry")["deal"].mean() * 100
print(industry_success.sort_values(ascending=False))

# Analyze individual Sharks
shark_columns = [
    col for col in df.columns
    if "shark" in col.lower() or "deal" in col.lower()
]
print(shark_columns)


# Find how many deals each Shark made
shark_deal_columns = [
    col for col in df.columns
    if col.endswith("_deal")
]
print(shark_deal_columns)
shark_deals = {}

for col in shark_deal_columns:
    shark_name = col.replace("_deal", "").title()
    shark_deals[shark_name] = df[col].sum()

print(shark_deals)

# Convert it into a DataFrame
shark_deals_df = pd.DataFrame(
    list(shark_deals.items()),
    columns=["Shark", "Deals"]
)

print(shark_deals_df)

# Find the most active Shark
top_shark = shark_deals_df.iloc[0]

print("Most Active Shark:", top_shark["Shark"])
print("Number of Deals:", top_shark["Deals"])

# Create a Shark bar chart
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

plt.bar(
    shark_deals_df["Shark"],
    shark_deals_df["Deals"]
)

plt.title("Number of Deals by Shark")
plt.xlabel("Shark")
plt.ylabel("Number of Deals")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Save the chart
plt.savefig("shark_deals.png", dpi=300, bbox_inches="tight")

df.to_csv("SharkTank_Cleaned.csv", index=False)