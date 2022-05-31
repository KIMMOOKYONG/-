# 참조
- https://m.blog.naver.com/tjdrud1323/221720259834
- 
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
- <span style="color:red">**주성분이란 전체 데이터(독립변수들)의 분산을 가장 잘 설명하는 성분이라고 할 수 있다.**</span> 
- 하나의 변수는 하나의 차원을 의미한다.
- 4개 독립변수를 하나의 공간에 표현하기 위해서는 그 공간이 4차원 이어야 한다.
- http://thesciencelife.com/archives/1001
- 차원이 커질수록 해를 구하기 위한 방정식이 늘어난다.
- 데이터 샘플의 수가 작으면 해 공간이 불안정해진다.
- 해 공간이 불안정해진다는 것은 회귀로 보자면 계수의 신뢰 구간이 넓어지는 것으로 말할 수 있다.
- 변수가 너무 많아 이들 중 중요하다고 판단되는 변수들 몇 개만 뽑아 모델링을 하려고 할 때 주로 PCA를 사용한다.
- **전체 데이터(독립변수들)의 분산을 가장 잘 설명하는 축의 개수를 선정해서 그 축에 따라 변형된 데이터를 배열하면 그 데이터가 주성분이 된다. 다시 한번 말하지만, 주성분은 원래의 데이터와 다르다.**
- 

# PCA with Python 
```python
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names=["sepal length","sepal width","petal length","petal width","target"])
data.head()

```
![image](https://user-images.githubusercontent.com/102650331/171083965-fa9b3cfd-8046-4217-a301-839871f47c8c.png)

# 표준화 
- pca를 하기 전에 데이터 스케일링을 하는 이유는 데이터의 스케일에 따라 주성분의 설명 가능한 분산량이 달라질 수 있기 때문이다. 
![image](https://user-images.githubusercontent.com/102650331/171084084-bb49bfd3-5d4e-486b-a4c0-42589b2f6f69.png)

- 표준화가 모델 성능에 미치는 영향
![image](https://user-images.githubusercontent.com/102650331/171084639-d09af2fc-3d95-4660-9e0e-efd3ffd0041a.png)

- 따라서, scale을 하지 않으면 변인이 가진 값의 크기에 따라 설명 가능한 분산량이 왜곡될 수 있기 때문에 반드시 표준화를 해주어야 한다. 

- 표준화된 데이터
```python
from sklearn.preprocessing import StandardScaler  # 표준화 패키지 라이브러리 
x = df.drop(["target"], axis=1).values # 독립변인들의 value값만 추출
y = df["target"].values # 종속변인 추출

x = StandardScaler().fit_transform(x) # x객체에 x를 표준화한 데이터를 저장

features = ["sepal length", "sepal width", "petal length", "petal width"]
df = pd.DataFrame(x, columns=features).head()
df.head()

```
![image](https://user-images.githubusercontent.com/102650331/171084461-6ff53ed3-b2c3-4fed-9328-671f83e7ad99.png)


# PCA 실행
```python
finalDf = pd.concat([principalDf, data], axis=1)

```

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2) # 주성분을 몇개로 할지 결정
printcipalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=printcipalComponents, columns = ["principal component1", "principal component2"])
# 주성분으로 이루어진 데이터 프레임 구성
principalDf.head()

```
![image](https://user-images.githubusercontent.com/102650331/171084845-8f0217ac-0e1e-4638-be2d-213884ceac46.png)


# 도대체 어떤 이유를 근거로 주성분을 2개로 결정하는가? 
![image](https://user-images.githubusercontent.com/102650331/171085013-757018e3-fa55-49ce-a1a2-d2c145a4ff45.png)
-본 그래프에서 주성분 6개일 때, 누적 설명 분산량이 73%이기 때문에 주성분을 6개로 결정하였다.

## 전체에서 해당 주성분의 고윳값이 차지하는 비율을 알아보는 것이다.  
```python
pca.explained_variance_ratio_
# array([0.72770452, 0.23030523])

```

## 두개의 주성분이 전체 데이터의 분산에 대한 설명하는 정도
```python
sum(pca.explained_variance_ratio_)
# 0.9580097536148197

```
- pca에서 위와 같은 코드로 간단하게 내가 설정한 주성분의 개수(n_components)로 전체 데이터의 분산을 얼마만큼 설명 가능한지 알 수 있다.
- 본 데이터의 경우 두 개의 주성분이 전체 분산의 약 96%를 설명한다. 

## 분석 결과, 3번째 주성분의 분산 설명량은 0.03밖에 되지 않는 것을 알 수 있다. 
```python
pca = PCA(n_components=3)
printcipalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=printcipalComponents, columns = ["principal component1", "principal component2", "3"])
pca.explained_variance_ratio_
# array([0.72770452, 0.23030523, 0.03683832])

# 혹시나 궁금하신 분들을 위해 n_components=3으로 분석을 진행해봤다. 분석 결과, 3번째 주성분의 분산 설명량은 0.03밖에 되지 않는 것을 알 수 있다. 
# 따라서, 추가적인 주성분을 투입하더라도 설명 가능한 분산량이 얼마 증가하지 않기 때문에 주성분은 두 개로 결정하는 것이 적절하다고 할 수 있다. 

```

# 두 개의 주성분을 이용한 iris species 시각화
- 이제 두 개의 주성분을 이용하여 iris 데이터의 species가 어떤 식으로 표현되는지 그래프를 이용하여 확인해보자. 

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("Principal Component 1", fontsize = 15)
ax.set_ylabel("Principal Component 2", fontsize = 15)
ax.set_title("2 component PCA", fontsize=20)

targets = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
colors = ["r", "g", "b"]
for target, color in zip(targets,colors):
    indicesToKeep = finalDf["target"] == target
    ax.scatter(finalDf.loc[indicesToKeep, "principal component1"]
               , finalDf.loc[indicesToKeep, "principal component2"]
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
```
![image](https://user-images.githubusercontent.com/102650331/171123332-cdb24675-6179-4594-9868-1b2f7ce18eaf.png)
