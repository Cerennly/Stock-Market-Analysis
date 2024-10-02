
# Stock Market Analysis

**Stock Market Analysis** is a comprehensive project that focuses on analyzing the stock market trends of six prominent companies in Turkey: **Garanti Bank (TKGBY)**, **Finansbank (QNBFB.IS)**, **Turkish Airlines (THYAO.IS)**, **BIM (BIMAS.IS)**, **Aselsan (ASELS.IS)**, and **Sasa Polyester (SASA.IS)**. This project leverages real-time data from Yahoo Finance to provide insightful visualizations and technical analysis over the past 3 months. Whether you're a financial analyst or an enthusiast, this tool will help you gain deeper insights into stock performance through various key metrics.

## Project Overview

The project retrieves the stock price data of the selected companies and performs detailed technical analysis, such as:
- **Closing Price Trends**: Monitoring price fluctuations over time.
- **Moving Averages (MA)**: Calculation of 10-day and 20-day moving averages to identify long and short-term trends.
- **Volatility Analysis**: Measuring the stability or risk of each stock by calculating the rolling standard deviation.
- **Correlation Analysis**: Investigating the relationship between BIM and Finansbank stock prices to understand how closely they move together.

Using state-of-the-art visualization techniques via **Plotly**, the project delivers highly interactive and insightful charts, allowing users to easily interpret complex data.

## Key Features

### 1. **Stock Data Collection**
The project automatically fetches stock data for the past 3 months from Yahoo Finance, ensuring that the analysis is based on the most up-to-date and accurate information.

### 2. **Interactive Data Visualization**
We provide intuitive and customizable visual representations, including:
- **Line Charts**: Illustrating the closing prices of all companies over time.
- **Area Charts**: Displaying the price movement of each company in comparison to others.
- **Scatter Plot with Trendline**: A correlation plot for **BIM** and **Finansbank**, helping identify potential relationships or dependencies between these stocks.

### 3. **Technical Indicators**
- **Moving Averages (MA10 & MA20)**: These provide a smoother representation of stock price trends, filtering out noise to reveal the true direction of the market.
- **Volatility Tracking**: By computing the rolling standard deviation, this feature highlights periods of high or low price fluctuation, enabling better risk management.

### 4. **Correlation Analysis**
Understanding the relationship between two stocks is crucial for portfolio diversification. Our correlation analysis between **BIM** and **Finansbank** gives insight into how these companies' stocks move relative to one another.

## Why This Project?

In an era where stock market behavior is unpredictable and influenced by multiple factors, this tool allows users to:
- Track performance metrics of **six leading companies** in real-time.
- Compare short and long-term trends through **moving averages**.
- Identify high-risk periods using **volatility measures**.
- Explore the potential **correlation** between companies to make informed investment decisions.

This project not only helps seasoned investors but also serves as an educational tool for those new to stock market analysis. It bridges the gap between raw financial data and meaningful insights through its easy-to-understand visualizations and comprehensive analysis techniques.

## Getting Started

### Installation
To run this project, you will need the following libraries:
- `pandas` for data manipulation
- `yfinance` for downloading stock data
- `plotly` for creating interactive plots

Install them using:
pip install pandas yfinance plotly

Run the script to start the analysis:
python stock_analysis.py

## Conc

Whether you're a trader, financial analyst, or a curious learner, this project equips you with the tools to explore the stock market like never before. Dive into the analysis, uncover hidden trends, and make data-driven decisions with confidence.

---
