# SentenceBERT 모델 로드
```python
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

```

```python
# https://huggingface.co/jhgan/ko-sroberta-multitask
model = SentenceTransformer("jhgan/ko-sroberta-multitask")

sentences = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트 모델입니다."]
embeddings = model.encode(sentences)
print(embeddings)

```
