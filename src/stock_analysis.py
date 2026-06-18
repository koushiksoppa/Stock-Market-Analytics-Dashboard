import yfinance as yf
import pandas as pd

ticker = "RELIANCE.NS"

data = yf.download(ticker, period="1y")

print("First 5 Rows:")
print(data.head())

print("\nLast 5 Rows:")
print(data.tail())

print("\nShape of Data:")
print(data.shape)