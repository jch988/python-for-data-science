# market basket analysis (how often two items are likely to be purchased together)

# terms: antecedent -> consequent (x -> y), itemsets

# association rules
	# - support: what % of the time an item appears in a transaction
	# - confidence: what % of the transactions involving the consequent also involved the antecedent
	# - lift: strength of association compared to random co-occurence

# if lift:
	# > 1, positive association (likely to be purchased together)
	# = 1, no correlation
	# < 1, negative correlation (unlikely to be purchased together)

# Apriori algorithm

transactions = [
   ['curd', 'sour cream'], ['curd', 'orange', 'sour cream'],
   ['bread', 'cheese', 'butter'], ['bread', 'butter'], ['bread', 'milk'],
   ['apple', 'orange', 'pear'], ['bread', 'milk', 'eggs'], ['tea', 'lemon'],
   ['curd', 'sour cream', 'apple'], ['eggs', 'wheat flour', 'milk'],
   ['pasta', 'cheese'], ['bread', 'cheese'], ['pasta', 'olive oil','cheese'],
   ['curd', 'jam'], ['bread', 'cheese', 'butter'],
   ['bread', 'sour cream','butter'], ['strawberry', 'sour cream'],
   ['curd', 'sour cream'], ['bread', 'coffee'], ['onion', 'garlic']
				]

# What are the associations between these items?

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

# create TansactionEncoder object
encoder = TransactionEncoder()

# turn 'transactions' list into 'one-hot encoded boolean array'
encoded_array = encoder.fit(transactions).transform(transactions)

# convert to pandas dataframe
df_itemsets = pd.DataFrame(encoded_array, columns = encoder.columns_)

	#     apple  bread  butter  cheese  ...  sour cream  strawberry    tea  wheat flour
	# 0   False  False   False   False  ...        True       False  False        False
	# 1   False  False   False   False  ...        True       False  False        False
	# 2   False   True    True    True  ...       False       False  False        False
	# 3   False   True    True   False  ...       False       False  False        False
	# 4   False   True   False   False  ...       False       False  False        False
	# 5    True  False   False   False  ...       False       False  False        False
	# 6   False   True   False   False  ...       False       False  False        False
	# 7   False  False   False   False  ...       False       False   True        False
	# 8    True  False   False   False  ...        True       False  False        False
	# 9   False  False   False   False  ...       False       False  False         True
	# 10  False  False   False    True  ...       False       False  False        False
	# 11  False   True   False    True  ...       False       False  False        False
	# 12  False  False   False    True  ...       False       False  False        False
	# 13  False  False   False   False  ...       False       False  False        False
	# 14  False   True    True    True  ...       False       False  False        False
	# 15  False   True    True   False  ...        True       False  False        False
	# 16  False  False   False   False  ...        True        True  False        False
	# 17  False  False   False   False  ...        True       False  False        False
	# 18  False   True   False   False  ...       False       False  False        False
	# 19  False  False   False   False  ...       False       False  False        False

# Implement the Apriori function
from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df_itemsets, min_support=0.1, use_colnames=True)

	#     support                 itemsets
	# 0      0.10                  (apple)
	# 1      0.40                  (bread)
	# 2      0.20                 (butter)
	# 3      0.25                 (cheese)
	# 4      0.25                   (curd)
	# 5      0.10                   (eggs)
	# 6      0.15                   (milk)
	# 7      0.10                 (orange)
	# 8      0.10                  (pasta)
	# 9      0.30             (sour cream)
	# 10     0.20          (butter, bread)
	# 11     0.15          (bread, cheese)
	# 12     0.10            (bread, milk)
	# 13     0.10         (butter, cheese)
	# 14     0.10          (pasta, cheese)
	# 15     0.20       (sour cream, curd)
	# 16     0.10             (eggs, milk)
	# 17     0.10  (butter, bread, cheese)

# All of these items or combinations of items have at least 10% support—they appear at least 10% of the time.

