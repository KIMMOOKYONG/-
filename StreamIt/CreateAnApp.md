# Create your first app
- 스크립트 파일 생성
- 라이브러리 로딩
- 스크립트 작성
- 실행
- 결과 확인 및 수정 등

```python
# uber_pickups.py

import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in NYC")


```

![image](https://user-images.githubusercontent.com/102650331/169686010-df8b217b-6d42-466c-9a33-79ac26177094.png)

![image](https://user-images.githubusercontent.com/102650331/169686407-a148a995-0832-446b-bb8d-7814a5c02c62.png)

```python
# uber_pickups.py

import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in NYC")

DATE_COLUMN = "date/time"
DATA_URL = ("https://s3-us-west-2.amazonaws.com/"
                "streamlit-demo-data/uber-raw-data-sep14.csv.gz")

def load_data(nrows):

    """
    @nrows: 데이터프레임에서 추출한 레코드 숫자
    """

    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

```

![image](https://user-images.githubusercontent.com/102650331/169686499-a236d278-94df-47e8-b9f6-28eba331e02a.png)

