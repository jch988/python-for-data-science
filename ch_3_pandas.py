import pandas as pd

names = ['Jeff Russell', 'Nick Boorman', 'Tom Heints']
emp_names = pd.Series(names, index = [9001, 9002, 9003], name = 'name')

emails = ['jeff.russell', 'nick.boorman', 'tom.heints']
emp_emails = pd.Series(emails, index = [9001, 9002, 9003], name = 'email')

phones = [1234, 8675309, 4567]
emp_phones = pd.Series(phones, index = [9001, 9002, 9003], name = 'phone')

df = pd.concat([emp_names, emp_emails, emp_phones], axis = 1)
print(df)