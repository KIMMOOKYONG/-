# 참고
- https://blog.streamlit.io/tag/tutorials/
- https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4
- https://wycho.tistory.com/258
- https://www.youtube.com/watch?v=wDysPcF0Hbc
- https://www.youtube.com/watch?v=RHzjE-WBaSk
- https://www.youtube.com/watch?v=hQnMV_bF84I 

# StreamIt 시작하기
```
# STEP1.필요 패키지 설치(StreamIt, localtunnel)

# STEP2.앱 개발

# STEP3.데몬 실행
!streamlit run app.py &>/dev/null&

# STEP4.터널링
!npx localtunnel --port 8501

# STEP5.웹 브라우저 접속 테스트

```

# streamlit 설치
```
!pip install streamlit
StreamIt 설치 후 런타임 재시작 필요
```
![image](https://user-images.githubusercontent.com/102650331/169513227-12b8ae43-1ef6-4c14-a2ac-8f755c290cb5.png)

# 코랩 서버에 외부 접속이 가능하도록 localtunnel 설치
```
!npm install localtunnel

```
![image](https://user-images.githubusercontent.com/102650331/169514115-7cea17d6-bb2b-4d64-b1d5-b5cb24b7945e.png)

# 테스트 코드
```python
%%writefile app.py
import streamlit as st

st.title("Streamlit Test")
st.write("hello world")
st.write("""
# MarkDown
> comment
- one
- two
- three
""")

```

```
# 데몬 실행
!streamlit run app.py &>/dev/null&
# 터널링
!npx localtunnel --port 8501
```
# 터널링
![image](https://user-images.githubusercontent.com/102650331/169514422-94319bfd-d259-46d5-bb4b-260db2f3db93.png)

# 웹 브라우저 접속
![image](https://user-images.githubusercontent.com/102650331/169515188-fab2b1b4-72ca-4418-a087-47ab69569777.png)


