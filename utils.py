import json
import re
from pymorphy2 import MorphAnalyzer
from pymystem3 import Mystem
import gensim
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stopwords_ru = stopwords.words("russian") +  json.loads(open("stopwords-ru.json").read())
m = Mystem()
morph = MorphAnalyzer()
patterns = '[0-9!a-z#$%&A-Z"()*+,./:;<=>?-@[\]^_`{|}~—\"\-]+'

# Вариация с pymystem3
def lemmatize_pymystem(doc, patterns, m):
    doc = re.sub(patterns, ' ', doc)
    doc = m.lemmatize(doc)
    tokens = []
    for token in doc:
        if token:
            token = token.strip()
            tokens.append(token)
    return " ".join(tokens)


# Вариация с pymorphy2
def lemmatize(doc):
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token:
            token = token.strip()
            token = morph.parse(token)[0].normal_form
            tokens.append(token)
    return " ".join(tokens)

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(lemmatize(text)):
        if token not in stopwords_ru and len(token) > 3:
            result.append(token)
    return result
