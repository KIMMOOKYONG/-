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

# st.plotly_chart

```python
import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ["Group 1", "Group 2", "Group 3"]

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

```
![image](https://user-images.githubusercontent.com/102650331/169703056-e8dcc98c-927f-4f49-8780-0b82bbdf7e5e.png)

# st.bokeh_chart

```python
import streamlit as st
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

```
![image](https://user-images.githubusercontent.com/102650331/169703124-99320ffb-0e77-41fe-9ce9-f1c77abc728a.png)

# st.pydeck_chart
# st.graphviz_chart
# st.map
