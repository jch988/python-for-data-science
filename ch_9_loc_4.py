# find objects in a certain area
# sometimes obstacles, like rivers, block a path
# the closest cab in distance is not always the closest in time

from shapely.geometry import Point, Polygon

# create area north of the river
coords = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395,
             38.997684),(46.073822, 39.007297), (46.081741, 39.008842)]
poly = Polygon(coords)

# set locations of cabs and pick-up point
cab_26 = Point(46.073852, 38.991890)
cab_112 = Point(46.078228, 39.003949)
pick_up = Point(46.080074, 38.991289)


# find out which cab is within the polygon
print("cab_26 within the polygon:", cab_26.within(poly))
print("cab_112 within the polygon:", cab_112.within(poly))
print("pick_up within the polygon:", pick_up.within(poly))

		# cab_26 within the polygon: False
		# cab_112 within the polygon: True
		# pick_up within the polygon: True

# define an entry point between the two polygons
# if cab is in adjacent polygon, must calculate two distances

from geopy.distance import distance
entry_point = Point(46.075357, 39.000298)


# calculate how far cab_26 has to travel (loc to entry point into new polygon, plus then to pick-up point)
if cab_26.within(poly):
	dist = distance((pick_up.x, pick_up.y), (cab_26.x, cab_26.y)).m
else:
	dist1 = distance((cab_26.x, cab_26.y), (entry_point.x, entry_point.y)).m
	dist2 = distance((entry_point.x, entry_point.y), (pick_up.x, pick_up.y)).m
	dist = dist1 + dist2

print(dist)
		# 1543.7000956024508

