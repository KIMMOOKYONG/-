# PCA는 무엇이며 언제 사용하는가?
- (주성분분석설명)https://www.youtube.com/watch?v=FgakZw6K1QQ
- (공분산 행렬의 의미와 PCA)https://www.youtube.com/watch?v=jNwf-JUGWgg
-  주성분은 내가 원래 가지고 있는 데이터와 다르다. 변환된 데이터이다.
-  따라서, 원래 변수가 가지고 있는 의미 즉 열의 의미가 중요한 경우에는 PCA를 사용하면 안 된다. 왜냐하면, 위에서 말했듯이 PCA는 데이터에 변환을 가하는 것이기 때문이다.
 
# 그렇다면, 언제 PCA를 사용해야 하는가? 
- PCA의 본질은 탐색적 분석이다. 즉, 변인을 탐색해서 변환을 통해 주성분을 결정하는 방법이다. 

# 주성분은 무엇인가? 
![image](https://user-images.githubusercontent.com/102650331/171083002-3842eadd-a2a1-41a4-97d0-747749169f6d.png)

- 만약, 2개의 변수로도 4개(전체)의 변수의  분산에 대해 설명할 수 있다면 target을 분류할 때 2개만 사용하면 되지 않을까? 
- 주성분이란 전체 데이터(독립변수들)의 분산을 가장 잘 설명하는 성분이라고 할 수 있다. 
- 하나의 변수는 하나의 차원을 의미한다.
- 4개 독립변수를 하나의 공간에 표현하기 위해서는 그 공간이 4차원 이어야 한다.
- http://thesciencelife.com/archives/1001
- 차원이 커질수록 해를 구하기 위한 방정식이 늘어난다.
- 데이터 샘플의 수가 작으면 해 공간이 불안정해진다.
- 해 공간이 불안정해진다는 것은 회귀로 보자면 계수의 신뢰 구간이 넓어지는 것으로 말할 수 있다.
- 변수가 너무 많아 이들 중 중요하다고 판단되는 변수들 몇 개만 뽑아 모델링을 하려고 할 때 주로 PCA를 사용한다.

# PCA with Python 
```python
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=["sepal length","sepal width","petal length","petal width","target"])
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/171083965-fa9b3cfd-8046-4217-a301-839871f47c8c.png)

# 표준화 
- pca를 하기 전에 데이터 스케일링을 하는 이유는 데이터의 스케일에 따라 주성분의 설명 가능한 분산량이 달라질 수 있기 때문이다. 
![image](https://user-images.githubusercontent.com/102650331/171084084-bb49bfd3-5d4e-486b-a4c0-42589b2f6f69.png)

- 따라서, scale을 하지 않으면 변인이 가진 값의 크기에 따라 설명 가능한 분산량이 왜곡될 수 있기 때문에 반드시 표준화를 해주어야 한다. 

- 표준화된 데이터
```python
from sklearn.preprocessing import StandardScaler  # 표준화 패키지 라이브러리 
x = df.drop(["target"], axis=1).values # 독립변인들의 value값만 추출
y = df["target"].values # 종속변인 추출

x = StandardScaler().fit_transform(x) # x객체에 x를 표준화한 데이터를 저장

features = ["sepal length", "sepal width", "petal length", "petal width"]
pd.DataFrame(x, columns=features).head()

```
![image](https://user-images.githubusercontent.com/102650331/171084461-6ff53ed3-b2c3-4fed-9328-671f83e7ad99.png)



