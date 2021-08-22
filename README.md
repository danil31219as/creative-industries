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

Inference [model](https://drive.google.com/file/d/1-2FK_LDNew7WBymhCrx_mahx_cRodDo5/view?usp=sharing)

```
python inference.py --path <path to your json with article>
```
Example article.json [download example](https://github.com/danil31219as/creative-industries/blob/main/test_article.json)
```json
{"news": ["doc1", "doc2", "doc3" ...]}
```
