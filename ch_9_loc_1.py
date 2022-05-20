import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCkqsAFBvbSQwzZClsfZvq1vxWU4wVYJcg')
address = '1600 Amphitheatre Parkway, Mountain View, CA'
geocode_result = gmaps.geocode(address)
print(geocode_result[0]['geometry']['location'].values())

