# Turtle Trading Simulator 분석 중

```
# 모듈 설치
```python
# install Pint if necessary
!pip install pint

# yfinance library
!pip install yfinance

# yahoofinancials library
!pip install yahoofinancials 

!pip install modsimpy

```
# 라이브러리 로딩
```python
from modsim import *
import pint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from yahoofinancials import YahooFinancials

```
![image](https://user-images.githubusercontent.com/102650331/185079587-e7d9b1ae-d7de-482f-8bce-d37c3d824c2c.png)


# 변수 선언
```python
# For the end user, change the parameters below and run script:
stock = 'NFLX'              # choose your stock here
start_date = '2016-06-01'   # choose your initial investment date
end_date = '2020-09-01'      # choose your exit date
investment_dollars = 80000  # choose the total dollars to invest

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
    
    return System(t_0 = get_first_label(df),  # 시작 번호
                  t_end = get_last_label(df), # 마지막 번호
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

```python
# create system object
TT_system = make_system(TT_df, TT_financial_state, investment_dollars,
                     unit_size, add_unit_signal)
TT_system

```
![image](https://user-images.githubusercontent.com/102650331/185089837-c6c37e8f-adf4-4512-b842-7b7251b44462.png)


# run_simulation(df, system, update_func)
```python
# define run simulation function that stores results in a TimeFrame
def run_simulation(df, system, update_func):
    
    # create a TimeFrame to keep track of financials over time
    frame = TimeFrame(columns = system.financials.index)
    frame.row[system.t_0] = system.financials
    
    # run the simluation for every day in the date range
    for t in linrange(system.t_0, system.t_end):
        frame.row[t+1] = update_func(df, frame.row[t], t, system)
        
    return frame

```

```python
system.financials
```
![image](https://user-images.githubusercontent.com/102650331/185104428-7517ec1f-fa6d-4f26-808a-02d50e1fac01.png)


```python
frame = TimeFrame(columns = system.financials.index)
frame
```
![image](https://user-images.githubusercontent.com/102650331/185104568-36754c53-22ec-4126-9146-1de7d881b166.png)


```python
frame.row[TT_system.t_0] = TT_system.financials
frame.row[TT_system.t_0]

```
![image](https://user-images.githubusercontent.com/102650331/185104673-8c09e84f-51fd-4343-97ec-84797ffd858c.png)


```python
update_func(TT_df, frame.row[0], 0, system)

```

```python
# The update function takes the state during the current time step
# and returns the state during the next time step.
def update_func(df, state, t, system):

    d = state.dollars
    shares = state.shares
    #current_price = state.current_price
    x = state.x
    exit_x = state.exit_x
    status = state.status
    entry_price = state.entry_price
    exit_price = state.exit_price
    add_unit_signal = system.add_unit_signal
    
    if t <= x+2:
        
        xdh = max(df['Close'][1:x])
        xdl = min(df['Close'][1:x])
        sma_x = df['SMA_x'][t]
        atr = (xdh - xdl)/1.5
        current_price = df['Close'][t]
        
    if t > x+2:
        
        xdh = max(df['Close'][t-x:t+1])
        xdl = min(df['Close'][t-x:t+1])
        sma_x = df['SMA_x'][t]
        atr = (xdh - xdl)/1.5
        current_price = df['Close'][t]
        
        # if you see the entry signal and you're out
        if current_price >= xdh and status == 'out':
            
            entry_price = current_price
            shares = (system.unit_size)//(entry_price)
            d = d - ((system.unit_size)//(entry_price)) * entry_price
            status = 'in'
        
        # if you see the add unit signal and you're already in
        elif (status == 'in') and (current_price > (entry_price + (atr*add_unit_signal))) and (d > current_price):
            
            entry_price = current_price
            shares = shares + (system.unit_size)//(entry_price)
            d = d - ((system.unit_size)//(entry_price)) * entry_price
            status = 'in'
        
        # if you're in and you see the exit signal
        elif (current_price < (sma_x - (atr*exit_x))) and (status == 'in'):
            
            exit_price = current_price
            d = d + (shares * exit_price)
            shares = 0
            status = 'out'
        
        # you're just cruisin
        else:
            
            entry_price = entry_price
            exit_price = exit_price
            shares = shares
            d = d
        
    return State(dollars = d,
                 shares = shares,
                 total_value = d + (shares*current_price),
                 x_day_high = xdh,
                 x_day_low = xdl,
                 current_price = current_price,
                 ATR = atr,
                 SMA_x = sma_x,
                 x = x,
                 exit_x = exit_x,
                 status = status,
                 entry_price = entry_price,
                 exit_price = exit_price)

```


