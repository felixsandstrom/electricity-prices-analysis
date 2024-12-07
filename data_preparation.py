import os
import pandas as pd

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "electricity_prices_norway_raw.csv")

# Read the raw CSV file with utf-8-sig encoding for proper character handling
df = pd.read_csv(file_path, encoding="utf-8-sig")

# Rename columns for consistency and readability
df.columns = ["Måned", "Sone", "2024", "2023", "2022", "2021", "2020", "2019"]

# Transform data from wide format (years as columns) to long format (years as rows)
df_long = pd.melt(df, id_vars=["Måned", "Sone"], 
                  value_vars=["2024", "2023", "2022", "2021", "2020", "2019"], 
                  var_name="Year", value_name="Price")

# Combine year and month into a single Date column and convert to datetime format
df_long["Date"] = pd.to_datetime(df_long["Year"] + "-" + df_long["Måned"], format="%Y-%B", errors="coerce")

# Remove rows with invalid dates and drop redundant columns
df_long = df_long.dropna(subset=["Date"]).drop(columns=["Måned", "Year"])

# Convert Price column to numeric, handling any non-numeric values
df_long["Price"] = pd.to_numeric(df_long["Price"], errors="coerce")

# Drop rows with missing prices
df_long = df_long.dropna(subset=["Price"])

# Pivot data to have one column per Sone, with prices as values
df_pivoted = df_long.pivot(index="Date", columns="Sone", values="Price").reset_index()

# Save the cleaned and transformed data to a new CSV file
output_file_path = os.path.join(script_dir, "electricity_prices_norway_processed.csv")
df_pivoted.to_csv(output_file_path, index=False, encoding="utf-8-sig")

# Print confirmation message
print(f"Processed data saved to {output_file_path}")
