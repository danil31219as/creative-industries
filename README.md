# creative-industries

Install requirements

```
pip install tqdm pandas gensim nltk pymorphy2 pymystem3
```

Using CUDA
```
pip install pytorch>=1.6 cudatoolkit=11.0 -c pytorch
```

CPU only
```
pip install pytorch cpuonly -c pytorch
```

Finally
```
pip install simpletransformers
```

Inference

```
python inference.py --path <path to your json with article>
```
Example article.json
```json
{"news": ["doc1", "doc2", "doc3" ...]}
```
