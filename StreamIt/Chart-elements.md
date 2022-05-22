# st.line_chart

```python
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=["a", "b", "c"])

st.line_chart(chart_data)

```
![image](https://user-images.githubusercontent.com/102650331/169702326-37b26294-708f-4305-b7ae-85eb1fae837d.png)

# st.area_chart

```python
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=["a", "b", "c"])

st.area_chart(chart_data)

```
![image](https://user-images.githubusercontent.com/102650331/169702379-f66992c1-f3f6-4752-8993-83c94e3cc088.png)

# st.bar_chart

```python
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

```
![image](https://user-images.githubusercontent.com/102650331/169702435-c1fbbb84-2426-4eaa-8d4a-9ba220076328.png)

# st.pyplot

```python
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

```
![image](https://user-images.githubusercontent.com/102650331/169702510-456ae214-76da-4dbd-b20c-3e8b7a67ecc5.png)

# st.altair_chart

```python
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=["a", "b", "c"])

c = alt.Chart(df).mark_circle().encode(
     x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])

st.altair_chart(c, use_container_width=True)

```
![image](https://user-images.githubusercontent.com/102650331/169702588-863c1dc1-3859-4ba1-a8fa-9ab069be5775.png)

# st.vega_lite_chart

```python
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=["a", "b", "c"])

st.vega_lite_chart(df, {
     "mark": {"type": "circle", "tooltip": True},
     "encoding": {
         "x": {"field": "a", "type": "quantitative"},
         "y": {"field": "b", "type": "quantitative"},
         "size": {"field": "c", "type": "quantitative"},
         "color": {"field": "c", "type": "quantitative"},
     },
 })

```
![image](https://user-images.githubusercontent.com/102650331/169702945-f2185f8b-1343-46d3-8ae7-581eff1e1b7b.png)

