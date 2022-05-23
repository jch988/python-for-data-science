"""
Predict whether the price of a stock will increase, decrease, or stay the same
for the next day

Use classification model
(A more sophisticated model would use regression)

Stock prediction uses all different kinds of input data

"""

import yfinance as yf
tkr = yf.Ticker('AAPL')
hist = tkr.history(period='1y')

	#                   Open        High  ...  Dividends  Stock Splits
	# Date                                ...                         
	# 2021-05-21  127.093883  127.272861  ...        0.0             0
	# 2021-05-24  125.294164  127.213200  ...        0.0             0
	# 2021-05-25  127.093887  127.591054  ...        0.0             0
	# 2021-05-26  126.238763  126.666320  ...        0.0             0
	# 2021-05-27  125.721728  126.914908  ...        0.0             0
	# ...                ...         ...  ...        ...           ...
	# 2022-05-16  145.550003  147.520004  ...        0.0             0
	# 2022-05-17  148.860001  149.770004  ...        0.0             0
	# 2022-05-18  146.850006  147.360001  ...        0.0             0
	# 2022-05-19  139.880005  141.660004  ...        0.0             0
	# 2022-05-20  139.089996  140.699997  ...        0.0             0


# compare to overal market. use S&P 500 during the same 1-year period
import pandas_datareader.data as pdr
from datetime import date, timedelta
end = date.today()
start = end - timedelta(days=365)
index_data = pdr.get_data_stooq('^SPX', start, end)

	#                Open     High      Low    Close      Volume
	# Date                                                      
	# 2022-05-20  3927.76  3943.42  3810.32  3901.36  3000683819
	# 2022-05-19  3899.00  3945.96  3876.58  3900.79  2774587225
	# 2022-05-18  4051.98  4051.98  3911.91  3923.68  2719641498
	# 2022-05-17  4052.00  4090.72  4033.93  4088.85  2462826212
	# 2022-05-16  4013.02  4046.46  3983.99  4008.01  2214046548
	# ...             ...      ...      ...      ...         ...
	# 2021-05-28  4210.77  4218.36  4203.57  4204.11  1958464949
	# 2021-05-27  4201.94  4213.38  4197.78  4200.88  3407781249
	# 2021-05-26  4191.59  4202.61  4184.11  4195.99  2087338274
	# 2021-05-25  4205.94  4213.42  4182.52  4188.13  2117333013
	# 2021-05-24  4170.16  4209.52  4170.16  4197.05  1848676717

# combine AAPL df with S&P500 df
df = hist.join(index_data, rsuffix = '_idx')

# both dfs have same column names. _idx means it's from index_data

	#                   Open        High  ...  Close_idx    Volume_idx
	# Date                                ...                         
	# 2021-05-21  127.093883  127.272861  ...        NaN           NaN
	# 2021-05-24  125.294171  127.213208  ...    4197.05  1.848677e+09
	# 2021-05-25  127.093887  127.591054  ...    4188.13  2.117333e+09
	# 2021-05-26  126.238770  126.666328  ...    4195.99  2.087338e+09
	# 2021-05-27  125.721728  126.914908  ...    4200.88  3.407781e+09
	# ...                ...         ...  ...        ...           ...
	# 2022-05-16  145.550003  147.520004  ...    4008.01  2.214047e+09
	# 2022-05-17  148.860001  149.770004  ...    4088.85  2.462826e+09
	# 2022-05-18  146.850006  147.360001  ...    3923.68  2.719641e+09
	# 2022-05-19  139.880005  141.660004  ...    3900.79  2.774587e+09
	# 2022-05-20  139.089996  140.699997  ...    3901.36  3.000684e+09

	# [253 rows x 12 columns]


# keep only the Close and Volume columns for each stock
df = df[['Close', 'Volume', 'Close_idx', 'Volume_idx']]

	#                  Close     Volume  Close_idx    Volume_idx
	# Date                                                      
	# 2021-05-21  124.717453   79295400        NaN           NaN
	# 2021-05-24  126.377975   63092900    4197.05  1.848677e+09
	# 2021-05-25  126.179123   72009500    4188.13  2.117333e+09
	# 2021-05-26  126.129395   56575900    4195.99  2.087338e+09
	# 2021-05-27  124.568314   94625600    4200.88  3.407781e+09
	# ...                ...        ...        ...           ...
	# 2022-05-16  145.539993   86643800    4008.01  2.214047e+09
	# 2022-05-17  149.240005   78336300    4088.85  2.462826e+09
	# 2022-05-18  140.820007  109742900    3923.68  2.719641e+09
	# 2022-05-19  137.350006  136095600    3900.79  2.774587e+09
	# 2022-05-20  137.589996  137194600    3901.36  3.000684e+09

# calculate the % change for each day
import numpy as np
df['PriceRise'] = np.log(df['Close'] / df['Close'].shift(1))
df['VolumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['PriceRise_idx'] = np.log(df['Close_idx'] / df['Close_idx'].shift(1))
df['VolumeRise_idx'] = np.log(df['Volume_idx'] / df['Volume_idx'].shift(1))
df = df.dropna()

# keep only the newly-calculated columns
df = df[['PriceRise', 'VolumeRise', 'PriceRise_idx', 'VolumeRise_idx']]

	#             PriceRise  VolumeRise  PriceRise_idx  VolumeRise_idx
	# Date                                                            
	# 2021-05-25  -0.001575    0.132190      -0.002128        0.135687
	# 2021-05-26  -0.000394   -0.241215       0.001875       -0.014268
	# 2021-05-27  -0.012454    0.514345       0.001165        0.490172
	# 2021-05-28  -0.005362   -0.282876       0.000769       -0.553900
	# 2021-06-01  -0.002652   -0.052895      -0.000492        0.068334
	# ...               ...         ...            ...             ...
	# 2022-05-16  -0.010730   -0.272523      -0.003954       -0.137526
	# 2022-05-17   0.025105   -0.100794       0.019969        0.106488
	# 2022-05-18  -0.058073    0.337129      -0.041234        0.099191
	# 2022-05-19  -0.024950    0.215217      -0.005851        0.020002
	# 2022-05-20   0.001746    0.008043       0.000146        0.078338

# These will be the inputs


# Make the outputs
conditions = [
	(df['PriceRise'].shift(-1) > 0.01),
	(df['PriceRise'].shift(-1) < 0.01)
		]

choices = [1, -1]
df['Pred'] = np.select(conditions, choices, default=0)


# train the model
features = df[['PriceRise', 'VolumeRise', 'PriceRise_idx', 'VolumeRise_idx']].to_numpy()
features = np.around(features, decimals=2)
target = df['Pred'].to_numpy()

from sklearn.model_selection import train_test_split
rows_train, rows_test, y_train, y_test = train_test_split(features, target, test_size=0.2)
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(rows_train, y_train)

print(clf.score(rows_test, y_test))
	# 0.5882352941176471

"""
The model accurately predicted the next day's stock about 59% of the time
"""