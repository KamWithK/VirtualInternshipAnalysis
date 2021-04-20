import os, pickle
import spacy

import pandas as pd

from gensim import corpora
from gensim.corpora import Dictionary

nlp = spacy.load("en_core_web_sm")

data = pd.read_csv("data/data.csv", encoding = "ISO-8859–1")

def process_corpus(data, min_token_length=2, max_token_length=15, pos_possibilities=("VERB" or "NOUN")):
    token_is_valid = lambda token: not token.is_stop and token.prefix_ != "_" and min_token_length <= len(token.lemma_) <= max_token_length and token.pos_ is pos_possibilities
    return [[token.lemma_ for token in doc if token_is_valid(token)] for doc in nlp.pipe(data)]

# If dictionary was already created, load it
def make_dictionary(path="data/id2word", processed_corpus=None, overwrite=False):
    if not os.path.exists(path) or overwrite:
        dictionary = corpora.Dictionary(processed_corpus)
        dictionary.filter_extremes(no_below=20, no_above=0.1)

        dictionary.save(path)
    else:
        dictionary = Dictionary.load(path)
    
    return dictionary

def make_doc2bow(path="data/bow", processed_corpus=None, dictionary=None, overwrite=False):
    if not os.path.exists(path) or overwrite:
        bow = [dictionary.doc2bow(document) for document in processed_corpus]

        with open("data/bow", "wb") as file:
            pickle.dump(bow, file)

        return bow
    else:
        with open("data/bow", "rb") as file:
            return pickle.load(file)

processed_corpus = process_corpus(data["content"].values)
dictionary = make_dictionary(processed_corpus=processed_corpus, overwrite=True)
make_doc2bow(processed_corpus=processed_corpus, dictionary=dictionary, overwrite=True)
