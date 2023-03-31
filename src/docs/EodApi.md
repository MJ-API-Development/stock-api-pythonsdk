# src.IntelligentStockMarketAPI.EodApi

All URIs are relative to *https://gateway.eod-stock-api.site/api*

| Method                                                                                             | HTTP request                                         | Description |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------|-------------|
| [**v1_eod_date_exchange_code_get**](EodApi.md#v1_eod_date_exchange_code_get)                       | **GET** /v1/eod/{_date}/{exchange_code}              |             |
| [**v1_eod_date_exchange_code_stock_code_get**](EodApi.md#v1_eod_date_exchange_code_stock_code_get) | **GET** /v1/eod/{_date}/{exchange_code}.{stock_code} |             |
| [**v1_eod_from_to_exchange_code_get**](EodApi.md#v1_eod_from_to_exchange_code_get)                 | **GET** /v1/eod/{_from}.{_to}/{exchange_code}        |             |
| [**v1_eod_from_to_stock_code_get**](EodApi.md#v1_eod_from_to_stock_code_get)                       | **GET** /v1/eod/{_from}.{_to}/{stock_code}           |             |

# **v1_eod_date_exchange_code_get**
> EODStockResponse v1_eod_date_exchange_code_get(date, exchange_code)



will return end of day data for a certain stock at a given date

### Example

```python
from __future__ import print_function
import time
import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = src.IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = src.IntelligentStockMarketAPI.EodApi(api_client)
    date = 'date_example' # str | 
exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_eod_date_exchange_code_get(date, exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_date_exchange_code_get: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **date**          | **str** |             |       |
| **exchange_code** | **str** |             |       |

### Return type

[**EODStockResponse**](EODStockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_eod_date_exchange_code_stock_code_get**
> EODStockResponse v1_eod_date_exchange_code_stock_code_get(date, exchange_code, stock_code)



will return end of day data for a certain stock at a given date

### Example

```python
from __future__ import print_function
import time
import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = src.IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = src.IntelligentStockMarketAPI.EodApi(api_client)
    date = 'date_example' # str | 
exchange_code = 'exchange_code_example' # str | 
stock_code = 'stock_code_example' # str | 
    try:
        api_response = api_instance.v1_eod_date_exchange_code_stock_code_get(date, exchange_code, stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_date_exchange_code_stock_code_get: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **date**          | **str** |             |       |
| **exchange_code** | **str** |             |       |
| **stock_code**    | **str** |             |       |

### Return type

[**EODStockResponse**](EODStockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_eod_from_to_exchange_code_get**
> EODStockListResponse v1_eod_from_to_exchange_code_get(exchange_code, to, _from)



return a list of eod historical data on exchange_code from one date to the other

### Example

```python
from __future__ import print_function
import time
import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = src.IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = src.IntelligentStockMarketAPI.EodApi(api_client)
    exchange_code = 'exchange_code_example' # str | 
to = 'to_example' # str | 
_from = '_from_example' # str | 

    try:
        api_response = api_instance.v1_eod_from_to_exchange_code_get(exchange_code, to, _from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_from_to_exchange_code_get: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **exchange_code** | **str** |             |       |
| **to**            | **str** |             |       |
| **_from**         | **str** |             |       |

### Return type

[**EODStockListResponse**](EODStockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_eod_from_to_stock_code_get**
> EODStockResponse v1_eod_from_to_stock_code_get(stock_code, to, _from)



will return end of day data for a certain stock at a given date

### Example

```python
from __future__ import print_function
import time
import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = src.IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = src.IntelligentStockMarketAPI.EodApi(api_client)
    stock_code = 'stock_code_example' # str | 
to = 'to_example' # str | 
_from = '_from_example' # str | 

    try:
        api_response = api_instance.v1_eod_from_to_stock_code_get(stock_code, to, _from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_from_to_stock_code_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **to**         | **str** |             |       |
| **_from**      | **str** |             |       |

### Return type

[**EODStockResponse**](EODStockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