# Now generate association rules (support, confidence, lift). Limit confidence to 0.5 or higher
# This function automatically skips single-member itemsets
from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

	#          antecedents      consequents  antecedent support  consequent support  \
	# 0           (butter)          (bread)                0.20                0.40   
	# 1            (bread)         (butter)                0.40                0.20   
	# 2           (cheese)          (bread)                0.25                0.40   
	# 3             (milk)          (bread)                0.15                0.40   
	# 4           (butter)         (cheese)                0.20                0.25   
	# 5            (pasta)         (cheese)                0.10                0.25   
	# 6       (sour cream)           (curd)                0.30                0.25   
	# 7             (curd)     (sour cream)                0.25                0.30   
	# 8             (milk)           (eggs)                0.15                0.10   
	# 9             (eggs)           (milk)                0.10                0.15   
	# 10   (butter, bread)         (cheese)                0.20                0.25   
	# 11  (butter, cheese)          (bread)                0.10                0.40   
	# 12   (bread, cheese)         (butter)                0.15                0.20   
	# 13          (butter)  (bread, cheese)                0.20                0.15   

	#     support  confidence   lift  
	# 0      0.20       1.000  2.500  
	# 1      0.20       0.500  2.500  
	# 2      0.15       0.600  1.500  
	# 3      0.10       0.667  1.667  
	# 4      0.10       0.500  2.000  
	# 5      0.10       1.000  4.000  
	# 6      0.20       0.667  2.667  
	# 7      0.20       0.800  2.667  
	# 8      0.10       0.667  6.667  
	# 9      0.10       1.000  6.667  
	# 10     0.10       0.500  2.000  
	# 11     0.10       1.000  2.500  
	# 12     0.10       0.667  3.333  
	# 13     0.10       0.500  3.333  


# Visualize the results with a heatmap

# prepare the data

# make empty df
rules_plot = pd.DataFrame()

# convert headers of relevant columns from 'rules' to strings so they can be used as labels in the visualization
rules_plot['antecedents'] = rules['antecedents'].apply(lambda x: ','.join(list(x)))
rules_plot['consequents'] = rules['consequents'].apply(lambda x: ','.join(list(x)))

# round the lift values to 2 decimal places
rules_plot['lift'] = rules['lift'].apply(lambda x: round(x, 2))

# convert to matrix. Antecedents are vertical, Consequents are horizontal
pivot = rules_plot.pivot(index = 'antecedents', columns = 'consequents', values = 'lift')

# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
    # print(pivot)

	# consequents    bread  bread,cheese  butter  cheese  curd  eggs  milk  \
	# antecedents                                                            
	# bread            NaN           NaN    2.50     NaN   NaN   NaN   NaN   
	# bread,butter     NaN           NaN     NaN     2.0   NaN   NaN   NaN   
	# bread,cheese     NaN           NaN    3.33     NaN   NaN   NaN   NaN   
	# butter          2.50          3.33     NaN     2.0   NaN   NaN   NaN   
	# butter,cheese   2.50           NaN     NaN     NaN   NaN   NaN   NaN   
	# cheese          1.50           NaN     NaN     NaN   NaN   NaN   NaN   
	# curd             NaN           NaN     NaN     NaN   NaN   NaN   NaN   
	# eggs             NaN           NaN     NaN     NaN   NaN   NaN  6.67   
	# milk            1.67           NaN     NaN     NaN   NaN  6.67   NaN   
	# pasta            NaN           NaN     NaN     4.0   NaN   NaN   NaN   
	# sour cream       NaN           NaN     NaN     NaN  2.67   NaN   NaN   

	# consequents    sour cream  
	# antecedents                
	# bread                 NaN  
	# bread,butter          NaN  
	# bread,cheese          NaN  
	# butter                NaN  
	# butter,cheese         NaN  
	# cheese                NaN  
	# curd                 2.67  
	# eggs                  NaN  
	# milk                  NaN  
	# pasta                 NaN  
	# sour cream            NaN  

# The consequents will become the x-axis values
consequents = list(pivot.columns)

# The antecedents will become the y-axis values
antecedents = list(pivot.index.values)

# turn the values for the plot into a numpy array
import numpy as np
pivot = pivot.to_numpy()


