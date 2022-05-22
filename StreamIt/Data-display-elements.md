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

# st.metric

```python
import streamlit as st
import pandas as pd
import numpy as np

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

```
![image](https://user-images.githubusercontent.com/102650331/169702051-7be9a7ae-72cc-4a34-9315-e293af5422fb.png)

```python
import streamlit as st
import pandas as pd
import numpy as np

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

```
![image](https://user-images.githubusercontent.com/102650331/169702089-96023267-624f-4d32-98c5-6c6b07938e2d.png)

```python
import streamlit as st
import pandas as pd
import numpy as np

st.metric(label="Gas price", value=4, delta=-0.5,
     delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
     delta_color="off")

```
![image](https://user-images.githubusercontent.com/102650331/169702144-041393f8-8ef9-416f-aa64-7da4dd26217c.png)

# st.json

```python
import streamlit as st
import pandas as pd
import numpy as np

st.json({
     "foo": "bar",
     "baz": "boz",
     "stuff": [
         "stuff 1",
         "stuff 2",
         "stuff 3",
         "stuff 5",
     ],
 })

```
![image](https://user-images.githubusercontent.com/102650331/169702204-d7b50760-d061-4d06-9d35-fa55ea0be6fc.png)


