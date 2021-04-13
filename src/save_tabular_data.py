import spacy

import pandas as pd

from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")

data = pd.read_csv("data/data.csv")

# Sets up one hot encoded labels
fields = ["m_experimental_testing", "m_making_design_choices", "m_asking_questions", "j_customer_consultants_requests", "j_performance_parameters_requirements", "j_communication"]
def set_cats(doc, value):
    for index, category in enumerate(fields):
        doc.cats[category] = value[index]
    return doc

data = [(field[0], (field[1:])) for field in data[["content", *fields]].values]
categorised_data = [set_cats(doc, score) for doc, score in nlp.pipe(data, as_tuples=True)]


split_percent = 70
train_end = (len(categorised_data) // 100) * split_percent

train_data, validation_data = categorised_data[:train_end], categorised_data[train_end:]
train_bin, validation_bin = DocBin(docs=train_data), DocBin(docs=validation_data)
train_bin.to_disk("data/train.spacy"), validation_bin.to_disk("data/validation.spacy")