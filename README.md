# Global Energy Data Scraper

## Overview

This project is a Python-based web scraper that uses Selenium to extract energy-related data from the [IEA website](https://www.iea.org/). It collects information such as energy mix, electricity mix, global emissions, and yearly statistics for countries grouped by continents. The data is saved in a CSV file for further analysis.

## Features

- Extracts hidden chart data using JavaScript.
- Collects data at both country and continent levels.
- Saves the results in a structured CSV file.

## Requirements

- Python 3.10.5
- Selenium
- Pandas
- Google Chrome
- Chromedriver (compatible with the installed version of Chrome)

## Setup Instructions

1. **Create and Activate a Virtual Environment**

   ```bash
   # On Windows
   python -m venv env
   .\env\Scripts\activate

   # On macOS/Linux
   python -m venv env
   source env/bin/activate
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Chromedriver is Installed**

   1. Check your Chrome version by navigating to:

      ```plaintext
      chrome://settings/help
      ```

   2. Download the corresponding version of Chromedriver from the [Chromedriver Downloads](https://chromedriver.chromium.org/downloads).
   3. Add Chromedriver to your system's PATH or specify its location in the script.

4. **Run the Script**

   ```bash
   python global_energy_scraper.py
   ```

The script will save the extracted data to a CSV file named `global_energy_data.csv` in the same directory as the script.

## Output

The output CSV file will contain the following columns:

- **Country**: The name of the country.
- **Year**: The year of the data.
- **Global Emissions**: Percentage of global emissions.
- **Energy Supplied Renewable/Non-renewable**: Energy mix data.
- **Electricity Renewable/Non-renewable**: Electricity mix data.

### Example Output

| Country         | Year | Global Emissions | Energy Supplied Renewable | Electricity Renewable |
|-----------------|------|------------------|---------------------------|------------------------|
| United States   | 2022 | 15.5%            | 23%                       | 20%                   |
| Germany         | 2022 | 10.2%            | 30%                       | 40%                   |

## Directory Structure

```plaintext
project/
├── global_energy_scraper.py   # Main script for scraping
├── requirements.txt           # Python dependencies
├── env/                       # Virtual environment (not included in GitHub)
├── global_energy_data.csv     # Output file (generated after running script)
├── LICENSE                    # License for the project
└── README.md                  # Documentation
```

## Notes

- Ensure a stable internet connection while running the script, as it dynamically fetches data from the website.
- Use the same Chrome version as the Chromedriver version to avoid compatibility issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
