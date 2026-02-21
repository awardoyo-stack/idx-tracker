import yfinance as yf
import pandas as pd
import os
from datetime import datetime

idx_stocks = ["BBCA.JK", "BMRI.JK", "BBNI.JK", "GOTO.JK", "TLKM.JK"]
tracker_data = []

for ticker in idx_stocks:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    market_cap = info.get('marketCap')
    pe_ratio = info.get('trailingPE')
    pbv = info.get('priceToBook')
    roe = info.get('returnOnEquity')
    roe_percentage = round(roe * 100, 2) if roe else "N/A"

    company_stats = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Ticker": ticker,
        "Market Cap": market_cap,
        "P/E Ratio": round(pe_ratio, 2) if pe_ratio else "N/A",
        "Price to Book": round(pbv, 2) if pbv else "N/A",
        "ROE (%)": roe_percentage
    }
    tracker_data.append(company_stats)

df = pd.DataFrame(tracker_data)

# CHANGED: We removed the PythonAnywhere username path. 
# Now it just saves directly into the GitHub folder.
file_path = "idx_tracker.csv"
file_exists = os.path.isfile(file_path)
df.to_csv(file_path, mode='a', header=not file_exists, index=False)

print("Data successfully saved!")
