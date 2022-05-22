# st.write

```python
import streamlit as st

# 마크다운 형식 지원
st.write("Hello, **World!** :sunglasses:")

```
![image](https://user-images.githubusercontent.com/102650331/169700551-3157b388-dbc3-4404-ac08-bdd84d77ad8b.png)

```python
import streamlit as st
import pandas as pd

st.write(1234)
st.write(pd.DataFrame({
     "first column": [1, 2, 3, 4],
     "second column": [10, 20, 30, 40],
 }))

```
![image](https://user-images.githubusercontent.com/102650331/169700632-e80358c9-f34a-47e2-b389-549afffe3a83.png)

```python
import streamlit as st
import pandas as pd

st.write(1234)
data_frame = pd.DataFrame({
     "first column": [1, 2, 3, 4],
     "second column": [10, 20, 30, 40],
 })

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")

```
![image](https://user-images.githubusercontent.com/102650331/169700743-c190fa1d-6f62-4148-ac22-4eecb1f30ff9.png)

```python
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

```
![image](https://user-images.githubusercontent.com/102650331/169700843-31d74937-3314-4591-81f7-466afe369af1.png)





