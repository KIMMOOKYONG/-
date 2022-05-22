# st.markdown

```python
import streamlit as st

st.markdown("Streamlit is **_really_ cool**.")

```
![image](https://user-images.githubusercontent.com/102650331/169701198-8cb1bdd6-9d17-4790-a4b3-37e04e91ba44.png)

# st.title

```python
import streamlit as st

st.title("This is a title")

```
![image](https://user-images.githubusercontent.com/102650331/169701297-1ecc3a71-9604-401a-9e60-055345a4a140.png)

# st.header

```python
import streamlit as st

st.header("This is a header")

```
![image](https://user-images.githubusercontent.com/102650331/169701338-6923cf44-6e75-42a5-9bef-a1fbb70e9911.png)

# st.subheader

```python
import streamlit as st

st.subheader("This is a subheader")

```
![image](https://user-images.githubusercontent.com/102650331/169701377-c2657dca-fbf7-4d78-b82c-5946a1a087e0.png)

# st.caption

```python
import streamlit as st

st.caption("This is a string that explains something above.")

```
![image](https://user-images.githubusercontent.com/102650331/169701428-d9fefaf9-2ebd-424f-bcbb-f4376a67fe29.png)

# st.code

```python
import streamlit as st

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language="python")

```
![image](https://user-images.githubusercontent.com/102650331/169701509-0af996ca-e6c3-43a7-9e97-efd629e7252a.png)

# st.text

```python
import streamlit as st

st.text("This is some text.")

```
![image](https://user-images.githubusercontent.com/102650331/169701552-c13c34fe-15c6-409a-a45d-27565658e58f.png)

# st.latex

```python
import streamlit as st

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

```
![image](https://user-images.githubusercontent.com/102650331/169701593-6e82f101-9873-48d1-8fb1-1e1454c9ae4e.png)



