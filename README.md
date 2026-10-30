# Asir Tourism Analysis

A small data analysis project about tourism in Asir region, Saudi Arabia, using Python.

## What it does
- Shows where Asir's visitors come from (2023)
- Compares Asir's visitors to the Kingdom total (2024)
- Generates charts automatically

## Data
All figures in `asir_tourism_data.csv` come from published reports. The `source` column names each one.
Some figures were reported by news outlets quoting the Ministry of Tourism; check the original reports before citing them elsewhere.

Sources:
- Ministry of Tourism 2024 report coverage: https://www.urdupoint.com/arabic/story/2002634.html
- Kingdom totals (SPA): https://www.spa.gov.sa/N2344293
- Ministry of Culture report (SPA): https://www.spa.gov.sa/en/N2166259

The "Other" visitor share is calculated (100% minus the published shares).

## How to run
    pip install -r requirements.txt
    python analysis.py

## Built with
Python, Pandas, Matplotlib

## Future ideas
- Add yearly data from the Ministry of Tourism Statistics portal
- Build an interactive dashboard
