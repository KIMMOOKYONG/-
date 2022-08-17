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
