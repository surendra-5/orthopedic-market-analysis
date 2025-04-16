import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set chart style
sns.set(style="whitegrid")

# Step 1: Define years and companies
years = list(range(2019, 2027))
companies = ["Stryker", "Zimmer Biomet", "Medtronic", "Smith & Nephew"]

# Step 2: Set base revenues and CAGR per company
base_revenues = {
    "Stryker": 4000,
    "Zimmer Biomet": 3500,
    "Medtronic": 4500,
    "Smith & Nephew": 3000
}
cagr = {
    "Stryker": 0.06,
    "Zimmer Biomet": 0.055,
    "Medtronic": 0.05,
    "Smith & Nephew": 0.045
}

# Step 3: Generate revenue forecast data (2019–2026)
data = {"Year": years}
for company in companies:
    revenue_list = [base_revenues[company]]
    for _ in range(1, len(years)):
        revenue_list.append(round(revenue_list[-1] * (1 + cagr[company]), 2))
    data[company] = revenue_list

df = pd.DataFrame(data)

# Step 4: Plot Revenue Growth Over Time (Line Chart)
df_melted = df.melt(id_vars="Year", var_name="Company", value_name="Revenue")

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x="Year", y="Revenue", hue="Company", marker="o")
plt.title("Revenue Growth of Orthopedic Device Companies (2019–2026)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Revenue (in Million USD)")
plt.xticks(df["Year"])
plt.legend(title="Company")
plt.tight_layout()
plt.show()
plt.savefig("charts/filename.png")
plt.close()

# Step 5: Projected Revenue in 2026 (Bar Chart)
revenue_2026 = df[df["Year"] == 2026].melt(id_vars="Year", var_name="Company", value_name="Revenue")

plt.figure(figsize=(8, 5))
sns.barplot(data=revenue_2026, x="Revenue", y="Company", palette="pastel")
plt.title("Projected Revenue by Company in 2026", fontsize=14)
plt.xlabel("Revenue (in Million USD)")
plt.ylabel("Company")
plt.tight_layout()
plt.show()
plt.savefig("charts/filename.png")
plt.close()


# Step 6: Calculate CAGR from 2019 to 2023
cagr_values = {}
for company in companies:
    start_val = df[df["Year"] == 2019][company].values[0]
    end_val = df[df["Year"] == 2023][company].values[0]
    num_years = 2023 - 2019
    cagr_calc = ((end_val / start_val) ** (1 / num_years)) - 1
    cagr_values[company] = round(cagr_calc * 100, 2)  # in %

cagr_df = pd.DataFrame({
    "Company": list(cagr_values.keys()),
    "CAGR (%)": list(cagr_values.values())
}).sort_values("CAGR (%)", ascending=False)

# Step 7: Plot CAGR Comparison (Bar Chart)
plt.figure(figsize=(8, 5))
sns.barplot(data=cagr_df, x="CAGR (%)", y="Company", palette="deep")
plt.title("Compound Annual Growth Rate (2019–2023)", fontsize=14)
plt.xlabel("CAGR (%)")
plt.ylabel("Company")
plt.tight_layout()
plt.show()
plt.savefig("charts/filename.png")
plt.close()

