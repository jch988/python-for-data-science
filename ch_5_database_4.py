import yfinance as yf

data = []
tickers = ['TSLA', 'FB', 'ORCL', 'AMZN']

for ticker in tickers:
	tkr = yf.Ticker(ticker)
	hist = tkr.history(period='5d').reset_index()
	records = hist[['Date', 'Close']].to_records(index=False)
	records = list(records)
	records = [(ticker, str(elem[0])[:10], round(elem[1],2)) for elem in records]

	data = data + records



import mysql.connector

try:
	cnx = mysql.connector.connect(user='root', password='apassword', host='127.0.0.1', database='sampledb')

	cursor = cnx.cursor()

	# define the query
	query_add_stocks = ("""INSERT INTO stocks (ticker, date, price) VALUES (%s, %s, %s)""")
	
	# add the stock price rows
	cursor.executemany(query_add_stocks, data)
	cnx.commit()

except mysql.connector.Error as err:
	print('Error-Code:', err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()
