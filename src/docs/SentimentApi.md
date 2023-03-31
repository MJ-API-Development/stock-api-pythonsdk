# src.IntelligentStockMarketAPI.SentimentApi

All URIs are relative to *https://gateway.eod-stock-api.site/api*

| Method                                                                                                                 | HTTP request                                           | Description |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|-------------|
| [**v1_sentiment_trend_setters_stock_stock_code_get**](SentimentApi.md#v1_sentiment_trend_setters_stock_stock_code_get) | **GET** /v1/sentiment/trend-setters/stock/{stock_code} |             |
| [**v1_sentiment_trending_stock_stock_code_get**](SentimentApi.md#v1_sentiment_trending_stock_stock_code_get)           | **GET** /v1/sentiment/trending/stock/{stock_code}      |             |
| [**v1_sentiment_tweet_stock_stock_code_get**](SentimentApi.md#v1_sentiment_tweet_stock_stock_code_get)                 | **GET** /v1/sentiment/tweet/stock/{stock_code}         |             |

# **v1_sentiment_trend_setters_stock_stock_code_get**
> StockTrendSetters v1_sentiment_trend_setters_stock_stock_code_get(stock_code)



Given the stock_code return a list of trend setters for this stock and their sentiments

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
    api_instance = src.IntelligentStockMarketAPI.SentimentApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_sentiment_trend_setters_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentimentApi->v1_sentiment_trend_setters_stock_stock_code_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

### Return type

[**StockTrendSetters**](StockTrendSetters.md)

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

# **v1_sentiment_trending_stock_stock_code_get**
> OptionsResponse v1_sentiment_trending_stock_stock_code_get(stock_code)



Will return a sentiment for most trending Tweets by stock

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
    api_instance = src.IntelligentStockMarketAPI.SentimentApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_sentiment_trending_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentimentApi->v1_sentiment_trending_stock_stock_code_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

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
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_sentiment_tweet_stock_stock_code_get**
> OptionsResponse v1_sentiment_tweet_stock_stock_code_get(stock_code)



Will return a list Social Media Sentiments for a certain stock

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
    api_instance = src.IntelligentStockMarketAPI.SentimentApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_sentiment_tweet_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentimentApi->v1_sentiment_tweet_stock_stock_code_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

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
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

