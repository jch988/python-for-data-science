import numpy as np

jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]

base_salary = np.array([jeff_salary, nick_salary, tom_salary])

print(base_salary)

print()

jeff_bonus = [500, 400, 400]
nick_bonus = [600, 300, 400]
tom_bonus= [200, 500, 400]

bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])

print(bonus)

print()

pay = base_salary + bonus

print(pay)

print(pay.max())
print(pay.min())

print(np.amax(pay, axis = 1))
print(np.amax(pay, axis = 0))


avg_high_pay = np.average(np.amax(pay, axis = 0))
print(avg_high_pay)

