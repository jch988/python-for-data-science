# multivariate time series: more than one variable that changes over time

# get 5 days of stock prices for multiple tickers
import pandas as pd
import yfinance as yf
stocks = pd.DataFrame()
tickers = ['MSFT', 'TSLA', 'GM', 'AAPL', 'ORCL', 'AMZN']
for ticker in tickers:
	tkr = yf.Ticker(ticker)
	hist = tkr.history(period='5d')
	hist = pd.DataFrame(hist[['Close']].rename(columns={'Close': ticker}))
	if stocks.empty:
		stocks = hist
	else:
		stocks = stocks.join(hist)

print(stocks)
	#                   MSFT        TSLA  ...       ORCL         AMZN
	# Date                                ...                        
	# 2022-05-13  260.513245  769.590027  ...  71.169998  2261.100098
	# 2022-05-16  260.892365  724.369995  ...  69.709999  2216.209961
	# 2022-05-17  266.200012  761.609985  ...  71.879997  2307.370117
	# 2022-05-18  254.080002  709.809998  ...  68.300003  2142.250000
	# 2022-05-19  253.139999  709.419983  ...  67.040001  2146.379883

# Filter out stocks whose price dropped more than 5%
stocks_to_keep = []
for i in stocks.columns:
	if stocks[stocks[i]/stocks[i].shift(1) < 0.95].empty:
		stocks_to_keep.append(i)
print(stocks_to_keep)
	# ['MSFT', 'ORCL']

print(stocks[stocks_to_keep])
	#                   MSFT       ORCL
	# Date                             
	# 2022-05-13  260.513245  71.169998
	# 2022-05-16  260.892365  69.709999
	# 2022-05-17  266.200012  71.879997
	# 2022-05-18  254.080002  68.300003
	# 2022-05-19  253.139999  67.040001

