import os
import pandas as pd

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the CSV file
relative_path = "electricity_prices_norway_raw.csv"  # Replace this with the actual relative path
file_path = os.path.join(script_dir, relative_path)

# Read the CSV file
df = pd.read_csv(file_path, encoding="latin1")

# Rename columns for clarity
df.columns = ["Måned", "Sone", "2024", "2023", "2022", "2021", "2020", "2019"]

# Convert the wide format to long format
df_long = pd.melt(
    df,
    id_vars=["Måned", "Sone"],  # Keep Måned and Sone as identifiers
    value_vars=["2024", "2023", "2022", "2021", "2020", "2019"],  # Years as values
    var_name="Year",  # New column for years
    value_name="Price"  # New column for prices
)

# Ensure the Måned column can be properly merged with Year into a valid date
month_translation = {
    "Januar": "January", "Februar": "February", "Mars": "March", 
    "April": "April", "Mai": "May", "Juni": "June", 
    "Juli": "July", "August": "August", "September": "September",
    "Oktober": "October", "November": "November", "Desember": "December"
}
df_long["Måned"] = df_long["Måned"].map(month_translation)

# Combine Måned and Year into a single Date column and convert to datetime
df_long["Date"] = pd.to_datetime(df_long["Year"] + "-" + df_long["Måned"], format="%Y-%B", errors="coerce")

# Keep rows with valid dates
df_long = df_long[~df_long["Date"].isna()]

# Convert Price to numeric, keeping missing values as NaN
df_long["Price"] = pd.to_numeric(df_long["Price"], errors="coerce")

# Pivot the data so each Sone becomes a column
df_pivoted = df_long.pivot(index="Date", columns="Sone", values="Price")

# Reset the index to include Date as a column
df_pivoted.reset_index(inplace=True)

# Save the pivoted data to a new CSV file in the same directory as the original file
output_file_path = os.path.join(script_dir, "electricity_prices_norway_processed.csv")
df_pivoted.to_csv(output_file_path, index=False, encoding="utf-8")

print(f"Pivoted data saved to {output_file_path}")
