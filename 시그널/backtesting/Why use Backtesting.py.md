# 참조
- https://greyhoundanalytics.com/blog/backtestingpy-a-complete-quickstart-guide/

# The simplest backtest
## 설치
```
!pip install backtesting
!pip install pandas-ta

```

## 라이브러리 로딩
```python
import datetime
import pandas_ta as ta
import pandas as pd

from backtesting import Backtest
from backtesting import Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG

```

## 매매 전략 클래스
```python
class RsiOscillator(Strategy):
    """
    rsi가 upper_bound를 상향 돌파하면 포지션 정리(매도 포지션)
    rsi가 lower_bound를 하향 돌파하면 매수 포지션
    """

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    # Do as much initial computation as possible
    # 전략 실행에 필요한 각종 연산을 이 함수에서 수행
    def init(self):
        self.rsi = self.I(ta.rsi, pd.Series(self.data.Close), self.rsi_window)

    # Step through bars one by one
    # Note that multiple buys are a thing here
    # 일자별 캔들 각각에 대해서 아래 함수 실행
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            # 이전에 실행한 모든 주문을 취소 처리
            # 매도
            # 포지션 청산
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            # 매수
            self.buy()

```

## 매매 전략 백테스팅
```python
bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)
stats = bt.run()
bt.plot()

```

![image](https://user-images.githubusercontent.com/102650331/181919786-eb8662c1-5512-4fec-890d-6e6fe3afe631.png)

```python
stats

```
![image](https://user-images.githubusercontent.com/102650331/181919823-62292b46-1ee1-45a3-8117-501a2a82f646.png)

# Parameter optimization
- 클래스 변수에 대해서 최적화를 수행한다.
- grid-search to find the best portfolio for whatever metric you've defined.

```python
stats=bt.run()

```
위의 코드를 아래와 같이 변경
```python
# maximize 변수는 stats dataframe에 정의된 지표값을 활용
# optimizer는 값이 높은 것을 좋은 결과로 가정한다.

stats = bt.optimize(
        upper_bound = range(50,85,5),
        lower_bound = range(15,45,5),
        rsi_window = range(10,30,2),
        maximize = "Equity Final [$]")

```


![image](https://user-images.githubusercontent.com/102650331/181920103-fd4fbc34-60eb-43bd-a5dd-d216490cb4b1.png)

```python
stats

```
![image](https://user-images.githubusercontent.com/102650331/181920159-eaecf6bb-5487-4d58-821f-09f28011857e.png)


```python
stats.keys()

```
![image](https://user-images.githubusercontent.com/102650331/181920549-4e5d5e86-b598-4068-8087-d81872dc2290.png)

```python
# stats 변수는 best performing set of parameters의 값을 가지고 있다.
strategy = stats["_strategy"]
strategy.upper_bound
strategy.lower_bound

```
![image](https://user-images.githubusercontent.com/102650331/181920628-b9355499-6821-4f69-af0b-9fc7b32cba16.png)


# Custom Optimization Functions
```python
def optim_func(series):
    # 10번 이하의 거래면 백테스팅 case는 최적화 결과에서 제외
    if series["# Trades"] < 10:
        return -1
    else:
        # 얼마나 짧은 시간에 많은 수익을 창출했는지 측정
        return series["Equity Final [$]"]/series["Exposure Time [%]"]

```

```python
stats = bt.optimize(
        upper_bound = range(50,85,5),
        lower_bound = range(15,45,5),
        rsi_window = range(10,30,2),
        maximize=optim_func)

```

# Parameter Heatmaps
- which parameter combinations perform best

```python
import matplotlib.pyplot as plt
import seaborn as sns
...
class RsiOscillator(Strategy):
    ...
...

bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)

stats, heatmap = bt.optimize(
        upper_bound = range(50,85,5),
        lower_bound = range(15,45,5),
        rsi_window = range(10,30,2),
        maximize='Equity Final [$]',
        return_heatmap=True)

# choose your colormaps from here
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
hm = heatmap.groupby(["upper_bound","lower_bound"]).mean().unstack()
sns.heatmap(hm, cmap="plasma")
plt.show()

```
![image](https://user-images.githubusercontent.com/102650331/181924528-12fd791f-c41c-42f2-898d-f3ddaed70ce8.png)

