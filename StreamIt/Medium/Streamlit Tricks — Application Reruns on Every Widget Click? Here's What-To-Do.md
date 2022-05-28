# 어플리케이션 위젯에 변경이 발생했을때, 전체 코드가 다시 실행되는 문제점을 해결하는 방법에 대한 고찰
![image](https://user-images.githubusercontent.com/102650331/170825406-a30f81e5-2ef7-417f-9b9c-400fe0860784.png)

- 이를 해결하는 방법에 대해서 알아보자.

# Default behaviour of any Streamlit Web App (The Linear flow)
```python
# ---- Modules ------- 
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Fruits List")
# ---- Creating Dictionary ----
_dic = { 'Name': ['Mango', 'Apple', 'Banana'],
         'Quantity': [45, 38, 90]}

load = st.button('Load Data')

if load:
    _df = pd.DataFrame(_dic)
    st.write(_df)

    # ---- Plot types -------
    opt = st.radio('Plot type :',['Bar', 'Pie'])
    if opt == 'Bar':
        fig = px.bar(_df, x= 'Name',
                    y = 'Quantity',title ='Bar Chart')
        st.plotly_chart(fig)

    else:     
        fig = px.pie(_df,names = 'Name',
                    values = 'Quantity',title ='Pie Chart')
        st.plotly_chart(fig)
        

```
![](https://miro.medium.com/max/700/1*p4IAXz04uXK0eiJpfqx8_g.gif)

