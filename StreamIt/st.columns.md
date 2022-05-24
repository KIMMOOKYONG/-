# 수평으로 컴포넌트 레이아웃 배치

# st.columns

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

```
![image](https://user-images.githubusercontent.com/102650331/169936569-f9260de0-3654-43df-8d9b-2fc7ad6c59a7.png)

```python
import streamlit as st
import numpy as np

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)


```
![image](https://user-images.githubusercontent.com/102650331/169936747-afa9dca9-3f03-49ca-99f5-ed5c7de61af9.png)

# st.expander

```python
import streamlit as st
import numpy as np

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")

```
![image](https://user-images.githubusercontent.com/102650331/169938015-cd55edb4-0976-4e18-b9be-18e7f1a85d3f.png)

```python
import streamlit as st
import numpy as np

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write("""
     The chart above shows some numbers I picked for you.
     I rolled actual dice for these, so they're *guaranteed* to
     be random.
 """)
expander.image("https://static.streamlit.io/examples/dice.jpg")

```
![image](https://user-images.githubusercontent.com/102650331/169938154-9bbdd116-25a6-48f2-bc64-fb4f15fdeecc.png)

# st.container

```python
import streamlit as st
import numpy as np

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

```
![image](https://user-images.githubusercontent.com/102650331/169938554-16eb569d-39fa-444c-88e1-ff3a888668b2.png)

```python
import streamlit as st
import numpy as np

container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")

```

# st.empty

```python
import streamlit as st
import numpy as np
import time

with st.empty():
     for seconds in range(60):
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ 1 minute over!")

```
```python
import streamlit as st

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

# Clear all those elements:
placeholder.empty()
```

