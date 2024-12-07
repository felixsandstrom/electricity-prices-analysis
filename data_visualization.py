import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from PIL import Image

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the CSV file
relative_path = "electricity_prices_norway_processed.csv"  # Replace with the actual filename
file_path = os.path.join(script_dir, relative_path)

# Read the CSV file
df = pd.read_csv(file_path, encoding="utf-8-sig")

# Ensure the Date column is a datetime object
df["Date"] = pd.to_datetime(df["Date"])

# Set the Date as the index for plotting
df.set_index("Date", inplace=True)

# Plotting
plt.figure(figsize=(10, 5))  # Adjusted figure size
colors = plt.cm.tab10.colors  # Use a colormap for lines

# Plot each Sone as a separate line
for idx, column in enumerate(df.columns):
    plt.plot(
        df.index,  # Date on x-axis
        df[column],  # Prices on y-axis
        marker="o",
        label=column,  # Use column name (Sone) as the label
        linewidth=2,  # Thicker lines for better visibility
        color=colors[idx % len(colors)],  # Cycle through colors
        alpha=0.85  # Slight transparency for a polished look
    )

# Format y-axis as currency (øre)
plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f øre'))

# Add a grid with lighter lines
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Customize the plot
plt.title("Strømpriser per sone over tid", fontsize=15, weight='semibold', color='#1a1a1a', pad=20)
plt.xlabel("Dato", fontsize=13)
plt.ylabel("Øre/kWh, inkl. mva", fontsize=13)
plt.xticks(fontsize=11, rotation=45, ha="right")
plt.yticks(fontsize=11)

# Add a legend with a transparent background inside the plot
plt.legend(
    title="Sone",
    fontsize=10,
    loc="upper left",
    bbox_to_anchor=(0.02, 0.98),
    framealpha=0.9  # Slightly transparent background
)

# Adjust margins to make the left and right margins uniform
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.2)

# Save the plot as a PNG file
output_png_path = os.path.join(script_dir, "electricity_prices_plot.png")
plt.savefig(output_png_path, format="png", dpi=150)

# Convert the PNG to WebP using Pillow
output_webp_path = os.path.join(script_dir, "electricity_prices_plot.webp")
with Image.open(output_png_path) as img:
    img.save(output_webp_path, format="webp", quality=70)  # Adjust quality as needed

print(f"Plot saved to {output_webp_path}")

# Close the plot to ensure it is reset for the next plot
plt.close()
