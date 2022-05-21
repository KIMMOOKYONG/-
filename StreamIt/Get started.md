# Main concepts
```
# 3가지 방식의 Streamlit 프로그램을 실행시키는 방식

# (1)
# 작성한 스크립트에 파라미터를 전달하는 경우 반드시 -- 사용해야함.
# -- 사용하지 않으면 Sreamlit의 파라미터로 인식함.
streamlit run your_script.py [-- script args]

# (2)
# Python module 실행하는 방법
python -m streamlit run your_script.py

# (3)
# github 에 존재하는 스크립트를 실행하는 방식도 지원함.
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

```

![image](https://user-images.githubusercontent.com/102650331/169661224-c6ca4da4-90d6-4ab7-8edb-b467e1aa0d2c.png)

