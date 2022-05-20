import pandas as pd

# get locations of cabs and find the nearest one
locations = [
               ('cab_26',43.602508,39.715685,'14:47:44'),
               ('cab_112',43.582243,39.752077,'14:47:55'),
               ('cab_26',43.607480,39.721521,'14:49:11'),
               ('cab_112',43.579258,39.758944,'14:49:51'),
               ('cab_112',43.574906,39.766325,'14:51:53'),
               ('cab_26',43.612203,39.720491,'14:52:48')
               ]

df = pd.DataFrame(locations, columns = ['cab', 'lat', 'lon', 'tm'])
	#        cab        lat        lon        tm
	# 0   cab_26  43.602508  39.715685  14:47:44
	# 1  cab_112  43.582243  39.752077  14:47:55
	# 2   cab_26  43.607480  39.721521  14:49:11
	# 3  cab_112  43.579258  39.758944  14:49:51
	# 4  cab_112  43.574906  39.766325  14:51:53
	# 5   cab_26  43.612203  39.720491  14:52:48

# want only most recent locations
latestRows = df.sort_values(['cab', 'tm'], ascending=False).drop_duplicates('cab')
	#        cab        lat        lon        tm
	# 5   cab_26  43.612203  39.720491  14:52:48
	# 4  cab_112  43.574906  39.766325  14:51:53

# convert to list of lists
cabs_loc = latestRows.values.tolist()
	# [['cab_26', 43.612203, 39.720491, '14:52:48'], ['cab_112', 43.574906, 39.766325, '14:51:53']]

# calculate the distance between each cab and the pick up point
from geopy.distance import distance
pick_up = 43.578854, 39.754995
for i, row in enumerate(cabs_loc):
	dist = distance(pick_up, (row[1], row[2])).m
	print(row[0] + ':', round(dist))
	cabs_loc[i].append(round(dist))
		# cab_26: 4636
		# cab_112: 1015

closest = min(cabs_loc, key=lambda x: x[4])
print("The closest cab is ", closest[0]," - the distance in meters: ", closest[4])
	# The closest cab is  cab_112  - the distance in meters:  1015