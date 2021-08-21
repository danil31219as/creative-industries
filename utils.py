import json
import re
from pymorphy2 import MorphAnalyzer
from pymystem3 import Mystem
from nltk.corpus import stopwords
import gensim

nltk.download("stopwords")
stopwords_ru = stopwords.words("russian") + json.loads(open("stopwords-ru.json").read())
morph = MorphAnalyzer()
patterns = '[0-9!a-z#$%&A-Z"()*+,./:;<=>?-@[\]^_`{|}~—\"\-]+'
m = Mystem()


def give_data(text):
    with open(text, 'r', encoding='utf-8') as data:
        data = data.read()
        li = {}
        data = json.loads(data)
        for i in data:
            title = i['title']
            li[title] = []
            for j in i["news"]:
                li[title].append(" ".join(j["body"].strip().split("\n")).strip())
    return li


def lemmatize_pymorphy2(doc, patterns, morph):
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token:
            token = token.strip()
            token = morph.parse(token)[0].normal_form
            tokens.append(token)
    return " ".join(tokens)


def lemmatize_pymystem3(doc, patterns, m):
    doc = re.sub(patterns, ' ', doc)
    doc = m.lemmatize(doc)
    tokens = []
    for token in doc:
        if token:
            token = token.strip()
            tokens.append(token)
    return " ".join(tokens)


def preprocess_pymorphy2(path):
    inputdata = give_data(path)
    outputdata = {}
    for i in range(len(inputdata)):
        outputdata[list(inputdata.keys())[i]] = []
        for j in inputdata[list(inputdata.keys())[i]]:
            result = []
            for token in gensim.utils.simple_preprocess(lemmatize_pymorphy2(j, patterns, morph)):
                if token not in stopwords_ru and len(token) > 3:
                    result.append(token)
            if len(result) != 0:
                outputdata[list(inputdata.keys())[i]].append(result)
    return outputdata


def preprocess_pymystem3(path):
    inputdata = give_data(path)
    outputdata = {}
    for i in range(len(inputdata)):
        outputdata[list(inputdata.keys())[i]] = []
        for j in inputdata[list(inputdata.keys())[i]]:
            result = []
            for token in gensim.utils.simple_preprocess(lemmatize_pymystem3(j, patterns, m)):
                if token not in stopwords_ru and len(token) > 3:
                    result.append(token)
            if len(result) != 0:
                outputdata[list(inputdata.keys())[i]].append(result)
    return outputdata
