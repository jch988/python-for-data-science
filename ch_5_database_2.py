import mysql.connector

try:
	cnx = mysql.connector.connect(user='root', password='apassword', host='127.0.0.1', database='sampledb')

	cursor = cnx.cursor()

	query = ("SELECT * FROM emps WHERE empno > %s")
	empno = 9001
	cursor.execute(query, (empno,))
	for (empno, empname, job) in cursor:
		print("{}, {}, {}".format(empno, empname, job))

except mysql.connector.Error as err:
	print('Error-Code:', err.errno)
	print("Error-Message: {}".format(err.msg))

finally:
	cursor.close()
	cnx.close()
