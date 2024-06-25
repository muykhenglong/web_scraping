# Financial Data Extraction Using Selenium

This Python script automates the extraction of financial data from Yahoo Finance for multiple tickers using Selenium. It retrieves income statements, balance sheets, and cash flow statements, converting them into structured Pandas dataframes for further analysis.

## Features

- **Automated Browser Interaction**: Uses Selenium to interact with Yahoo Finance web pages.
- **Data Extraction**: Retrieves financial data including income statements, balance sheets, and cash flow statements.
- **Data Transformation**: Cleans and transforms the data into a numerical format, making it ready for analysis.

## Requirements

- Python 3.8.19
- Selenium WebDriver
- Pandas

Ensure you have the necessary Python packages installed:
```pip install selenium pandas

## How It Works

The script initializes a browser instance using Selenium and navigates to the Yahoo Finance page for each ticker.
It interacts with the page to navigate to the financials section and triggers any necessary clicks to reveal data.
Financial data is extracted from structured HTML tables into a text format.
The script converts this text into a structured Pandas dataframe and cleans the data by removing non-numeric characters and converting strings to numerical values.

## Author

Muykheng Long
