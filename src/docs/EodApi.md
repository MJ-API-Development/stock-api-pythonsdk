# Intelligent Stock Market API 
## EOD API

All URIs are relative to *https://gateway.eod-stock-api.site/api*
Note that if you prefer you can just call this endpoints using your preferred method 
e.g python requests module in which case you will have to supply your api_key togather with the http request as a path parameter 

| Method                                                                                             | HTTP request                                         | Description |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------|-------------|
| [**v1_eod_date_exchange_code_get**](EodApi.md#v1_eod_date_exchange_code_get)                       | **GET** /v1/eod/{_date}/{exchange_code}              |             |
| [**v1_eod_date_exchange_code_stock_code_get**](EodApi.md#v1_eod_date_exchange_code_stock_code_get) | **GET** /v1/eod/{_date}/{exchange_code}.{stock_code} |             |
| [**v1_eod_from_to_exchange_code_get**](EodApi.md#v1_eod_from_to_exchange_code_get)                 | **GET** /v1/eod/{_from}.{_to}/{exchange_code}        |             |
| [**v1_eod_from_to_stock_code_get**](EodApi.md#v1_eod_from_to_stock_code_get)                       | **GET** /v1/eod/{_from}.{_to}/{stock_code}           |             |

# **EOD Data By Exchange Code & By Date**


will return end of day data for a certain exchange on a specific date identified by exchange code

### Example

```python
from __future__ import print_function
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    api_key = "API KEY"
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.EodApi(api_client)
    date = '222-01-02' # str | YYYY-MM-DD
    exchange_code = 'TO' # str |  Exchange Code For Toronto Stock Exchange

    try:
        api_response = api_instance.v1_eod_date_exchange_code_get(date, exchange_code)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception : {e}")

```

### Parameters

| Name              | Type    | Description    | Notes |
|-------------------|---------|----------------|-------|
| **date**          | **str** | **YYYY-MM-DD** |       |
| **exchange_code** | **str** |                |       |

### Return type

[**EODStockResponse**](EODStockResponse.md)

### Authorization

api_key : str -> can be obtained from our website at https://eod-stock-api.site

### HTTP request headers

 - **Content-Type**: "application/json"
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     | OK          | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **EOD Data By Exchange & Stock Code**

will return end of day data for a certain stock at a given date

### Example

```python
from __future__ import print_function
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    api_key = "API KEY", # Obtain an API Key from our website at https://eod-stock-api.site/login#signup
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.EodApi(api_client)
    date = '2022-01-02' # str | Format YYYY-MM-DD 
    exchange_code = 'TO' # str | See SExchange API in order to obtain Exchange Codes
    stock_code = 'AAPL' # str | Ticker Symbol for the stock you want to check EOD Data for 
    try:
        api_response = api_instance.v1_eod_date_exchange_code_stock_code_get(date, exchange_code, stock_code)
        pprint(api_response)
    except ApiException as e:
        print(f"Exception : {e}")
```

### Parameters

| Name              | Type    | Description    | Notes                                     |
|-------------------|---------|----------------|-------------------------------------------|
| **date**          | **str** | **YYYY-MM-DD** | Date Formatted String                     |
| **exchange_code** | **str** | TO             | Toronto Exchange Canada                   |
| **stock_code**    | **str** | AAPL           | Ticker Symbol as listed on Stock Exchange |

### Return type

[**EODStockResponse**](EODStockResponse.md)

### Authorization

api_key **str** -> can be obtained from our website at https://eod-stock-api.site

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     | Status OK   | -                |  

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **EOD Data By Exchange taken from one Date to Another**


return a list of eod historical data on exchange_code from one date to the other

### Example

```python
from __future__ import print_function
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    api_key = "API KEY"
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.EodApi(api_client)
    exchange_code = 'exchange_code_example' # str | 
    _to = 'to_example' # str | 
    _from = '_from_example' # str | 

    try:
        api_response = api_instance.v1_eod_from_to_exchange_code_get(exchange_code, _to, _from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi: {}".format(e))
```

### Parameters

| Name              | Type    | Description | Notes       |
|-------------------|---------|-------------|-------------|
| **exchange_code** | **str** |             |             |
| **_to**           | **str** | YYYY-MM-DD  | Date String |
| **_from**         | **str** | YYYY-MM-DD  | Date String |

### Return type

[**EODStockListResponse**](EODStockListResponse.md)

### Authorization

api_key -> can be obtained from our website at https://eod-stock-api.site

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     | Status OK   | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **EOD Data For a Company Taken By Stock Code , from one Date to Another**




Will return end of day data for a certain stock at a given date range , given by to and from field

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    api_key = "API Key" 
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.EodApi(api_client)
    stock_code = 'MSFT' # str | 
    _to = '2023-01-01' # str | 
    _from = '2022-01-01' # str | 

    try:
        api_response = api_instance.v1_eod_from_to_stock_code_get(stock_code, _to, _from)
        pprint(api_response)
    except ApiException as e:
        print("Exception : {}".format(e))

```

### Parameters

| Name           | Type    | Description       | Notes |
|----------------|---------|-------------------|-------|
| **stock_code** | **str** | **Ticker Symbol** |       |
| **_to**        | **str** | **YYYY-MM-DD**    |       |
| **_from**      | **str** | **YYYY-MM-DD**    |       |

### Return type

[**EODStockResponse**](EODStockResponse.md)

### Authorization

api_key -> can be obtained from our website at https://eod-stock-api.site

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     | Success     | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

