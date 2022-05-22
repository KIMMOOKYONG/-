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

# Development flow
```
소스코드 변경 후 저장하면 Streamlit 프로그램일 자동으로 감지해서 재실행 여부를 묻거나 
설정에서 Always rerun 옵션을 선택하면 자동으로 변경되 소스 코드를 반영해주는 기능을 제공한다.

```

# Data flow
```
소스 코드 변경시 또는 컴포넌트 이벤트 발생시 소스코드 전체를 재실행
재실행 시 비용이 많은 부분에 대해서는 @st.cache 사용

```

# Display and style data
## Use magic("magic commands")
```python
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# 내부적으로 st.write() 메서드를 이용해서 출력함
df

```
![image](https://user-images.githubusercontent.com/102650331/169661876-1e74ff8a-7d20-4fe0-8c52-9440c449427b.png)


## Write a data frame
```python
import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

```
![image](https://user-images.githubusercontent.com/102650331/169661950-d2a43f5a-70b3-403e-a290-373f685794a3.png)

```python
import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

```
![image](https://user-images.githubusercontent.com/102650331/169662025-a58d884c-fad1-4b30-a750-6a3293688408.png)

```python
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

```
![image](https://user-images.githubusercontent.com/102650331/169662064-959bee73-59c7-4fc9-9b4d-3f8177817214.png)

```python
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

```
![image](https://user-images.githubusercontent.com/102650331/169662097-63c8102d-6e2e-4d2f-9c30-fc88a9f83722.png)

## Draw a line chart
```python
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

![image](https://user-images.githubusercontent.com/102650331/169662197-798416e3-e3d0-4826-a70a-b9662be7e908.png)

```python
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

```

![image](https://user-images.githubusercontent.com/102650331/169662397-a59fe5f8-c7ce-46f0-9102-cdf42926a488.png)

# Widgets
```python
import streamlit as st
x = st.slider("x")
st.write(x, "squared is", x * x)

```
![image](https://user-images.githubusercontent.com/102650331/169676470-46c3cea4-dea0-4912-8118-9cae93b33801.png)

```python
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

```
![image](https://user-images.githubusercontent.com/102650331/169676554-3a1353fe-adcc-41c5-b4b5-7dcd08794cc0.png)

## Use checkboxes to show/hide data

```python
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=["a", "b", "c"])

    chart_data

```
![image](https://user-images.githubusercontent.com/102650331/169676802-5016e9e1-c0ff-4410-8bc1-6a561d4c11fb.png)

## Use a selectbox for options

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
    })

# 배열 또는 데이터프
option = st.selectbox(
    "Which number do you like best?",
     df["first column"])

"You selected: ", option

```

![image](https://user-images.githubusercontent.com/102650331/169676860-87af4df0-8b29-40cd-b1ea-ddbcaf50723a.png)

# Layout

```python
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)

```
![image](https://user-images.githubusercontent.com/102650331/169676984-b335d26a-57b3-420c-8e3c-353e1f8545de.png)

```python
import streamlit as st

# st.columns, st.expander
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat",
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

```
![image](https://user-images.githubusercontent.com/102650331/169677045-9c22d941-4ab3-4df8-85fc-3cefe4ae6013.png)

![image](https://user-images.githubusercontent.com/102650331/169677080-7459490b-c417-4465-8db9-d2ec0aaa09a1.png)

## Show progress

```python
import streamlit as st
import time

"Starting a long computation..."

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f"Iteration {i+1}")
  bar.progress(i + 1)
  time.sleep(0.1)

"...and now we\"re done!"

```
![image](https://user-images.githubusercontent.com/102650331/169677118-bb7b9d47-c6ed-4217-a78e-f1bc662c3259.png)

# Themes

![image](https://user-images.githubusercontent.com/102650331/169677147-cb57f96c-81f9-4b08-b315-1aa895501ddf.png)

![image](https://docs.streamlit.io/images/edit_theme.gif)




# 참고
- (Streamlit with Nginx) https://medium.com/featurepreneur/streamlit-with-nginx-bde7a9a41e6c
- (Nginx를 사용해서 Streamlit 서비스 프록시 패스하기) https://gzupark.dev/blog/Passing-the-Streamlit-service-using-Nginx/
- (Streamlit) https://intrepidgeeks.com/tags/Streamlit
- (Streamlit API reference) https://docs.streamlit.io/library/api-reference
- ()
