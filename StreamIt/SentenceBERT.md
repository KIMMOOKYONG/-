# 구글 코랩 파이썬 버전 업그레이드
```
#install python 3.9
!sudo apt-get update -y
!sudo apt-get install python3.9

#change alternatives
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

#check python version
!python --version
#3.9.6

```

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

![image](https://user-images.githubusercontent.com/102650331/170174853-93370641-30e3-4abe-ac8c-a55b731f19a4.png)

# 데이터셋 로드
```python
df = pd.read_csv("https://raw.githubusercontent.com/kairess/mental-health-chatbot/master/wellness_dataset_original.csv")
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170175290-5d4fbeb1-df98-4beb-9ea1-8eba8b201fcc.png)

# 전처리
```python
df = df.drop(columns=["Unnamed: 3"])
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170175435-3fc7bfc3-cd0a-4dcd-8225-1c149f5e7180.png)

```python
df = df[~df["챗봇"].isna()]
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170175551-daf5a0d0-4230-413b-9685-06b359e26815.png)

```python
df.loc[0, "유저"]

```
![image](https://user-images.githubusercontent.com/102650331/170175649-fce04bcf-0e83-4dde-8ffd-fde7115aba49.png)

```python
model.encode(df.loc[0, "유저"])

```
![image](https://user-images.githubusercontent.com/102650331/170175762-378d2089-3f6c-476c-8f3a-d91bbfa74ec7.png)

# 유저 대화내용 인코딩
```python
df["embedding"] = pd.Series([[]] * len(df)) # dummy
df["embedding"] = df["유저"].map(lambda x: list(model.encode(x)))
df.head()

df.to_csv("wellness_dataset.csv", index=False)

```
![image](https://user-images.githubusercontent.com/102650331/170176817-7faceecf-81a0-4e50-87d8-d5fc0a75b5b8.png)

# 간단한 챗봇
```python
text = "요즘 머리가 아프고 너무 힘들어"
embedding = model.encode(text)

df["distance"] = df["embedding"].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170177075-095fd697-8604-46ff-bf7b-9a68cc0cab90.png)

```python
answer = df.loc[df["distance"].idxmax()]

print("구분", answer["구분"])
print("유사한 질문", answer["유저"])
print("챗봇 답변", answer["챗봇"])
print("유사도", answer["distance"])

```
![image](https://user-images.githubusercontent.com/102650331/170177195-678754e1-acff-4b3d-a2fa-4c47e8e1a437.png)

