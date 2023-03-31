# openapi_client.StocksApi

All URIs are relative to *http://https://gateway.eod-stock-api.site/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_stock_code_stock_code_get**](StocksApi.md#v1_stock_code_stock_code_get) | **GET** /v1/stock/code/{stock_code} | 
[**v1_stocks_country_country_get**](StocksApi.md#v1_stocks_country_country_get) | **GET** /v1/stocks/country/{country} | 
[**v1_stocks_currency_currency_get**](StocksApi.md#v1_stocks_currency_currency_get) | **GET** /v1/stocks/currency/{currency} | 
[**v1_stocks_exchange_code_exchange_code_get**](StocksApi.md#v1_stocks_exchange_code_exchange_code_get) | **GET** /v1/stocks/exchange/code/{exchange_code} | 
[**v1_stocks_exchange_id_exchange_id_get**](StocksApi.md#v1_stocks_exchange_id_exchange_id_get) | **GET** /v1/stocks/exchange/id/{exchange_id} | 
[**v1_stocks_get**](StocksApi.md#v1_stocks_get) | **GET** /v1/stocks | 
[**v1_stocks_post**](StocksApi.md#v1_stocks_post) | **POST** /v1/stocks | 


# **v1_stock_code_stock_code_get**
> StockResponse v1_stock_code_stock_code_get(stock_code)



given stock code return stock details

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_stock_code_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stock_code_stock_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_code** | **str**|  | 

### Return type

[**StockResponse**](StockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stocks_country_country_get**
> StockListResponse v1_stocks_country_country_get(country)



returns a list of stocks listed in a certain country

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    country = 'country_example' # str | 

    try:
        api_response = api_instance.v1_stocks_country_country_get(country)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stocks_country_country_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 

### Return type

[**StockListResponse**](StockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stocks_currency_currency_get**
> StockListResponse v1_stocks_currency_currency_get(currency)



returns a list of stocks listed with a certain currency

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    currency = 'currency_example' # str | 

    try:
        api_response = api_instance.v1_stocks_currency_currency_get(currency)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stocks_currency_currency_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 

### Return type

[**StockListResponse**](StockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stocks_exchange_code_exchange_code_get**
> StockListResponse v1_stocks_exchange_code_exchange_code_get(exchange_code)



given an exchange_code code return a list of stocks in the exchange_code

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_stocks_exchange_code_exchange_code_get(exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stocks_exchange_code_exchange_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_code** | **str**|  | 

### Return type

[**StockListResponse**](StockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stocks_exchange_id_exchange_id_get**
> StockListResponse v1_stocks_exchange_id_exchange_id_get(exchange_id)



given an exchange_code id return a list of stocks in the exchange_code

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    exchange_id = 'exchange_id_example' # str | 

    try:
        api_response = api_instance.v1_stocks_exchange_id_exchange_id_get(exchange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stocks_exchange_id_exchange_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**|  | 

### Return type

[**StockListResponse**](StockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stocks_get**
> StockListResponse v1_stocks_get()



returns a complete list of stocks present

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    
    try:
        api_response = api_instance.v1_stocks_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stocks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StockListResponse**](StockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stocks_post**
> StockListResponse v1_stocks_post(body=body)



create new stocks from a list of stocks

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StocksApi(api_client)
    body = openapi_client.StockListRequest() # StockListRequest |  (optional)

    try:
        api_response = api_instance.v1_stocks_post(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StocksApi->v1_stocks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StockListRequest**](StockListRequest.md)|  | [optional] 

### Return type

[**StockListResponse**](StockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

