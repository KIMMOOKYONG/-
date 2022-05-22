# st.dataframe

```python
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

```
![image](https://user-images.githubusercontent.com/102650331/169701714-1b850bbc-4d42-4f15-bf8e-e69b2e44400d.png)

```python
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

# st.dataframe(df)  # Same as st.write(df)
st.dataframe(df, 200, 100)

```
![image](https://user-images.githubusercontent.com/102650331/169701748-8fdfdfc0-d76b-4ed2-8db9-c91dc05f63a0.png)

```python
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

```
![image](https://user-images.githubusercontent.com/102650331/169701827-b13330fa-830c-4925-9797-cd7cdd4ec9cb.png)

# st.table
- 전체 데이터가 출력된다.

```python
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

```
![image](https://user-images.githubusercontent.com/102650331/169701909-32055006-2990-4172-b3fe-f000926d32e4.png)

