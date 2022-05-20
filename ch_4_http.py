import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://github.com/pythondatabook/sources/blob/main/ch4/excerpt.txt')

for i, line in enumerate(r.data.decode('utf-8').split('\n')):
	if line.strip():
		print("Line %i: " %(i), line.strip())