from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec



# Doc2Vec.FAST_VERSION0

# Pretrained doc2vec : https://github.com/jhlau/doc2vec

import connector
import cleaner

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


## Link : http://linanqiu.github.io/2015/10/07/word2vec-sentiment/


data = connector.postgres_to_dataframe()


# model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)
# model.build_vocab(sentences.to_array())

## Preprocessing Steps
data['value'] = data['value'].apply(lambda x: cleaner.replace_null_with_empty_string(x))
data['readable_text'] = data['value'].apply(lambda x: cleaner.get_readable_text(x))
data['processed_value'] = data['value'].apply(lambda x: cleaner.clean_html_and_extract_text(x))


documents = data['processed_value'].tolist()

labeledDocs = []

for i, document in enumerate(documents):
    labeledDocs.append(LabeledSentence(document.split(), "label_" + str(i)))

    
model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)
model.build_vocab(labeledDocs)

import random

for epoch in range(10):
    random.shuffle(labeledDocs)
    model.train(labeledDocs, total_examples=model.corpus_count,  epochs=model.iter)


model.save('accounting.d2v')

model = Doc2Vec.load('accounting.d2v')

