# Add widgets to sidebar

```python
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

```
![image](https://user-images.githubusercontent.com/102650331/169935948-f33fb453-d097-447c-83ba-5d6f817f1726.png)

