def lemmatize(doc, patterns, m):
    doc = re.sub(patterns, ' ', doc)
    doc = m.lemmatize(doc)
    tokens = []
    for token in doc:
        if token:
            token = token.strip()
            tokens.append(token)
    return " ".join(tokens)


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in stopwords_ru and len(token) > 3:
            result.append(token)
    return result
