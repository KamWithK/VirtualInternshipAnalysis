import spacy

import pandas as pd

from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")

data = pd.read_csv("data/data.csv")

# Sets up one hot encoded labels
def set_cats(doc, value):
    for number in range(9):
        doc.cats[f"SCORE_{number}"] = 0 if number != value else 1
    return doc

categorised_data = [set_cats(doc, score) for doc, score in nlp.pipe(data[["content", "OutcomeScore"]].values, as_tuples=True)]


split_percent = 70
train_end = (len(categorised_data) // 100) * split_percent

train_data, validation_data = categorised_data[:train_end], categorised_data[train_end:]
train_bin, validation_bin = DocBin(docs=train_data), DocBin(docs=validation_data)
train_bin.to_disk("data/train.spacy"), validation_bin.to_disk("data/validation.spacy")
