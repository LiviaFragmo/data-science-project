import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--data", help="Optional local course CSV; otherwise download from IBM")
parser.add_argument("--output-dir", default="laptop-results")
args = parser.parse_args()
out = Path(args.output_dir)
out.mkdir(parents=True, exist_ok=True)
chart_number = 0

def save_chart():
    global chart_number
    chart_number += 1
    plt.savefig(out / f"chart-{chart_number}.png", dpi=150, bbox_inches="tight")
    plt.close()

import matplotlib
matplotlib.use("Agg")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
df = pd.read_csv(args.data or DATA_URL)
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])
pd.set_option("display.max_columns", None)
print("Dataset loaded successfully.")
print("Shape:", df.shape)
df.head()

laptop_df = df.copy()

laptop_df["Screen_Size_cm"] = pd.to_numeric(laptop_df["Screen_Size_cm"], errors="coerce")
laptop_df["Weight_kg"] = pd.to_numeric(laptop_df["Weight_kg"], errors="coerce")

laptop_df["Weight_kg"] = laptop_df["Weight_kg"].fillna(laptop_df["Weight_kg"].mean())
laptop_df["Screen_Size_cm"] = laptop_df["Screen_Size_cm"].fillna(laptop_df["Screen_Size_cm"].mode()[0])

laptop_df["Screen_Size_inch"] = laptop_df["Screen_Size_cm"] / 2.54
laptop_df["Weight_pounds"] = laptop_df["Weight_kg"] * 2.205
laptop_df["CPU_frequency"] = laptop_df["CPU_frequency"] / laptop_df["CPU_frequency"].max()

bins = np.linspace(laptop_df["Price"].min(), laptop_df["Price"].max(), 4)
labels = ["Low", "Medium", "High"]
laptop_df["Price-binned"] = pd.cut(laptop_df["Price"], bins=bins, labels=labels, include_lowest=True)

screen_dummies = pd.get_dummies(laptop_df["Screen"], prefix="Screen")
laptop_df = pd.concat([laptop_df.drop(columns=["Screen"]), screen_dummies], axis=1)

print("Missing values after cleaning:")
print(laptop_df.isna().sum())
laptop_df.head()

plt.figure(figsize=(8, 5))
sns.histplot(laptop_df["Price"], kde=True, bins=20)
plt.title("Distribution of Laptop Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
save_chart()

print("Price skewness:", round(laptop_df["Price"].skew(), 3))

manufacturer_price = laptop_df.groupby("Manufacturer")["Price"].mean().sort_values(ascending=False)
print(manufacturer_price)

plt.figure(figsize=(10, 5))
manufacturer_price.plot(kind="bar")
plt.title("Average Laptop Price by Manufacturer")
plt.xlabel("Manufacturer")
plt.ylabel("Average price")
plt.xticks(rotation=45)
save_chart()

numeric_features = ["CPU_frequency", "RAM_GB", "Storage_GB_SSD", "CPU_core", "GPU", "OS", "Category", "Screen_Size_inch", "Weight_pounds"]

correlations = laptop_df[numeric_features + ["Price"]].corr()["Price"].sort_values(ascending=False)
print(correlations)

plt.figure(figsize=(8, 5))
sns.heatmap(laptop_df[numeric_features + ["Price"]].corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Matrix")
save_chart()

key_features = ["CPU_frequency", "RAM_GB", "CPU_core", "Storage_GB_SSD"]
fig, axes = plt.subplots(2, 2, figsize=(11, 8))

for axis, feature in zip(axes.ravel(), key_features):
    sns.regplot(data=laptop_df, x=feature, y="Price", ax=axis, scatter_kws={"alpha": 0.65})
    axis.set_title(f"Price vs {feature}")

plt.tight_layout()
save_chart()

from scipy import stats

groups = [group["Price"].values for _, group in laptop_df.groupby("Manufacturer") if len(group) > 1]
f_stat, p_value = stats.f_oneway(*groups)

print("ANOVA F-statistic:", round(f_stat, 4))
print("ANOVA p-value:", p_value)
if p_value < 0.05:
    print("Conclusion: Average prices differ significantly across manufacturers.")
else:
    print("Conclusion: No statistically significant average price difference was detected.")
import json
summary = {"rows": len(laptop_df), "missing_values_after_cleaning": int(laptop_df.isna().sum().sum()), "price_skewness": float(laptop_df["Price"].skew()), "ram_price_correlation": float(correlations["RAM_GB"]), "anova_f": float(f_stat), "anova_p": float(p_value), "charts": chart_number}
(out / "results.json").write_text(json.dumps(summary, indent=2))
print("Artifacts saved:", out)
