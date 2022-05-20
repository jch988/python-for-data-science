import json
import pandas as pd

salaries = [
	{"Empno": 9001, "Salary": 3000},
	{"Empno": 9002, "Salary": 2800},
	{"Empno": 9003, "Salary": 2500},
]

json_data = json.dumps(salaries)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')

# print(salary)
	#        Salary
	# Empno        
	# 9001     3000
	# 9002     2800
	# 9003     2500



data = [
['9001', 'Jeff Russell', 'salesman'],
['9002', 'Nick Offerman', 'carpenter'],
['9003', 'Ron Swanson', 'parks director'],
]

emps = pd.DataFrame(data, columns = ["Empno", 'Name', 'Job'])
col_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(col_types)
emps = emps.set_index('Empno')

# print(emps)
	#                 Name             Job
	# Empno                               
	# 9001    Jeff Russell        salesman
	# 9002   Nick Offerman       carpenter
	# 9003     Ron Swanson  parks director


new_emp = pd.Series({'Name': "Leslie Knope", 'Job': 'idk'}, name = 9004)
emps = emps.append(new_emp)



sales = [
[2608, 9001, 35], [2617, 9001, 35], [2620, 9001, 139],
[2621, 9002, 95], [2626, 9002, 218]
]

orders = pd.DataFrame(sales, columns = ['Pono', 'Empno', 'Total'])
	# print(orders)
		#    Pono  Empno  Total
		# 0  2608   9001     35
		# 1  2617   9001     35
		# 2  2620   9001    139
		# 3  2621   9002     95
		# 4  2626   9002    218



emp_info = emps.join(salary, how='inner')


emp_orders = emps.merge(orders, how='inner', left_on='Empno', right_on='Empno').set_index('Pono')
# print(emp_orders)

print(orders.groupby(['Empno'])['Total'].mean())

print()

print(orders.groupby(['Empno'])['Total'].sum())