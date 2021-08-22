# creative-industries

Install requirements

```
pip install tqdm pandas gensim nltk pymorphy2 pymystem3
```
CPU only
```
pip install torch
```

Finally
```
pip install simpletransformers
```

Inference [model](https://drive.google.com/file/d/1bPdK13kKiV4RYt8cXwgYGb3dFx46SVjn/view?usp=sharing)

```
python inference.py --path <path to your json with article>
```
Example article.json [download example](https://github.com/danil31219as/creative-industries/blob/main/test_article.json)
```json
{"news": ["doc1", "doc2", "doc3" ...]}
```
