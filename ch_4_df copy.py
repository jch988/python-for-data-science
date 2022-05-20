import json
import pandas as pd

data = [
{'Emp': 'Jeff Russell', 'Emp_email': 'jeff.russel',
	'POs': [
			{'Pono': 2608, 'Total': 35},
			{'Pono': 2617, 'Total': 35},
			{'Pono': 2620, 'Total': 139},
			]	
},
{'Emp': 'Nick Boorman', 'Emp_email': 'nick.boorman',
	'POs': [
			{'Pono': 2121, 'Total': 95},
			{'Pono': 2626, 'Total': 218}
			]
}]

df = pd.json_normalize(data, 'POs', ['Emp', 'Emp_email']).set_index(['Emp', 'Emp_email', 'Pono'])
print(df)

print()

df = df.reset_index()

json_doc = (df.groupby(['Emp'], as_index=True).apply(lambda x: x[['Pono', 'Total']].to_dict('records')).reset_index().rename(columns={0:'Pos'}).to_json(orient='records'))
print(json.dumps(json.loads(json_doc), indent=2))