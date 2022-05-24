```python
import streamlit as st

@st.cache
def get_data(url):
    return pd.read_csv(url)

@st.cache
def get_co2_data(): 
    # OWID Data on CO2 and Greenhouse Gas Emissions
    # Creative Commons BY license
    url = 'https://github.com/owid/co2-data/raw/master/owid-co2-data.csv'
    return get_data(url)

@st.cache
def get_warming_data():
    # OWID Climate Change impacts
    # Creative Commons BY license
    url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Climate%20change%20impacts/Climate%20change%20impacts.csv'
    return get_data(url).query("Entity == 'World' and Year <=2021")

```
