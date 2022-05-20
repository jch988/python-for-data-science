import mysql.connector

try:
	cnx = mysql.connector.connect(user='root', password='apassword', host='127.0.0.1', database='sampledb')

	cursor = cnx.cursor()

	# define the employee rows
	emps = [
	(9001, "Ron Swanson", 'Parks Director'),
	(9002, "Leslie Knope", "Deputy Parks Director"),
	(9003, "Nick Offerman", "Carpenter")
	]

	# define the query
	query_add_emp = ("""INSERT INTO emps (empno, empname, job) VALUES (%s, %s, %s)""")

	# insert employees
	for emp in emps:
		cursor.execute(query_add_emp, emp)

	# define and insert the salaries
	salary = [
	(9001, 3000),
	(9002, 2800),
	(9003, 2500),
	]
	query_add_salary = ("""INSERT INTO salary (empno, salary) VALUES (%s, %s)""")
	for sal in salary:
		cursor.execute(query_add_salary, sal)

	# define and insert the orders
	orders = [
	(2608, 9001, 35),
	(2617, 9001, 35),
	(2620, 9001, 139),
	(2621, 9002, 95),
	(2626, 9002, 218)
	]
	query_add_order = ("""INSERT INTO orders(pono, empno, total) VALUES (%s, %s, %s)""")
	for order in orders:
		cursor.execute(query_add_order, order)
	
	# make the insertions permanent in the database
	cnx.commit()

except mysql.connector.Error as err:
	print('Error-Code:', err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()
