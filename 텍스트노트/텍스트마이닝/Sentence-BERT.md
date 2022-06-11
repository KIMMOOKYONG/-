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

```python
model.encode(df.loc[0, "유저"])

```
![image](https://user-images.githubusercontent.com/102650331/170454873-3f25e0c5-3d77-4b09-8d6d-e123afc764ac.png)

# 데이터 인코딩
```python
df["embedding"] = pd.Series([[]] * len(df)) # dummy
df["embedding"] = df["유저"].map(lambda x: list(model.encode(x)))
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170455294-6fde7731-9093-4ce0-a717-47d106bd0a58.png)

# 간단한 챗봇
```python
text = "요즘 머리가 아프고 너무 힘들어"
embedding = model.encode(text)

df["distance"] = df["embedding"].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/170455501-07653429-39c4-461f-93c2-129585e9444c.png)

```python
answer = df.loc[df["distance"].idxmax()]

print("구분", answer["구분"])
print("유사한 질문", answer["유저"])
print("챗봇 답변", answer["챗봇"])
print("유사도", answer["distance"])

```
![image](https://user-images.githubusercontent.com/102650331/170455592-88a0ac5b-ddfd-48cf-9ef7-b9c2a4eae21e.png)


```python
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import time

from gtts import gTTS
import IPython

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv("https://raw.githubusercontent.com/kairess/mental-health-chatbot/master/wellness_dataset.csv")    
    return df

def speak(text):
    tts = gTTS(text=text, lang="ko")
    filename = "voice.mp3"
    tts.save(filename)

model = cached_model()
df = get_dataset()

# df['embedding'] = df['embedding'].apply(json.loads)  

st.header('심리상담 챗봇')
st.markdown("[❤️빵형의 개발도상국](https://www.youtube.com/c/빵형의개발도상국)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('당신: ', '')
    submitted = st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]

    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['챗봇'])

message = st.empty()
for i in range(len(st.session_state["past"])):
    message.text("사용자: " + st.session_state["past"][i])
    if len(st.session_state["generated"]) > i:
        message.text("상담사: " + st.session_state["generated"][i])

speak(st.session_state["generated"][i])

audio_file = open("voice.mp3", "rb")
st.audio(audio_file.read(), start_time=0)


```

```python
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import time

from gtts import gTTS
import IPython

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv("chatdata.csv")    
    # df['embedding'] = df['embedding'].apply(json.loads)  
    return df

def speak(text):
    tts = gTTS(text=text, lang="ko")
    filename = "voice.mp3"
    tts.save(filename)

model = cached_model()
df = get_dataset()

# df['embedding'] = df['embedding'].apply(json.loads)  

st.header('심리상담 챗봇')
st.markdown("[❤️빵형의 개발도상국](https://www.youtube.com/c/빵형의개발도상국)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('당신: ', '')
    submitted = st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]

    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['A'])

message = st.empty()
for i in range(len(st.session_state["past"])):
    message.text("사용자: " + st.session_state["past"][i])
    if len(st.session_state["generated"]) > i:
        message.text("상담사: " + st.session_state["generated"][i])

speak(st.session_state["generated"][i])

audio_file = open("voice.mp3", "rb")
st.audio(audio_file.read(), start_time=0)


```
