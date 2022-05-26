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

