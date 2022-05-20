# data points in chronological order
# Here, focus on stock prices

# regular vs irregular

import yfinance as yf
ticker = 'TSLA'
tkr = yf.Ticker(ticker)

df = tkr.history(period='5d')

	#                   Open        High  ...  Dividends  Stock Splits
	# Date                                ...                         
	# 2022-05-13  773.479980  787.349976  ...          0             0
	# 2022-05-16  767.159973  769.760010  ...          0             0
	# 2022-05-17  747.359985  764.479980  ...          0             0
	# 2022-05-18  744.520020  760.500000  ...          0             0
	# 2022-05-19  707.000000  734.000000  ...          0             0

# just want the amount at the close of each day
print(df['Close'])
	# Date
	# 2022-05-13    769.590027
	# 2022-05-16    724.369995
	# 2022-05-17    761.609985
	# 2022-05-18    709.809998
	# 2022-05-19    709.419983


# Do a 2-day shoft to see changes over time and compare data across different days
import pandas as pd
print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1, keys = ['Close', '2DayShift']))
	#                  Close   2DayShift
	# Date                              
	# 2022-05-13  769.590027         NaN
	# 2022-05-16  724.369995         NaN
	# 2022-05-17  761.609985  769.590027
	# 2022-05-18  709.809998  724.369995
	# 2022-05-19  709.419983  761.609985

# Calculate the change across 2 days. Take the nat log of the current over old
import numpy as np
df['2DaysRaise'] = np.log(df['Close'] / df['Close'].shift(2))
print(df[['Close', '2DaysRaise']])
	#                  Close  2DaysRaise
	# Date                              
	# 2022-05-13  769.590027         NaN
	# 2022-05-16  724.369995         NaN
	# 2022-05-17  761.609985   -0.010423
	# 2022-05-18  709.809998   -0.020305
	# 2022-05-19  709.419983   -0.070987

# Look at the rolling average closing price for the preceding two days
df['2DaysAvg'] = df['Close'].shift(1).rolling(2).mean()
print(df[['Close', '2DaysAvg']])
	#                  Close    2DaysAvg
	# Date                              
	# 2022-05-13  769.590027         NaN
	# 2022-05-16  724.369995         NaN
	# 2022-05-17  761.609985  746.980011
	# 2022-05-18  709.809998  742.989990
	# 2022-05-19  709.419983  735.709991

# The 2DaysAvg for 5-19 is of 5-17 and 5-18
# This shows is the stock performance is consistent

# Now calculate the % change between each days price and it's rolling average
df['2DaysAvgRaise'] = np.log(df['Close'] / df['2DaysAvg'])
print(df[['Close', '2DaysRaise', '2DaysAvgRaise']])
	#                  Close  2DaysRaise  2DaysAvgRaise
	# Date                                             
	# 2022-05-13  769.590027         NaN            NaN
	# 2022-05-16  724.369995         NaN            NaN
	# 2022-05-17  761.609985   -0.010423       0.019396
	# 2022-05-18  709.809998   -0.020305      -0.045685
	# 2022-05-19  709.419983   -0.070987      -0.036388

