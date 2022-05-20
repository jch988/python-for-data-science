
# load the sample dataset
import pandas as pd
df = pd.read_csv('sentiment labelled sentences/amazon_cells_labelled.txt',
			names=['review', 'sentiment'], sep='\t')

# split the data into train and test categories
from sklearn.model_selection import train_test_split
reviews = df['review'].values
sentiments = df['sentiment'].values
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)

# turn the text into numerical values
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(reviews)
X_train = vectorizer.transform(reviews_train)
X_test = vectorizer.transform(reviews_test)

# train and evaluate the model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, sentiment_train)

# evaluate the model
accuracy = classifier.score(X_test, sentiment_test)
print("Accuracy:", accuracy)

# test the model
new_reviews = [
	'Old version of Python is useless',
	'Very good effort, but not five stars',
	'Clear and concise',
	'Have not used yet, but excited to start',
	'Great!',
	'It is ok']
X_new = vectorizer.transform(new_reviews)
print(classifier.predict(X_new))