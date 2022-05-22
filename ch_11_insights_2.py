"""
Work with large dataset - hundreds of thousands of transactions. Process like
in part 1 with mlxtend. Provide insights into combinations and sicounts
"""

import pandas as pd
df_retail = pd.read_excel('/Users/JCH/Python/pds/ch_11_online_retail.xlsx', index_col=0, engine='openpyxl')
	# HEADERS: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

# print(len(df_retail))
	# 541909

# remove 'NaN'
df_retail = df_retail.dropna(subset=['Description'])

# change description values to string
df_retail = df_retail.astype({'Description': 'str'})

# turn the df into a list of lists and group by InvoiceNo
trans = df_retail.groupby(['InvoiceNo'])['Description'].apply(list).to_list()

# print(len(trans))
	# 24446

# transform into one-hot encoded boolean array
from mlxtend.preprocessing import TransactionEncoder
encoder = TransactionEncoder()
encoded_array = encoder.fit(trans).transform(trans)
df_trans = pd.DataFrame(encoded_array, columns = encoder.columns_)

# generate frequent itemsets with apriori function (min_support=0.025)
from mlxtend.frequent_patterns import apriori
frequent_transactions = apriori(df_trans, min_support=0.025, use_colnames=True)

# generate association rules (metric='confidence', min_threshold=0.3)
from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_transactions, metric='confidence', min_threshold=0.3)

# print(rules.iloc[:,0:7])


	#                             antecedents  ...       lift
	# 0          (ALARM CLOCK BAKELIKE GREEN)  ...  14.594209
	# 1           (ALARM CLOCK BAKELIKE RED )  ...  14.594209
	# 2      (PINK REGENCY TEACUP AND SAUCER)  ...  18.594571
	# 3     (GREEN REGENCY TEACUP AND SAUCER)  ...  18.594571
	# 4     (GREEN REGENCY TEACUP AND SAUCER)  ...  16.189404
	# 5    (ROSES REGENCY TEACUP AND SAUCER )  ...  16.189404
	# 6             (JUMBO BAG PINK POLKADOT)  ...   7.748130
	# 7             (JUMBO BAG RED RETROSPOT)  ...   7.748130
	# 8   (JUMBO SHOPPER VINTAGE RED PAISLEY)  ...   6.588399
	# 9             (JUMBO BAG RED RETROSPOT)  ...   6.588399
	# 10             (JUMBO STORAGE BAG SUKI)  ...   6.988290
	# 11            (JUMBO BAG RED RETROSPOT)  ...   6.988290
	# 12            (LUNCH BAG  BLACK SKULL.)  ...   7.611972
	# 13            (LUNCH BAG RED RETROSPOT)  ...   7.611972
	# 14            (LUNCH BAG RED RETROSPOT)  ...   8.400970
	# 15            (LUNCH BAG PINK POLKADOT)  ...   8.400970
	# 16     (PINK REGENCY TEACUP AND SAUCER)  ...  16.731144
	# 17   (ROSES REGENCY TEACUP AND SAUCER )  ...  16.731144

	# [18 rows x 7 columns]
	# [Finished in 84.3s]

rules_plot = pd.DataFrame()
rules_plot['antecedents'] = rules['antecedents'].apply(lambda x: ','.join(list(x)))
rules_plot['consequents'] = rules['consequents'].apply(lambda x: ','.join(list(x)))
rules_plot['lift'] = rules['lift'].apply(lambda x: round(x, 2))
pivot = rules_plot.pivot(index = 'antecedents', columns = 'consequents', values = 'lift')
consequents = list(pivot.columns)
antecedents = list(pivot.index.values)
import numpy as np
pivot = pivot.to_numpy()
import matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
im = ax.imshow(pivot, cmap = 'Reds')
ax.set_xticks(np.arange(len(consequents)))
ax.set_yticks(np.arange(len(antecedents)))
ax.set_xticklabels(consequents)
ax.set_yticklabels(antecedents)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(len(antecedents)):
	for j in range(len(consequents)):
		if not np.isnan((pivot[i,j])):
			text = ax.text(j, i, pivot[i,j], ha='center', va='center')
ax.set_title("Lift metric for frequent transactions")
ax.set_xlabel('Consequent')
ax.set_ylabel('Antecedent')
fig.tight_layout()
plt.show()
