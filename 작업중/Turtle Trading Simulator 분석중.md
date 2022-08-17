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


