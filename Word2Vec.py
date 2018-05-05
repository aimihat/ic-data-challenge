from gensim.models import Word2Vec
import pandas as pd
import csv

# define training data
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
			['this', 'is', 'the', 'second', 'sentence'],
			['yet', 'another', 'sentence'],
			['one', 'more', 'sentence'],
			['and', 'the', 'final', 'sentence']]
mSentences = [];

df = pd.read_csv("10.csv")
print(df.ix[:,1])

with open("100000.csv", 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		mSentences.append(row)


# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
print(model['sentence'])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)