from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

import json

import random


def converter(data, outputFile):
    db = DocBin()  # create a DocBin object

    for instance in tqdm(data):
        text = instance["text"]
        entities = instance["entities"]
        doc = nlp.make_doc(text)  # create doc object from text
        ents = []
        for start, end, label in entities:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents  # label the text with the ents
        db.add(doc)

    db.to_disk(f"./{outputFile}.spacy")  # save the docbin object
    return f"Processed {len(db)}"


nlp = spacy.blank("de")  # load a new spacy model

with open("monner1.jsonl", "r") as f:
    data = [json.loads(line) for line in f]


# shuffle and split data

random.seed(1234)
random.shuffle(data)

train_splitpoint = int(len(data) * 0.9)

train_data = data[:train_splitpoint]
dev_data = data[train_splitpoint:]

train_convert = converter(train_data, "train")
dev_convert = converter(dev_data, "dev")
