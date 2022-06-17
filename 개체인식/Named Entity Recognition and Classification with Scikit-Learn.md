# Named Entity Recognition and Classification with Scikit-Learn
# The Data
- https://www.kaggle.com/code/abhinavwalia95/how-to-loading-and-fitting-dataset-to-scikit/data?select=ner_dataset.csv

![image](https://user-images.githubusercontent.com/102650331/174271214-24049b93-5fd4-404a-beae-7c0660b1bbb7.png)

# Essential info about entities
![image](https://user-images.githubusercontent.com/102650331/174271320-eaf94b90-88c8-4424-af5b-efba5cb3b6ef.png)

# Inside–outside–beginning (tagging)
- short for inside, outside, beginning
![image](https://user-images.githubusercontent.com/102650331/174271465-941a0be9-f162-4815-a34c-ac72eec41fc5.png)

# The Data
```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

df = pd.read_csv("https://raw.githubusercontent.com/KIMMOOKYONG/Technical-Note/main/%EA%B0%9C%EC%B2%B4%EC%9D%B8%EC%8B%9D/ner_dataset.csv", \
                encoding = "ISO-8859-1")
df = df[:100000]
df.head()

df.isnull().sum()

```
![image](https://user-images.githubusercontent.com/102650331/174272351-535b6409-60b4-4f3f-ae16-e3a8e7d070c4.png)

# Data Preprocessing
```python
df = df.fillna(method="ffill")
df["Sentence #"].nunique(), df.Word.nunique(), df.Tag.nunique()

```

```python
df.groupby("Tag").size().reset_index(name="count")

```
![image](https://user-images.githubusercontent.com/102650331/174273452-c9f44ef3-e6f2-445a-a6fd-6a99d0566b8b.png)

