# Initialize values in Session State

```python
# Initialization
if "key" not in st.session_state:
    st.session_state["key"] = "value"

# Session State also supports attribute based syntax
if "key" not in st.session_state:
    st.session_state.key = "value"

```

# Reads and updates

```python
# Read
st.write(st.session_state.key)
# Outputs: value

st.session_state.key = "value2"     # Attribute API
st.session_state["key"] = "value2"  # Dictionary like API

st.write(st.session_state)

# With magic:
st.session_state

st.write(st.session_state["value"])

# Throws an exception!

```

# Delete items

```python
# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]

```

# Session State and Widget State association

```python
st.text_input("Your name", key="name")

# This exists now:
st.session_state.name

```

# Forms and Callbacks

```python
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key="my_form"):
    slider_input = st.slider("My slider", 0, 10, 5, key="my_slider")
    checkbox_input = st.checkbox("Yes or No", key="my_checkbox")
    submit_button = st.form_submit_button(label="Submit", on_click=form_callback)

```

# Caveats and limitations

```python
slider = st.slider(
    label="My Slider", min_value=1,
    max_value=10, value=5, key="my_slider")

st.session_state.my_slider = 7

# Throws an exception!

st.session_state.my_slider = 7

slider = st.slider(
    label="Choose a Value", min_value=1,
    max_value=10, value=5, key="my_slider")

if "my_button" not in st.session_state:
    st.session_state.my_button = True

st.button("My button", key="my_button")

# Throws an exception!


```
