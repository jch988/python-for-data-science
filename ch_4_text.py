import csv

path = 'ch_4_cars.csv'
with open(path, 'r') as f:
	csv_reader = csv.DictReader(f)
	cars = []
	for row in csv_reader:
		cars.append(dict(row))

for row in cars:
	print(list(row.values()))

to_update = ['1999', 'Chevy', 'Venture']
price_update = '4500.00'

print()

with open('ch_4_cars.csv', 'w') as f:
	fieldnames = cars[0].keys()
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	for row in cars:
		if set(to_update).issubset(set(row.values())):
			row['Price'] = price_update
		writer.writerow(row)

for row in cars:
	print(list(row.values()))