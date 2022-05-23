# st.button
- Display a button widget.

```python
import streamlit as st

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

```
![image](https://user-images.githubusercontent.com/102650331/169781981-ee0033a9-0fed-4953-a2d3-be07e8c93e4a.png)

```python
import streamlit as st

st.title("Making a Button")
result = st.button("Click Here")
st.write(result)

if result:
    st.write(":smile:")

```
![image](https://user-images.githubusercontent.com/102650331/169782130-b977b1cc-c32d-4f80-aff1-4af8f413ffaa.png)

```python
import streamlit as st

st.title("Radio Buttons, Checkboxes and Buttons")
page_names = ["Checkbox", "Button"]
page = st.radio("Navigation", page_names)
st.write("**The variable 'page' returns:**", page)

```
![image](https://user-images.githubusercontent.com/102650331/169783319-123dd9f5-da0e-464e-b9d4-5630cb38cf99.png)

```python
import streamlit as st

st.title("Radio Buttons, Checkboxes and Buttons")
page_names = ["Checkbox", "Button"]
page = st.radio("Navigation", page_names)
st.write("**The variable 'page' returns:**", page)

if page == "Checkbox":
    st.subheader("Welcome to the Checkbox page!")
    st.write("Nice to see you! :wave:")
else:
    st.subheader("Welcome to the Button page!")
    st.write(":thumbsup:")

```
![image](https://user-images.githubusercontent.com/102650331/169784206-f20ce209-555f-4726-bcde-bdc2922a9c26.png)
