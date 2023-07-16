import pandas as pd
import yfinance as yf
from datetime import datetime

start_date = datetime.now() - pd.DateOffset(months=3)
end_date =datetime.now()

tickers = ["TKGBY", "QNBFB.IS", "THYAO.IS", "BIMAS.IS", "ASELS.IS","SASA.IS"]

df_list =[]
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end =end_date)
    df_list.append(data)

df = pd.concat(df_list, keys=tickers, names=["Ticker", "Date"])
print(df.head())

df =df.reset_index()
print(df.head())

import plotly.express as px
fig1 =px.line(df, x="Date",y ="Close", color="Ticker", title= "son 3 ay icin analiz")
fig1.show()

fig1 = px.area(df, x="Date", y="Close", color="Ticker", facet_col= "Ticker",labels={'Date':'Date', 'Close':'Closing Price', 'Ticker':'Company'},
title='Stock Prices for garanti, enpara, turkhavayolari,bim ,aselsan and sisecam')
fig1.show()

df['MA10'] = df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0, drop=True)
df['MA20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)

for ticker, group in df.groupby('Ticker'):
    print(f'Moving Averages for {ticker}')
    print(group[['MA10', 'MA20']])


for ticker, group in df.groupby("Ticker"):
    fig1= px.line(group, x="Date", y=["Close", "MA10", "MA20"],
    title=f"{ticker} Moving Averages")
    fig1.show()


df['Volatility'] = df.groupby('Ticker')['Close'].pct_change().rolling(window=10).std().reset_index(0, drop=True)
fig = px.line(df, x='Date', y='Volatility', 
color='Ticker', 
title='Volatility of All Companies')
fig.show()

bim = df.loc[df["Ticker"] == "BIMAS.IS", ["Date","Close"]].rename(columns={"Close": "BIMAS.IS"})
fin = df.loc[df["Ticker"] == "QNBFB.IS", ["Date","Close"]].rename(columns={"Close": "QNBFB.IS"})
df_corr = pd.merge(bim, fin, on="Date")

fig1 = px.scatter(df_corr, x="BIMAS.IS", y="QNBFB.IS", trendline="ols", title="korelasyon bim-finansbank")
fig1.show()

