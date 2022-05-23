"""

Sentiment analysis: determine if a piece of writing is positive or negative

Natural language processing
Classification
Supervised learning

This section: use Amazon reviews and predict start rating 1-5 based on language

"""

import pandas as pd
df = pd.read_csv('ch_12_reviews.csv')

# check the length
# print(len(df))
	# 653

# check the first ten entries
# print(df[['title', 'rating']].head(10))
	#                                                title  rating
	# 0  Great inner content! Not that great outer qual...       4
	# 1                                Very enjoyable read       5
	# 2                                 Worth Every Penny!       5
	# 3  Good for beginner but does not go too far or deep       4
	# 4                                The updated preface       5
	# 5                                 Easy to understand       5
	# 6                             Great book for python.       5
	# 7                   Not bad, but some disappointment       4
	# 8  Truely for the person that doesn't know how to...       3
	# 9                                 Tips for beginners       5

# Looks good so far
# 'title' will be the input, and 'rating' will be the output

print('starting')

# filter out non-English reviews
from google_trans_new import google_translator
detector = google_translator()
df['lang'] = df['title'].apply(lambda x: detector.detect(x)[0])
	# print(len(df)) 	445
df = df[df['lang'] == 'en']
	# print(len(df))	440

# split and transform the data
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
reviews = df['title'].values
ratings = df['rating'].values

# randomly split the data into training (80%) and testing (20%) sets
reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, ratings, test_size=0.2, random_state=1000)

# transform text into numerical feature vectors
vectorizer = CountVectorizer()
vectorizer.fit(reviews_train)
x_train = vectorizer.transform(reviews_train)
x_test = vectorizer.transform(reviews_test)

"""
x_train and x_test are what sckikit-learn has generated from the review titles
using the bag-of-words technique

80% of the reviews (352) are set to train and 20% (88) are set to test.
The lengths of these arrays can be verified

There is a matrix created where each column is a unque word. Each row represents
a review, and most of the columns are 0. The word that appears is a 1.
"""

# train the model using logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

# pass the model the words matrix and the corresponding ratings
classifier.fit(x_train, y_train)

# test the accuracy
import numpy as np
predicted = classifier.predict(x_test)
accuracy = np.mean(predicted == y_test)
print(f"Accuracy", round(accuracy, 2))
	# Accuracy 0.77

# look at a confusion matrix
from sklearn import metrics
# print(metrics.confusion_matrix(y_test, predicted, labels = [1, 2, 3, 4, 5]))

"""
These are the 88 tested reviews

[[ 0  0  0  1  5]
 [ 0  0  0  0  3]
 [ 0  0  0  0  3]
 [ 0  0  0  2  5]
 [ 0  0  1  2 66]]

Rows are actual ratings and columns are predicted ratings

First row: there were 6 actual one-star ratings. 1 of them was labeled as 4-star
and 5 were labeled as 5-star

Bottom row: 69 actual 5-star ratings. One was labeled as 3-star, two as 4-star,
and the rest accurately as 5-star

The main diagnoal top-left to bottom-right shows the correct predictions.
68 were correctly predicted.

68 of 88 (77%, as shown above) were guessed correctly.
A probably reason it's not higher is because there are a disproportionalty high
number of 5-star reviews compared to the other types.

 """

print(metrics.classification_report(y_test, predicted, labels = [1, 2, 3, 4, 5]))

#               precision    recall  f1-score   support

#            1       0.00      0.00      0.00         6
#            2       0.00      0.00      0.00         3
#            3       0.00      0.00      0.00         3
#            4       0.40      0.29      0.33         7
#            5       0.80      0.96      0.87        69

#     accuracy                           0.77        88
#    macro avg       0.24      0.25      0.24        88
# weighted avg       0.66      0.77      0.71        88