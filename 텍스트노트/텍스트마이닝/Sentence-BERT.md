# sentence-transformers 모듈 설치
```
!pip install sentence-transformers

```

# SentenceTransformer 테스트
# Hugging Face
```python
# https://huggingface.co/jhgan/ko-sroberta-multitask
# https://hyunlee103.tistory.com/118
model = SentenceTransformer("jhgan/ko-sroberta-multitask")

sentences = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트 모델입니다."]
embeddings = model.encode(sentences)
print(embeddings)

```
![image](https://user-images.githubusercontent.com/102650331/170448192-4ce55861-a7aa-44da-9aff-672079d68682.png)

# 데이터셋 로드
```python
df = pd.read_csv("https://raw.githubusercontent.com/kairess/mental-health-chatbot/master/wellness_dataset_original.csv")
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170448788-2b0e013e-7104-4eed-9fd5-cf76318b4aa8.png)

# 전처리
```python
df = df.drop(columns=["Unnamed: 3"])
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170448939-8be4eb38-5c4d-4b6f-8530-9909efffdb0d.png)

```python
df = df[~df["챗봇"].isna()]
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170449144-6d80175c-283b-4140-958c-08f25933e1dd.png)


```python
df.loc[0, "유저"]

```
![image](https://user-images.githubusercontent.com/102650331/170449301-1b465c06-27d7-4826-8783-6090fdc5957c.png)

```python
model.encode(df.loc[0, "유저"])

```

