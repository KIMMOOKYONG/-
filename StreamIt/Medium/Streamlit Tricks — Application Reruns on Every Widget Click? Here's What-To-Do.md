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

- 파이 차트 라디오 버턴을 선택해서 파일 차트를 출력할 의도였는데, 스크립트가 재실행되면서 button 의 상태가 초기화되어 파일 차트를 볼 방법이 없다.

# 해결 방법
## Usage of Streamlit checkbox widget(UI 관점에서는 이슈 있음)
- 체크박스를 사용해서 데이터의 로딩 상태 정보 저장

```python
# ---- Modules ------- 
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Fruits List")
# ---- Creating Dictionary ----
_dic = { 'Name': ['Mango', 'Apple', 'Banana'],
         'Quantity': [45, 38, 90]}

load = st.checkbox('Load Data')

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

![](https://miro.medium.com/max/700/1*JH0f6_FY-MDioUWWNjU0ng.gif)

## Controlling Streamlit button ⏹ widget using SessionState
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

# --- Initialising SessionState ---
if "load_state" not in st.session_state:
    st.session_state.load_state = False

if load or st.session_state.load_state:
    st.session_state.load_state = True
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

![](https://miro.medium.com/max/700/1*dmtFZ0D-Z11e39oieAcYaA.gif)

## Wrapping up your code within a function
```python
# ---- Modules ------- 
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Fruits List")

@st.experimental_memo(suppress_st_warning=True)
def skipComputation():
    # ---- Creating Dictionary ----
    _dic = { 'Name': ['Mango', 'Apple', 'Banana'],
            'Quantity': [45, 38, 90]}

    _df = pd.DataFrame(_dic)
    st.info("Only first time you will be seeing me!")
    return _df   

load = st.button('Load Data')

# --- Initialising SessionState ---
if "load_state" not in st.session_state:
    st.session_state.load_state = False

if load or st.session_state.load_state:
    st.session_state.load_state = True
    _df = skipComputation()
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


![](https://miro.medium.com/max/700/1*fwDxX_8AFQDk67O76cZ1vQ.gif)
