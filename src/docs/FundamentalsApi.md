# Intelligent Stock Market API 
## Companies Fundamentals DATA API

All URIs are relative to *https://gateway.eod-stock-api.site/api*

| Method                                                                                                                                                                                          | HTTP request                                                                                | Description |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| [**v1_fundamental_company_stock_code_get**](FundamentalsApi.md#v1_fundamental_company_stock_code_get)                                                                                           | **GET** /v1/fundamental/company/{stock_code}                                                |             |
| [**v1_fundamental_general_get**](FundamentalsApi.md#v1_fundamental_general_get)                                                                                                                 | **GET** /v1/fundamental/general                                                             |             |
| [**v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get**](FundamentalsApi.md#v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get)                                       | **GET** /v1/fundamentals/annual-balance-sheet/{filing_date}/{stock_code}                    |             |
| [**v1_fundamentals_company_address_id_fundamental_id_get**](FundamentalsApi.md#v1_fundamentals_company_address_id_fundamental_id_get)                                                           | **GET** /v1/fundamentals/company-address/id/{fundamental_id}                                |             |
| [**v1_fundamentals_company_address_stock_stock_code_get**](FundamentalsApi.md#v1_fundamentals_company_address_stock_stock_code_get)                                                             | **GET** /v1/fundamentals/company-address/stock/{stock_code}                                 |             |
| [**v1_fundamentals_company_details_id_fundamental_id_get**](FundamentalsApi.md#v1_fundamentals_company_details_id_fundamental_id_get)                                                           | **GET** /v1/fundamentals/company-details/id/{fundamental_id}                                |             |
| [**v1_fundamentals_company_details_stock_stock_code_get**](FundamentalsApi.md#v1_fundamentals_company_details_stock_stock_code_get)                                                             | **GET** /v1/fundamentals/company-details/stock/{stock_code}                                 |             |
| [**v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get**](FundamentalsApi.md#v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get)               | **GET** /v1/fundamentals/company-insider-transactions/stock-code/{stock_code}/{year}        |             |
| [**v1_fundamentals_company_valuations_stock_code_stock_code_year_get**](FundamentalsApi.md#v1_fundamentals_company_valuations_stock_code_stock_code_year_get)                                   | **GET** /v1/fundamentals/company-valuations/stock-code/{stock_code}/{year}                  |             |
| [**v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get**](FundamentalsApi.md#v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get)         | **GET** /v1/fundamentals/exchange-analyst-rankings/exchange-code/{exchange_code}/{year}     |             |
| [**v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get**](FundamentalsApi.md#v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get)     | **GET** /v1/fundamentals/exchange-outstanding-shares/exchange-code/{exchange_code}/{year}   |             |
| [**v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get**](FundamentalsApi.md#v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get)                     | **GET** /v1/fundamentals/financial-statements/by-term/{_from}.{_to}/{stock_code}/{term}     |             |
| [**v1_fundamentals_financial_statements_company_statement_stock_code_year_get**](FundamentalsApi.md#v1_fundamentals_financial_statements_company_statement_stock_code_year_get)                 | **GET** /v1/fundamentals/financial-statements/company-statement/{stock_code}/{year}         |             |
| [**v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get**](FundamentalsApi.md#v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get)                   | **GET** /v1/fundamentals/financial-statements/exchange-year/{exchange_code}/{year}          |             |
| [**v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get**](FundamentalsApi.md#v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get) | **GET** /v1/fundamentals/financial-statements/filing-date-ticker/{filing_date}/{stock_code} |             |
| [**v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get**](FundamentalsApi.md#v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get)           | **GET** /v1/fundamentals/financial-statements/ticker-date-range/{_from}.{_to}/{stock_code}  |             |
| [**v1_fundamentals_financials_income_statements_statement_id_get**](FundamentalsApi.md#v1_fundamentals_financials_income_statements_statement_id_get)                                           | **GET** /v1/fundamentals/financials/income-statements/{statement_id}                        |             |
| [**v1_fundamentals_highlights_id_fundamental_id_get**](FundamentalsApi.md#v1_fundamentals_highlights_id_fundamental_id_get)                                                                     | **GET** /v1/fundamentals/highlights/id/{fundamental_id}                                     |             |
| [**v1_fundamentals_highlights_stock_stock_code_get**](FundamentalsApi.md#v1_fundamentals_highlights_stock_stock_code_get)                                                                       | **GET** /v1/fundamentals/highlights/stock/{stock_code}                                      |             |
| [**v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get**](FundamentalsApi.md#v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get)                                 | **GET** /v1/fundamentals/quarterly-balance-sheet/{filing_date}/{stock_code}                 |             |
| [**v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get**](FundamentalsApi.md#v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get)                   | **GET** /v1/fundamentals/tech-indicators-by-company/stock-code/{stock_code}/{year}          |             |
| [**v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get**](FundamentalsApi.md#v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get)     | **GET** /v1/fundamentals/tech-indicators-by-exchange/exchange-code/{exchange_code}/{year}   |             |

# **Fundamental Data By Company Stock Code /Ticker Symbol**
> PublicFundamentalsResponse v1_fundamental_company_stock_code_get(stock_code)



for each stock code return the fundamental data of the company

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'aapl' # str | 

    try:
        api_response = api_instance.v1_fundamental_company_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

### Return type

[**PublicFundamentalsResponse**](PublicFundamentalsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **General Fundamental Data For All Listed Companies**
> GeneralResponse v1_fundamental_general_get()


return general fundamental data for all companies

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    
    try:
        api_response = api_instance.v1_fundamental_general_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api ".format(e))

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get**
> AnnualBalanceSheetResponse v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get(stock_code, filing_date)



given the filing date & balance_sheet_id return annual balance sheet

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    filing_date = '2022-02-03' # str | 

    try:
        api_response = api_instance.v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get(stock_code, filing_date)
        pprint(api_response)
    except ApiException as e:
                print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name            | Type    | Description | Notes |
|-----------------|---------|-------------|-------|
| **stock_code**  | **str** |             |       |
| **filing_date** | **str** |             |       |

### Return type

[**AnnualBalanceSheetResponse**](AnnualBalanceSheetResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_company_address_id_fundamental_id_get**
> AddressResponse v1_fundamentals_company_address_id_fundamental_id_get(fundamental_id)



returns company address data

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)

# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    fundamental_id = 'fundamental_id_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_company_address_id_fundamental_id_get(fundamental_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name               | Type    | Description | Notes |
|--------------------|---------|-------------|-------|
| **fundamental_id** | **str** |             |       |

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description                      | Response headers |
|-------------|----------------------------------|------------------|
| **0**       | get response for company address | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_company_address_stock_stock_code_get**
> AddressResponse v1_fundamentals_company_address_stock_stock_code_get(stock_code)



returns company address data

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_company_address_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description                      | Response headers |
|-------------|----------------------------------|------------------|
| **0**       | get response for company address | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

## **Fundamental Company Details**

returns company details from company fundamental data

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    fundamental_id = 'fundamental_id_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_company_details_id_fundamental_id_get(fundamental_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name               | Type    | Description | Notes |
|--------------------|---------|-------------|-------|
| **fundamental_id** | **str** |             |       |

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

## **Fundamentals Company Details By Stock Code**

returns company details from company fundamental data

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_company_details_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

## **Fundamentals Insider Trading By Stock Code and Year**

Given companies stock_code, and year return a list of insider transactions

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    year = '2022' # str | 

    try:
        api_response = api_instance.v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get(stock_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Fundamentals Api : {}".format(e))

```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **year**       | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_company_valuations_stock_code_stock_code_year_get**
> OptionsResponse v1_fundamentals_company_valuations_stock_code_stock_code_year_get(stock_code, year)



Get Company Valuations Data for the year

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    year = '2022' # str | 

    try:
        api_response = api_instance.v1_fundamentals_company_valuations_stock_code_stock_code_year_get(stock_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_company_valuations_stock_code_stock_code_year_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **year**       | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get**
> OptionsResponse v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get(exchange_code, year)



Get Analyst rankings for all companies listed under a specific exchange

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    exchange_code = 'exchange_code_example' # str | 
    year = '2023' # str | 

    try:
        api_response = api_instance.v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get(exchange_code, year)
        pprint(api_response)
    except ApiException as e:
            print("Exception when calling Fundamentals Api {}".format(e))

```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **exchange_code** | **str** |             |       |
| **year**          | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|------------|-------------|------------------|
| **200**    |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get**
> OptionsResponse v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get(exchange_code, year)



Given an exchange_code and a year return all outstanding shares for all companies for that year

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    exchange_code = 'exchange_code_example' # str | 
    year = 'year_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get(exchange_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **exchange_code** | **str** |             |       |
| **year**          | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get**
> OptionsResponse v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get(stock_code, to, _from, term)



Return Annual or Quarterly Statements based on Term, Stock Code, and dates _from and _to

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    to = 'to_example' # str | 
    _from = '_from_example' # str | 
    term = 'term_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get(stock_code, to, _from, term)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **to**         | **str** |             |       |
| **_from**      | **str** |             |       |
| **term**       | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_financial_statements_company_statement_stock_code_year_get**
> OptionsResponse v1_fundamentals_financial_statements_company_statement_stock_code_year_get(stock_code, year)



given an a stock_code and a year return a complete financial statements for the year

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    year = 'year_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_financial_statements_company_statement_stock_code_year_get(stock_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_financial_statements_company_statement_stock_code_year_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **year**       | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get**
> OptionsResponse v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get(exchange_code, year)



Given an exchange_code and a year return a complete list of financial statements for all companies in exchange

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    exchange_code = 'exchange_code_example' # str | 
    year = 'year_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get(exchange_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **exchange_code** | **str** |             |       |
| **year**          | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get**
> OptionsResponse v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get(stock_code, filing_date)



Returns Income Statements by Filing Date and Company Stock Code

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    filing_date = 'filing_date_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get(stock_code, filing_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get: %s\n" % e)
```

### Parameters

| Name            | Type    | Description | Notes |
|-----------------|---------|-------------|-------|
| **stock_code**  | **str** |             |       |
| **filing_date** | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get**
> OptionsResponse v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get(stock_code, to, _from)



Given two dates and a stock date return all financial statements, _from & _to should be date-strings

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    to = 'to_example' # str | 
    _from = '_from_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get(stock_code, to, _from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **to**         | **str** |             |       |
| **_from**      | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_financials_income_statements_statement_id_get**
> OptionsResponse v1_fundamentals_financials_income_statements_statement_id_get(statement_id)



Will return Company Income Statement By Statement ID

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    statement_id = 'statement_id_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_financials_income_statements_statement_id_get(statement_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_financials_income_statements_statement_id_get: %s\n" % e)
```

### Parameters

| Name             | Type    | Description | Notes |
|------------------|---------|-------------|-------|
| **statement_id** | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_highlights_id_fundamental_id_get**
> HighlightsResponse v1_fundamentals_highlights_id_fundamental_id_get(fundamental_id)



get fundamental highlights data from either fundamental_id or stock_codes

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    fundamental_id = 'fundamental_id_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_highlights_id_fundamental_id_get(fundamental_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_highlights_id_fundamental_id_get: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
|--------------------|---------|-------------|-------|
| **fundamental_id** | **str** |             |       |

### Return type

[**HighlightsResponse**](HighlightsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_highlights_stock_stock_code_get**
> HighlightsResponse v1_fundamentals_highlights_stock_stock_code_get(stock_code)



get fundamental highlights data from either fundamental_id or stock_codes

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_highlights_stock_stock_code_get(stock_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_highlights_stock_stock_code_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |

### Return type

[**HighlightsResponse**](HighlightsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get**
> QuarterlyBalanceResponse v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get(stock_code, filing_date)



given filing_date and balance_sheet_id return Quarterly Balance Sheet

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    filing_date = 'filing_date_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get(stock_code, filing_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get: %s\n" % e)
```

### Parameters

| Name            | Type    | Description | Notes |
|-----------------|---------|-------------|-------|
| **stock_code**  | **str** |             |       |
| **filing_date** | **str** |             |       |

### Return type

[**QuarterlyBalanceResponse**](QuarterlyBalanceResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get**
> OptionsResponse v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get(stock_code, year)



Given a company stock_code and a year return technical indicators for that year

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
     host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    stock_code = 'stock_code_example' # str | 
    year = 'year_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get(stock_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
|----------------|---------|-------------|-------|
| **stock_code** | **str** |             |       |
| **year**       | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get**
> OptionsResponse v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get(exchange_code, year)



Given an exchange_code and a year return all technical indicators released for companies listed on the exchange for the year mentioned

### Example

```python
from __future__ import print_function

import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://gateway.eod-stock-api.site/api
# See configuration.py for a list of all supported configuration parameters.
configuration = IntelligentStockMarketAPI.Configuration(
    host = "http://https://gateway.eod-stock-api.site/api",
    api_key = "SECRET API KEY",
)


# Enter a context with an instance of the API client
with IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = IntelligentStockMarketAPI.FundamentalsApi(api_client)
    exchange_code = 'exchange_code_example' # str | 
    year = 'year_example' # str | 

    try:
        api_response = api_instance.v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get(exchange_code, year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FundamentalsApi->v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get: %s\n" % e)
```

### Parameters

| Name              | Type    | Description | Notes |
|-------------------|---------|-------------|-------|
| **exchange_code** | **str** |             |       |
| **year**          | **str** |             |       |

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

api_key

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0**       |             | -                |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

