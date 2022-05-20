import json
import pandas as pd

data = [
{'Emp': 'Jeff Russell',
	'POs': [
			{'Pono': 2608, 'Total': 35},
			{'Pono': 2617, 'Total': 35},
			{'Pono': 2620, 'Total': 139},
			]	
},
{'Emp': 'Nick Boorman',
	'POs': [
			{'Pono': 2121, 'Total': 95},
			{'Pono': 2626, 'Total': 218}
			]
}]

df = pd.json_normalize(data, 'POs', 'Emp').set_index(['Emp', 'Pono'])
print(df)

print()

df = df.reset_index()

json_doc = (df.groupby(['Emp'], as_index=True).apply(lambda x: x[['Pono', 'Total']].to_dict('records')).reset_index().rename(columns={0:'Pos'}).to_json(orient='records'))
print(json.dumps(json.loads(json_doc), indent=2))