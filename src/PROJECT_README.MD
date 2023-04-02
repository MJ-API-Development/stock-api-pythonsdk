# Intelligent EOD Stock Market API Python SDK

<h2>Intelligent EOD Stocks API</h2>
    <p>
        Intelligent Stock Market API provides end-of-day stock data worldwide, financial news, and financial social
        media trends for web application developers, researchers and service providers.
        The API covers over 150,000 tickers, stocks, mutual funds, and more from around the world.
        It offers information for any period, including daily, weekly.
    <ul>
        <li>Exchange Information</li>
        <li>Stock Tickers Data</li>
        <li>End of Day (EOD) Stock Data</li>
        <li>Fundamental Data</li>
        <li>Stock Options And Splits Data</li>
        <li>Financial News API</li>
        <li>Social Media Trend Data For Stocks</li>
        <li>Sentiment Analysis for News & Social Media</li>
    </ul>       
        The information provided covers more than 150 000 tickers, stocks, mutual funds and more around the world.
        we provide information for any period, including daily, weekly.
    </p>

- API version: v1
- Package version: 0.0.3

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

you can install directly from pypi - 
find our package at [Intelligent-Stock-Market-API](https://pypi.org/project/Intelligent-Stock-Market-API)

On Windows
```sh
    pip install Intelligent-Stock-Market-API
    
```

On Linux 
    you may need to run `pip` with root permission:
```sh
  sudo pip install Intelligent-Stock-Market-API
```


Then import the package:
```python
import IntelligentStockMarketAPI
```

### Setuptools


Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

On Windows
```sh
python setup.py install --user
```

On Linux
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import IntelligentStockMarketAPI
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:


#### Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
#### See configuration.py for a list of all supported configuration parameters.

### EOD Data By Exchange and Date  

```python
from __future__ import print_function

import time
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint

# To get your API KEY visit [Intelligent EOD Stock Market API](https://eod-stock-market-api.site/login) 
# and create your free acoount 
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY"
)

# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.EodApi(api_client)
    date = '2022-02-02' # str | 
    exchange_code = 'TO' # str | "Country"="Canada", "name": "Toronto Exchange", "operating_mic": "XTSE" 

    try:
        api_response = api_instance.v1_eod_date_exchange_code_get(date, exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_date_exchange_code_get: %s\n" % e)    
```


### Exchange Details with Complete Ticker List Endpoint
```python

from __future__ import print_function
import time
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY"
)
# To get your API KEY visit [Intelligent EOD Stock Market API](https://eod-stock-market-api.site/login)

# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.ExchangesApi(api_client)
    exchange_code = 'TO' # str | Toronto Exchange Canada 

    try:
        api_response = api_instance.v1_exchange_exchange_with_tickers_code_exchange_code_get(exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_exchange_with_tickers_code_exchange_code_get: %s\n" % e)
```

### Latest Financial News Feed
### This will return the latest financial news articles grouped by their related tickers

Get list of all News Upper Bound is an Integer indicating a total number of articles to return

```python
from __future__ import print_function
import time
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    upper_bound = 56 # int | 
    try:
        api_response = api_instance.v1_news_articles_bounded_upper_bound_get(upper_bound)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialNewsApi->v1_news_articles_bounded_upper_bound_get: %s\n" % e)
```
  

### Get Financial News Articles By Ticker

### Example

```python
from __future__ import print_function
import time
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_news_articles_by_ticker_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialNewsApi->v1_news_articles_by_ticker_stock_code_get: %s\n" % e)
```


## Documentation for API Endpoints

All URIs are relative to *https://gateway.eod-stock-api.site/api*
