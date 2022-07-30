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
