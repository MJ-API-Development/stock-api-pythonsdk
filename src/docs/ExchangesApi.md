# openapi_client.ExchangesApi

All URIs are relative to *http://https://gateway.eod-stock-api.site/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_exchange_code_exchange_code_get**](ExchangesApi.md#v1_exchange_code_exchange_code_get) | **GET** /v1/exchange/code/{exchange_code} | 
[**v1_exchange_exchange_with_tickers_code_exchange_code_get**](ExchangesApi.md#v1_exchange_exchange_with_tickers_code_exchange_code_get) | **GET** /v1/exchange/exchange-with-tickers/code/{exchange_code} | 
[**v1_exchange_id_exchange_id_get**](ExchangesApi.md#v1_exchange_id_exchange_id_get) | **GET** /v1/exchange/id/{exchange_id} | 
[**v1_exchange_listed_companies_exchange_code_get**](ExchangesApi.md#v1_exchange_listed_companies_exchange_code_get) | **GET** /v1/exchange/listed-companies/{exchange_code} | 
[**v1_exchange_listed_stocks_exchange_code_get**](ExchangesApi.md#v1_exchange_listed_stocks_exchange_code_get) | **GET** /v1/exchange/listed-stocks/{exchange_code} | 
[**v1_exchange_post**](ExchangesApi.md#v1_exchange_post) | **POST** /v1/exchange | 
[**v1_exchanges_get**](ExchangesApi.md#v1_exchanges_get) | **GET** /v1/exchanges | 


# **v1_exchange_code_exchange_code_get**
> ExchangeResponse v1_exchange_code_exchange_code_get(exchange_code)



given exchange_id or exchange_code code will return exchange_code data

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
    api_instance = openapi_client.ExchangesApi(api_client)
    exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_exchange_code_exchange_code_get(exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_code_exchange_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_code** | **str**|  | 

### Return type

[**ExchangeResponse**](ExchangeResponse.md)

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

# **v1_exchange_exchange_with_tickers_code_exchange_code_get**
> ExchangeWithListedTickers v1_exchange_exchange_with_tickers_code_exchange_code_get(exchange_code)



Exchange Data with a total list of stock_codes and stock_id's 

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
    api_instance = openapi_client.ExchangesApi(api_client)
    exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_exchange_exchange_with_tickers_code_exchange_code_get(exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_exchange_with_tickers_code_exchange_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_code** | **str**|  | 

### Return type

[**ExchangeWithListedTickers**](ExchangeWithListedTickers.md)

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

# **v1_exchange_id_exchange_id_get**
> ExchangeResponse v1_exchange_id_exchange_id_get(exchange_id)



given exchange_id or exchange_code code will return exchange_code data

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
    api_instance = openapi_client.ExchangesApi(api_client)
    exchange_id = 'exchange_id_example' # str | 

    try:
        api_response = api_instance.v1_exchange_id_exchange_id_get(exchange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_id_exchange_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**|  | 

### Return type

[**ExchangeResponse**](ExchangeResponse.md)

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

# **v1_exchange_listed_companies_exchange_code_get**
> ExchangeListedCompaniesResponse v1_exchange_listed_companies_exchange_code_get(exchange_code)



returns a list of listed companies in exchange_code

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
    api_instance = openapi_client.ExchangesApi(api_client)
    exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_exchange_listed_companies_exchange_code_get(exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_listed_companies_exchange_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_code** | **str**|  | 

### Return type

[**ExchangeListedCompaniesResponse**](ExchangeListedCompaniesResponse.md)

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

# **v1_exchange_listed_stocks_exchange_code_get**
> ExchangeListedStock v1_exchange_listed_stocks_exchange_code_get(exchange_code)



returns a list of listed stocks in exchange_code

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
    api_instance = openapi_client.ExchangesApi(api_client)
    exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_exchange_listed_stocks_exchange_code_get(exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_listed_stocks_exchange_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_code** | **str**|  | 

### Return type

[**ExchangeListedStock**](ExchangeListedStock.md)

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

# **v1_exchange_post**
> ExchangeResponse v1_exchange_post(body=body)



given exchange_code data create new exchange_code

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
    api_instance = openapi_client.ExchangesApi(api_client)
    body = openapi_client.ExchangeRequest() # ExchangeRequest |  (optional)

    try:
        api_response = api_instance.v1_exchange_post(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchange_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExchangeRequest**](ExchangeRequest.md)|  | [optional] 

### Return type

[**ExchangeResponse**](ExchangeResponse.md)

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

# **v1_exchanges_get**
> ExchangeListResponse v1_exchanges_get()



returns a list of exchanges

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
    api_instance = openapi_client.ExchangesApi(api_client)
    
    try:
        api_response = api_instance.v1_exchanges_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangesApi->v1_exchanges_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangeListResponse**](ExchangeListResponse.md)

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
