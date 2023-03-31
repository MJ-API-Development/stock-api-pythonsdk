# src.IntelligentStockMarketAPI.OptionsApi

All URIs are relative to *http://https://gateway.eod-stock-api.site/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_stocks_contract_call_put_id_get**](OptionsApi.md#v1_stocks_contract_call_put_id_get) | **GET** /v1/stocks/contract/{call_put_id} | 
[**v1_stocks_options_stock_stock_code_get**](OptionsApi.md#v1_stocks_options_stock_stock_code_get) | **GET** /v1/stocks/options/stock/{stock_code} | 


# **v1_stocks_contract_call_put_id_get**
> ContractResponse v1_stocks_contract_call_put_id_get(call_put_id)



given call_put_id return Contract

### Example

```python
from __future__ import print_function
import time
import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = src.IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = src.IntelligentStockMarketAPI.OptionsApi(api_client)
    call_put_id = 'call_put_id_example' # str | 

    try:
        api_response = api_instance.v1_stocks_contract_call_put_id_get(call_put_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OptionsApi->v1_stocks_contract_call_put_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_put_id** | **str**|  | 

### Return type

[**ContractResponse**](ContractResponse.md)

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

# **v1_stocks_options_stock_stock_code_get**
> OptionsResponse v1_stocks_options_stock_stock_code_get(stock_code)



get Stock options data for the provided stock code

### Example

```python
from __future__ import print_function
import time
import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = src.IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api"
)


# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = src.IntelligentStockMarketAPI.OptionsApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_stocks_options_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OptionsApi->v1_stocks_options_stock_stock_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_code** | **str**|  | 

### Return type

[**OptionsResponse**](OptionsResponse.md)

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

