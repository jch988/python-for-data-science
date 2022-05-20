# combine spatial and nonspatial data

import pandas as pd

# open orders of cab company
orders = [
		('order_039', 'open', 'cab_14'),
		('order_034', 'open', 'cab_79'),
		('order_032', 'open', 'cab_104'),
		('order_026', 'closed', 'cab_79'),
		('order_021', 'open', 'cab_45'),
		('order_018', 'closed', 'cab_26'),
		('order_008', 'closed', 'cab_112')
		]

# convert to df and make list of cabs that have open orders and are therefore unavailable
df_orders = pd.DataFrame(orders, columns = ['order', 'status', 'cab'])
df_orders_open = df_orders[df_orders['status'] == 'open']
unavailable_list = df_orders_open['cab'].values.tolist()
print(unavailable_list)
	# ['cab_14', 'cab_79', 'cab_104', 'cab_45']
	# can't use those!

# find out which available cab is closest
from geopy.distance import distance

pickup = 46.083822, 38.967845
cab_26 = 46.073852, 38.991890
cab_112 = 46.078228, 39.003949
cab_104 = 46.071226, 39.004947
cab_14 = 46.004859, 38.095825
cab_79 = 46.088621, 39.033929
cab_45 = 46.141225, 39.124934

cabs = {'cab_26': cab_26, 'cab_112': cab_112, 'cab_14': cab_14,
        'cab_104': cab_104, 'cab_79': cab_79, 'cab_45': cab_45}

dist_list = []

for cab_name, cab_loc in cabs.items():
	if cab_name not in unavailable_list:
		dist = distance(pickup, cab_loc).m
		dist_list.append((cab_name, round(dist)))

print(dist_list)
	# [('cab_26', 2165), ('cab_112', 2861)]

print(min(dist_list, key=lambda x: x[1]))
	# ('cab_26', 2165)

# cab_26 is the closest available