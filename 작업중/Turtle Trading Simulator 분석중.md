# Turtle Trading Simulator 분석 중

# 변수 선언
```python
# For the end user, change the parameters below and run script:
stock = 'NFLX'              # choose your stock here
start_date = '2016-06-01'   # choose your initial investment date
end_date = '2020-09-01'      # choose your exit date
investment_dollars = 80000  # choose the total dollars to invest

```
# 모듈 설치
```python
# install Pint if necessary
try:
    import pint
except ImportError:
    !pip install pint
    
# download modsim.py if necessary

from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)
    
download('https://raw.githubusercontent.com/AllenDowney/' +
         'ModSimPy/master/modsim.py')
         
# yfinance library
try:
    import yfinance
except ImportError:
    !pip install yfinance
    
# yahoofinancials library
try:
    import yahoofinancials
except ImportError:
    !pip install yahoofinancials   
    
```

# 라이브러리 로딩
```python
from modsim import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from yahoofinancials import YahooFinancials

```

# 단일 종목 데이터프레임 생성
```python
# function that will create a dataframe for a single stock
def create_stock_df(stock, start, end, SMA):
    '''
    stock(종목명), start(시작일), end(종료일), SMA(이동평균 기간)
    '''
    # get the data from yahoo finance
    df = yf.download(stock, 
                     start=start, 
                     end=end, 
                     progress=False)
    
    # add extra columns for day, stock title,
    # simple moving average, and closing price average difference
    df['day'] = range(1, len(df) + 1)
    df['stock'] = stock
    # 종가 칼럼을 기준으로 이동평균 계산
    df['SMA_x'] = df.iloc[:,4].rolling(window=SMA).mean()
    # 전일 종가
    df['shifted_close'] = df['Close'].shift(1)
    # 금일 종가와 전일 종가의 차이
    df['close_difference'] = df['Close'] - df['shifted_close']
    
    # reset the index
    df = df.reset_index()
    
    # return the dataframe
    return df

```

# create_stock_df(stock, start, end, SMA) 호출 예시
```python
entry_signal = 55
df = create_stock_df(stock, start_date, end_date, entry_signal)
df

```
![image](https://user-images.githubusercontent.com/102650331/185061789-fa9579a8-76b8-499e-b2a8-ea2f00a37e34.png)

# 종가 데이터 시각화
```python
# function to plot the stock dataframe's closing prices
def plot_stock_price(df):
    
    x = df['Date']
    y = df['Close']

    # plotting the points  
    plt.plot(x, y) 

    # naming the axes 
    plt.xlabel('date')
    plt.ylabel('price/share')

    # rotate the tick marks
    plt.xticks(rotation=70)

    # title
    plt.title('Stock Price over time') 

    # function to show the plot 
    plt.show()

```

# plot_stock_price(df) 호출 예시
```python
plot_stock_price(df)

```
![image](https://user-images.githubusercontent.com/102650331/185068317-e9d56f91-d989-4a44-b3c1-ae9452021565.png)


# state object 생성
```python
# create a function that defines a state object
# for financial information that will change during simulation

# input your:
# 1. total dollars to invest
# 2. your entry signal in days
# 3. your exit signal (based on N, i.e. .5N)
def create_state_object(dollars, entry, exit):

    financial_state = State(dollars = dollars,
                           shares = 0,
                           total_value = dollars,
                           x_day_high = 0,
                           x_day_low = 0,
                           current_price = 0,
                           ATR = 0,
                           SMA_x = 0,
                           x = entry,
                           exit_x = exit,
                           status = 'out',
                           entry_price = 0,
                           exit_price = 0)
    
    return financial_state

```

# create_state_object(dollars, entry, exit) 호출 예시
```python
investment_dollars = 50000,
entry_signal = 55,
exit_signal = 1

create_state_object(investment_dollars, entry_signal, exit_signal)

```
![image](https://user-images.githubusercontent.com/102650331/185069229-b67fac7d-fa91-4815-a1fc-0bc239937635.png)

# 시스템 파라미터 생성(변경 안됨, 상수)
```python
# function that will create a system of parameters (that will not change during simulation)
# Modeling and Simulation in Python
# https://rpubs.com/zahirf/630705
# https://greenteapress.com/modsimpy/ModSimPy3.pdf
def make_system(df, state, starting_dollars,
                unit_size, add_unit_signal):
    
    return System(t_0 = get_first_label(df),
                  t_end = get_last_label(df),
                  starting_dollars = starting_dollars,
                  unit_size = starting_dollars*unit_size,
                  add_unit_signal = add_unit_signal,
                  entry_signal = state.x,
                  exit_signal = state.exit_x,
                  stock = get_first_value(df['stock']),
                  financials = state)

```

# make_system 예시
```python
stock = 'GOOG'
start_date = '2014-01-01'
end_date = '2020-02-01'
investment_dollars = 50000
entry_signal = 55
exit_signal = 1
unit_size = 0.1
add_unit_signal = .5

```

```python
# create stock dataframe
TT_df = create_stock_df(stock, start_date, end_date, entry_signal)
TT_df

```
![image](https://user-images.githubusercontent.com/102650331/185075865-dbfc323d-13b7-4aad-9eaa-98f3033b1855.png)


```python
# create financial state object
TT_financial_state = create_state_object(investment_dollars, entry_signal, exit_signal)
TT_financial_state

```
![image](https://user-images.githubusercontent.com/102650331/185076048-eef3e963-cd01-408e-b90b-9c4e54ad58dc.png)