# create the visualization

import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# convert data from 'pivot' numpy array into a 2-d color-coded image
im = ax.imshow(pivot, cmap = 'Reds')

ax.set_xticks(np.arange(len(consequents)))
ax.set_yticks(np.arange(len(antecedents)))
ax.set_xticklabels(consequents)
ax.set_yticklabels(antecedents)

# rotate the x-axis labels by 45 degrees (to fit better)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# loop over the data in the 'pivot' array
for i in range(len(antecedents)):
	for j in range(len(consequents)): 

		# filter out any pairs that have 'NaN'
		if not np.isnan((pivot[i, j])):

			# create a text annotation for each square in the heatmap
			text = ax.text(j, i, pivot[i, j], ha='center', va='center')


ax.set_title("Lift metric for frequent itemsets")
ax.set_xlabel('Consequent')
ax.set_ylabel('Antecedent')
fig.tight_layout()

# show the plot
# plt.show()


# GAIN INSIGHTS



# Make recommendations
# Set 'butter' as the antecedent and see which item or item sets have the three highest confidence values

# find the rules where butter is the antecedent and sort according to confidence (highest at the top)
butter_antecedent = rules[rules['antecedents'] == {'butter'}][['consequents','confidence']].sort_values('confidence', ascending = False)

# take the top three values and print them out
butter_consequents = [list(item) for item in butter_antecedent.iloc[0:3:,]['consequents']]
item = 'butter'
# print(f"Items frequently bought together with {item} are: {butter_consequents}")
	# Items frequently bought together with butter are: [['bread'], ['cheese'], ['bread', 'cheese']]





# Discounts
# Choose a single item to be discounted in each frequent itemset

# create an 'itemsets' column
from functools import reduce
rules['itemsets'] = rules[['antecedents', 'consequents']].apply(lambda x: reduce(frozenset.union, x), axis=1)
# print(rules[['antecedents', 'consequents', 'itemsets']])
	#          antecedents      consequents                 itemsets
	# 0           (butter)          (bread)          (butter, bread)
	# 1            (bread)         (butter)          (butter, bread)
	# 2           (cheese)          (bread)          (cheese, bread)
	# 3             (milk)          (bread)            (bread, milk)
	# 4           (butter)         (cheese)         (butter, cheese)
	# 5            (pasta)         (cheese)          (pasta, cheese)
	# 6             (curd)     (sour cream)       (curd, sour cream)
	# 7       (sour cream)           (curd)       (curd, sour cream)
	# 8             (eggs)           (milk)             (eggs, milk)
	# 9             (milk)           (eggs)             (eggs, milk)
	# 10  (butter, cheese)          (bread)  (butter, cheese, bread)
	# 11   (butter, bread)         (cheese)  (butter, cheese, bread)
	# 12   (cheese, bread)         (butter)  (butter, cheese, bread)
	# 13          (butter)  (cheese, bread)  (butter, cheese, bread)

# order doesn't matter here, so remove duplicates
rules.drop_duplicates(subset=['itemsets'], keep='first', inplace=True)
# print(rules['itemsets'])
	# 0             (butter, bread)
	# 2             (cheese, bread)
	# 3               (bread, milk)
	# 4            (butter, cheese)
	# 5             (cheese, pasta)
	# 6          (sour cream, curd)
	# 8                (milk, eggs)
	# 10    (butter, bread, cheese)
	# Name: itemsets, dtype: object

discounted = []
others = []
for itemset in rules['itemsets']:
	for i, item in enumerate(itemset):
		if item not in others:
			discounted.append(item)
			itemset = set(itemset)
			itemset.discard(item)
			others.extend(itemset)
			break
		if i == len(itemset)-1:
			discounted.append(item)
			itemset = set(itemset)
			itemset.discard(item)
			others.extend(itemset)
print(discounted)
	# ['butter', 'cheese', 'milk', 'butter', 'pasta', 'curd', 'eggs', 'butter']
print(set(discounted))
	# {'cheese', 'butter', 'bread', 'eggs', 'sour cream', 'pasta', 'milk'}
# Can discount these items


