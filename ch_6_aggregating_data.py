import pandas as pd

orders = [
(9423517, '2022-02-04', 9001),
(4626232, '2022-02-04', 9003),
(9423534, '2022-02-04', 9001),
(9423679, '2022-02-05', 9002),
(4626377, '2022-02-05', 9003),
(4626412, '2022-02-05', 9004),
(9423783, '2022-02-06', 9002),
(4626490, '2022-02-06', 9004)
]

details = [
(9423517, 'Jeans', 'Rip Curl', 87.0, 1),
(9423517, 'Jacket', 'The North Face', 112.0, 1),
(4626232, 'Socks', 'Vans', 15.0, 1),
(4626232, 'Jeans', 'Quiksilver', 82.0, 1),
(9423534, 'Socks', 'DC', 10.0, 2),
(9423534, 'Socks', 'Quiksilver', 12.0, 2),
(9423679, 'T-shirt', 'Patagonia', 35.0, 1),
(4626377, 'Hoody', 'Animal', 44.0, 1),
(4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
(4626412, 'Shirt', 'Volcom', 78.0, 1),
(9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
(9423783, 'Shorts', 'Globe', 26.0, 1),
(4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
(4626490, 'Sweater', 'Dickies', 56.0, 1)
]

emps = [
(9001, 'Jeff Russell', 'LA'),
(9002, 'Nick Boorman', 'San Francisco'),
(9003, 'Tom Heints', 'NYC'),
(9004, 'Maya Silver', 'Philadelphia')
]

locations = [
('LA', 'West'),
('San Francisco', 'West'),
('NYC', 'East'),
('Philadelphia', 'East')
]

# create dataframes
df_orders = pd.DataFrame(orders, columns = ['OrderNo', 'Date', 'Empno'])
df_details = pd.DataFrame(details, columns = ['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])
df_emps = pd.DataFrame(emps, columns = ['Empno', 'Empame', 'Location'])
df_locations = pd.DataFrame(locations, columns = ['Location', 'Region'])

# merge orders and details
df_sales = df_orders.merge(df_details)
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']

# Remove unwanted columns
df_sales = df_sales[['Date', 'Empno', 'Total']]

# add emps
df_sales_emps = df_sales.merge(df_emps)

# now add locations
df_result = df_sales_emps.merge(df_locations)

# remove unwanted columns
df_result = df_result[['Date', 'Region', 'Total']]

# create group
df_date_region = df_result.groupby(['Date', 'Region']).sum()

# grand total
ps = df_date_region.sum(axis = 0)
ps.name = ('ALL', 'ALL')

# add grand total to df
df_date_region_total = df_date_region.append(ps)

df_totals = pd.DataFrame()
for date, date_df in df_date_region.groupby(level=0):
	df_totals = df_totals.append(date_df)
	ps = date_df.sum(axis=0)
	ps.name = (date, 'ALL')
	df_totals = df_totals.append(ps)


west_group = df_result.groupby(['Date', 'Region'])
print(west_group.get_group(('2022-02-04', 'West')))
