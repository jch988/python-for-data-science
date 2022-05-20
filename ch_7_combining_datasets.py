orders_2022_02_04 = [
(9423517, '2022-02-04', 9001),
(4626232, '2022-02-04', 9003),
(9423534, '2022-02-04', 9001)
    ]
orders_2022_02_05 = [
(9423679, '2022-02-05', 9002),
(4626377, '2022-02-05', 9003),
(4626412, '2022-02-05', 9004)
    ]
orders_2022_02_06 = [
(9423783, '2022-02-06', 9002),
(4626490, '2022-02-06', 9004)
    ]

orders = orders_2022_02_04 + orders_2022_02_05 + orders_2022_02_06

details = [
(9423517, 'Jeans', 'Rip Curl', 87.0, 1),
(9423517, 'Jacket', 'The North Face', 112.0, 1),
(4626232, 'Socks', 'Vans', 15.0, 1),
(4626232, 'Jeans', 'Quiksilver', 82.0, 1),
(9423534, 'Socks', 'DC', 10.0, 2),
(9423534, 'Socks', 'Quiksilver', 12.0, 2),
(9423679, 'T-shirt', 'Patagonia', 35.0, 1),
(4626377, 'Hoody', 'Animal', 44.0, 1),
(4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
(4626412, 'Shirt', 'Volcom', 78.0, 1),
(9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
(9423783, 'Shorts', 'Globe', 26.0, 1),
(4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
(4626490, 'Sweater', 'Dickies', 56.0, 1)
    ]

# orders_details = []
# for order in orders:
#     for detail in details:
#         if detail[0] == order[0]:
#             orders_details.append(order + detail[1:])

orders_details = [[o for o in orders if d[0] == o[0]][0] + d[1:] for d in details]

for thing in orders_details:
    print(thing)

print()
print('-----------------')
print()


# details.append((4626592, 'Shorts', 'Protest', 48.0, 1))
orders_details = [[o for o in orders if d[0] == o[0]][0] + d[1:] for d in details if d[0] in [o[0] for o in orders]]

for thing in orders_details:
    print(thing)

print()
print('-----------------')
print()


import numpy as np

jeff_salary = [2700,3000,3000]
nick_salary = [2600,2800,2800]
tom_salary = [2300,2500,2500]
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])


maya_salary = [2200,2400,2400]
john_salary = [2500,2700,2700]
base_salary2 = np.array([maya_salary, john_salary])

base_salaries = np.concatenate((base_salary1, base_salary2), axis=0)

print(base_salaries)

new_month_salaries = np.array([[3000], [2900], [2500], [2500], [2700]])
base_salaries = np.concatenate((base_salaries, new_month_salaries), axis=1)
print(base_salaries)


print()
print('-----------------')
print()


import pandas as pd

salary_df1 = pd.DataFrame(
    {'jeff': jeff_salary,
    'nick': nick_salary,
    'tom': tom_salary})
salary_df1.index = ['June', 'July', 'August']
salary_df1 = salary_df1.T

salary_df2 = pd.DataFrame(
    {'maya': maya_salary,
    'john': john_salary
    },
    index = ['June', 'July', 'August']
    ).T

salary_df = pd.concat([salary_df1, salary_df2])


salary_df3 = pd.DataFrame(
    {'September': [3000,2800,2500,2400,2700],
     'October': [3200,3000,2700,2500,2900]
    },
    index = ['jeff', 'nick', 'tom', 'maya', 'john']
    )

salary_df = pd.concat([salary_df, salary_df3], axis=1)


salary_df = salary_df.drop(['September', 'October'], axis=1)

salary_df = salary_df.drop(['nick', 'maya'], axis=0)
print(salary_df)


print()
print('-----------------')
print()


df_date_region_1 = pd.DataFrame(
        [
    ('2022-02-04', 'East', 97.0),
    ('2022-02-04', 'West', 243.0),
    ('2022-02-05', 'East', 160.0),
    ('2022-02-05', 'West', 35.0),
    ('2022-02-06', 'East', 110.0),
    ('2022-02-06', 'West',  86.0)
        ],
    columns =['Date', 'Region', 'Total']).set_index(['Date','Region'])

df_date_region_2 = pd.DataFrame(
    [
    ('2022-02-04', 'South', 114.0),
    ('2022-02-05', 'South', 325.0),
    ('2022-02-06', 'South', 212.0),
    ], 
    columns = ['Date', 'Region', 'Total']).set_index(['Date', 'Region'])

df_date_region = pd.concat([df_date_region_1, df_date_region_2]).sort_index(level=['Date', 'Region'])



print()
print('-----------------')
print()


df_orders = pd.DataFrame(orders, columns = ['OrderNo', 'Date', 'Empno'])
df_details = pd.DataFrame(details, columns = ['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])

df_details = df_details.append(
    {
    'OrderNo': 4626592,
    'Item': 'Shorts',
    'Brand': 'Protest',
    'Price': 48.0,
    'Quantity': 1,
    },
    ignore_index=True
    )

df_orders_details_right = df_orders.merge(df_details, how='right', left_on='OrderNo', right_on='OrderNo')

df_orders_details_right =df_orders_details_right.fillna({'Empno':0}).astype({'Empno':'int64'})

print(df_orders_details_right)


print()
print('-----------------')
print()


books = pd.DataFrame({'book_id': ['b1', 'b2', 'b3'],
                      'title': ['Beautiful Coding', 'Python for Web Development','Pythonic Thinking'],
                      'topic': ['programming', 'Python, Web', 'Python']})

authors = pd.DataFrame({'author_id': ['jsn', 'tri', 'wsn'],
                        'author': ['Johnson', 'Treloni', 'Willson']})

matching = pd.DataFrame({'author_id': ['jsn', 'jsn', 'tri', 'wsn'],
                        'book_id': ['b1', 'b2', 'b2', 'b3']})

authorship = books.merge(matching).merge(authors)[['title', 'topic', 'author']]

print(authorship)