"""Asir Tourism Analysis
Uses published figures (see source column in the CSV) to show
where Asir's visitors come from and how big Asir is nationally.

Usage: python analysis.py
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("asir_tourism_data.csv")
os.makedirs("charts", exist_ok=True)


def get(indicator, year):
    row = df[(df["indicator"] == indicator) & (df["year"] == year)]
    return float(row["value"].iloc[0])


# 1) Where do Asir's visitors come from? (2023)
gcc = get("GCC visitors share", 2023)
mideast = get("Rest of Middle East visitors share", 2023)
other = round(100 - gcc - mideast, 2)  # calculated

plt.bar(["GCC", "Rest of Middle East", "Other (calculated)"], [gcc, mideast, other])
plt.title("Asir Visitors by Origin, 2023 (%)")
plt.ylabel("Share of visitors (%)")
plt.xticks(rotation=15)
plt.savefig("charts/visitor_origin.png", bbox_inches="tight")
plt.close()

# 2) Asir's share of all tourists in the Kingdom (2024)
asir = get("Asir tourists", 2024)
kingdom = get("Kingdom total tourists", 2024)
share = asir / kingdom * 100

plt.pie([asir, kingdom - asir], labels=["Asir", "Rest of Kingdom"], autopct="%1.1f%%")
plt.title("Asir Share of Kingdom Tourists, 2024")
plt.savefig("charts/asir_share.png", bbox_inches="tight")
plt.close()

# Kingdom growth
growth = (kingdom / get("Kingdom total tourists", 2023) - 1) * 100

print("Key insights:")
print(f"- Asir received about {asir} million tourists in 2024 ({share:.1f}% of the Kingdom).")
print(f"- {gcc:.0f}% of Asir visitors in 2023 came from GCC countries.")
print(f"- Kingdom tourists grew about {growth:.1f}% from 2023 to 2024.")
print("Charts saved in the 'charts' folder.")
