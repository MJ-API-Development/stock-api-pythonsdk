# Intelligent Stock Market API

All URIs are relative to *https://gateway.eod-stock-api.site/api*

| Method                                                                                                             | HTTP request                                       | Description |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------|
| [**v1_news_article_uuid_get**](FinancialNewsApi.md#v1_news_article_uuid_get)                                       | **GET** /v1/news/article/{uuid}                    |             |
| [**v1_news_articles_bounded_upper_bound_get**](FinancialNewsApi.md#v1_news_articles_bounded_upper_bound_get)       | **GET** /v1/news/articles-bounded/{upper_bound}    |             |
| [**v1_news_articles_by_date_date_get**](FinancialNewsApi.md#v1_news_articles_by_date_date_get)                     | **GET** /v1/news/articles-by-date/{_date}          |             |
| [**v1_news_articles_by_publisher_publisher_get**](FinancialNewsApi.md#v1_news_articles_by_publisher_publisher_get) | **GET** /v1/news/articles-by-publisher/{publisher} |             |
| [**v1_news_articles_by_ticker_stock_code_get**](FinancialNewsApi.md#v1_news_articles_by_ticker_stock_code_get)     | **GET** /v1/news/articles-by-ticker/{stock_code}   |             |

# **Return News Articles By UUID**

Obtain Financial News Information related to listed companies

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
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.v1_news_article_uuid_get(uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception {}".format(e))
```

### Parameters

| Name     | Type    | Description | Notes |
|----------|---------|-------------|-------|
| **uuid** | **str** |             |       |

### Return type

[**News**](News.md)

### Authorization

api key - obtainable from our website - subscribe here https://eod-stock-api.site/login

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **Return News Bounded by an Upper Limit**


Get list of all News Upper Bound is an Integer indicating a total number of articles to return

### Example

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
    api_key= "API Key"
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    upper_bound = 25 # int |  

    try:
        api_response = api_instance.v1_news_articles_bounded_upper_bound_get(upper_bound)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Financial News Api : {}".format(e))
```

### Parameters

| Name            | Type    | Description | Notes |
|-----------------|---------|-------------|-------|
| **upper_bound** | **int** |             |       |

### Return type

[**NewsResponseList**](NewsResponseList.md)

### Authorization

api key - obtainable from our website - subscribe here https://eod-stock-api.site/login

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|------------|-------------|------------------|
| **200**    |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **Articles By Specific Dates**
> News v1_news_articles_by_date_date_get(date)



Get Articles Financial News By Date

### Example

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
    api_key = "API Key"
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    date = '2022-04-01' # str | 

    try:
        api_response = api_instance.v1_news_articles_by_date_date_get(date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Financial News Api {}".format(e))
```

### Parameters

| Name     | Type    | Description | Notes |
|----------|---------|-------------|-------|
| **date** | **str** |             |       |

### Return type

[**News**](News.md)

### Authorization

api key - obtainable from our website - subscribe here https://eod-stock-api.site/login

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **Get Articles By Publisher**

Get News Financial News by publisher

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
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    publisher = 'new york times' # str | 

    try:
        api_response = api_instance.v1_news_articles_by_publisher_publisher_get(publisher)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Financial News Api {}".format(e))

```

### Parameters

| Name          | Type    | Description           | Notes |
|---------------|---------|-----------------------|-------|
| **publisher** | **str** | **Name of Publisher** |       |

### Return type

[**NewsResponseList**](NewsResponseList.md)

### Authorization

api key - obtainable from our website - subscribe here https://eod-stock-api.site/login

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

## **Return News Articles By Stock Code / Ticker Symbol**

Get Financial News Articles By Ticker Symbol / Stock Code

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
    api_instance = IntelligentStockMarketAPI.FinancialNewsApi(api_client)
    stock_code = 'TSLA' # str | Tesla Stock Code 

    try:
        api_response = api_instance.v1_news_articles_by_ticker_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Financial News Api {}".format(e))

```

### Parameters

| Name           | Type    | Description   | Notes |
|----------------|---------|---------------|-------|
| **stock_code** | **str** | Ticker Symbol |       |

### Return type

[**NewsResponseList**](NewsResponseList.md)

### Authorization
api key - obtainable from our website - subscribe here https://eod-stock-api.site/login

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|------------|-------------|------------------|
| **200**    |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

