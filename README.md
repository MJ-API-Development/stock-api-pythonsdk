# Intelligent EOD Stock Market API Python SDK

<h2>Intelligent EOD Stocks API</h2>
    <p>
    End of day stock world wide STOCK API, this api is intended for use by web application developers, 
    and service providers looking for up-to-date always available.
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

```python
from __future__ import print_function

import time
import IntelligentStockMarketAPI
from IntelligentStockMarketAPI.rest import ApiException
from pprint import pprint

# To get your API KEY visit [Intteligent EOD Stock Market API](https://eod-stock-market-api.site/login) 
# and create your free acoount 
configuration = IntelligentStockMarketAPI.Configuration(
    host = "https://gateway.eod-stock-api.site/api",
    apikey = "SECRET API KEY"
)
# Enter a context with an instance of the API client
with src.IntelligentStockMarketAPI.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance =IntelligentStockMarketAPI.EodApi(api_client)
    date = '2022-02-02' # str | 
    exchange_code = 'TO' # str | "Country"="Canada", "name": "Toronto Exchange", "operating_mic": "XTSE" 

    try:
        api_response = api_instance.v1_eod_date_exchange_code_get(date, exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_date_exchange_code_get: %s\n" % e)    
```

## Documentation for API Endpoints

All URIs are relative to *https://gateway.eod-stock-api.site/api*

### End of Day API Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *EodApi*           | [**v1_eod_date_exchange_code_get**](src/docs/EodApi.md#v1_eod_date_exchange_code_get)                                                                                                                    | **GET** /v1/eod/{_date}/{exchange_code}                                                     |             |
| *EodApi*           | [**v1_eod_date_exchange_code_stock_code_get**](src/docs/EodApi.md#v1_eod_date_exchange_code_stock_code_get)                                                                                              | **GET** /v1/eod/{_date}/{exchange_code}.{stock_code}                                        |             |
| *EodApi*           | [**v1_eod_from_to_exchange_code_get**](src/docs/EodApi.md#v1_eod_from_to_exchange_code_get)                                                                                                              | **GET** /v1/eod/{_from}.{_to}/{exchange_code}                                               |             |
| *EodApi*           | [**v1_eod_from_to_stock_code_get**](src/docs/EodApi.md#v1_eod_from_to_stock_code_get)                                                                                                                    | **GET** /v1/eod/{_from}.{_to}/{stock_code}                                                  |             |

### Exchange Data API Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *ExchangesApi*     | [**v1_exchange_code_exchange_code_get**](src/docs/ExchangesApi.md#v1_exchange_code_exchange_code_get)                                                                                                    | **GET** /v1/exchange/code/{exchange_code}                                                   |             |
| *ExchangesApi*     | [**v1_exchange_exchange_with_tickers_code_exchange_code_get**](src/docs/ExchangesApi.md#v1_exchange_exchange_with_tickers_code_exchange_code_get)                                                        | **GET** /v1/exchange/exchange-with-tickers/code/{exchange_code}                             |             |
| *ExchangesApi*     | [**v1_exchange_id_exchange_id_get**](src/docs/ExchangesApi.md#v1_exchange_id_exchange_id_get)                                                                                                            | **GET** /v1/exchange/id/{exchange_id}                                                       |             |
| *ExchangesApi*     | [**v1_exchange_listed_companies_exchange_code_get**](src/docs/ExchangesApi.md#v1_exchange_listed_companies_exchange_code_get)                                                                            | **GET** /v1/exchange/listed-companies/{exchange_code}                                       |             |
| *ExchangesApi*     | [**v1_exchange_listed_stocks_exchange_code_get**](src/docs/ExchangesApi.md#v1_exchange_listed_stocks_exchange_code_get)                                                                                  | **GET** /v1/exchange/listed-stocks/{exchange_code}                                          |             |
| *ExchangesApi*     | [**v1_exchange_post**](src/docs/ExchangesApi.md#v1_exchange_post)                                                                                                                                        | **POST** /v1/exchange                                                                       |             |
| *ExchangesApi*     | [**v1_exchanges_get**](src/docs/ExchangesApi.md#v1_exchanges_get)                                                                                                                                        | **GET** /v1/exchanges                                                                       |             |

### Financial News & Social Media Trends APi Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *FinancialNewsApi* | [**v1_news_article_uuid_get**](src/docs/FinancialNewsApi.md#v1_news_article_uuid_get)                                                                                                                    | **GET** /v1/news/article/{uuid}                                                             |             |
| *FinancialNewsApi* | [**v1_news_articles_bounded_upper_bound_get**](src/docs/FinancialNewsApi.md#v1_news_articles_bounded_upper_bound_get)                                                                                    | **GET** /v1/news/articles-bounded/{upper_bound}                                             |             |
| *FinancialNewsApi* | [**v1_news_articles_by_date_date_get**](src/docs/FinancialNewsApi.md#v1_news_articles_by_date_date_get)                                                                                                  | **GET** /v1/news/articles-by-date/{_date}                                                   |             |
| *FinancialNewsApi* | [**v1_news_articles_by_publisher_publisher_get**](src/docs/FinancialNewsApi.md#v1_news_articles_by_publisher_publisher_get)                                                                              | **GET** /v1/news/articles-by-publisher/{publisher}                                          |             |
| *FinancialNewsApi* | [**v1_news_articles_by_ticker_stock_code_get**](src/docs/FinancialNewsApi.md#v1_news_articles_by_ticker_stock_code_get)                                                                                  | **GET** /v1/news/articles-by-ticker/{stock_code}                                            |             |

### Fundamental Data API Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *FundamentalsApi*  | [**v1_fundamental_company_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamental_company_stock_code_get)                                                                                           | **GET** /v1/fundamental/company/{stock_code}                                                |             |
| *FundamentalsApi*  | [**v1_fundamental_general_get**](src/docs/FundamentalsApi.md#v1_fundamental_general_get)                                                                                                                 | **GET** /v1/fundamental/general                                                             |             |
| *FundamentalsApi*  | [**v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get)                                       | **GET** /v1/fundamentals/annual-balance-sheet/{filing_date}/{stock_code}                    |             |
| *FundamentalsApi*  | [**v1_fundamentals_company_address_id_fundamental_id_get**](src/docs/FundamentalsApi.md#v1_fundamentals_company_address_id_fundamental_id_get)                                                           | **GET** /v1/fundamentals/company-address/id/{fundamental_id}                                |             |
| *FundamentalsApi*  | [**v1_fundamentals_company_address_stock_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_company_address_stock_stock_code_get)                                                             | **GET** /v1/fundamentals/company-address/stock/{stock_code}                                 |             |
| *FundamentalsApi*  | [**v1_fundamentals_company_details_id_fundamental_id_get**](src/docs/FundamentalsApi.md#v1_fundamentals_company_details_id_fundamental_id_get)                                                           | **GET** /v1/fundamentals/company-details/id/{fundamental_id}                                |             |
| *FundamentalsApi*  | [**v1_fundamentals_company_details_stock_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_company_details_stock_stock_code_get)                                                             | **GET** /v1/fundamentals/company-details/stock/{stock_code}                                 |             |
| *FundamentalsApi*  | [**v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get)               | **GET** /v1/fundamentals/company-insider-transactions/stock-code/{stock_code}/{year}        |             |
| *FundamentalsApi*  | [**v1_fundamentals_company_valuations_stock_code_stock_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_company_valuations_stock_code_stock_code_year_get)                                   | **GET** /v1/fundamentals/company-valuations/stock-code/{stock_code}/{year}                  |             |
| *FundamentalsApi*  | [**v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get)         | **GET** /v1/fundamentals/exchange-analyst-rankings/exchange-code/{exchange_code}/{year}     |             |
| *FundamentalsApi*  | [**v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get)     | **GET** /v1/fundamentals/exchange-outstanding-shares/exchange-code/{exchange_code}/{year}   |             |
| *FundamentalsApi*  | [**v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get**](src/docs/FundamentalsApi.md#v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get)                     | **GET** /v1/fundamentals/financial-statements/by-term/{_from}.{_to}/{stock_code}/{term}     |             |
| *FundamentalsApi*  | [**v1_fundamentals_financial_statements_company_statement_stock_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_financial_statements_company_statement_stock_code_year_get)                 | **GET** /v1/fundamentals/financial-statements/company-statement/{stock_code}/{year}         |             |
| *FundamentalsApi*  | [**v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get)                   | **GET** /v1/fundamentals/financial-statements/exchange-year/{exchange_code}/{year}          |             |
| *FundamentalsApi*  | [**v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get) | **GET** /v1/fundamentals/financial-statements/filing-date-ticker/{filing_date}/{stock_code} |             |
| *FundamentalsApi*  | [**v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get)           | **GET** /v1/fundamentals/financial-statements/ticker-date-range/{_from}.{_to}/{stock_code}  |             |
| *FundamentalsApi*  | [**v1_fundamentals_financials_income_statements_statement_id_get**](src/docs/FundamentalsApi.md#v1_fundamentals_financials_income_statements_statement_id_get)                                           | **GET** /v1/fundamentals/financials/income-statements/{statement_id}                        |             |
| *FundamentalsApi*  | [**v1_fundamentals_highlights_id_fundamental_id_get**](src/docs/FundamentalsApi.md#v1_fundamentals_highlights_id_fundamental_id_get)                                                                     | **GET** /v1/fundamentals/highlights/id/{fundamental_id}                                     |             |
| *FundamentalsApi*  | [**v1_fundamentals_highlights_stock_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_highlights_stock_stock_code_get)                                                                       | **GET** /v1/fundamentals/highlights/stock/{stock_code}                                      |             |
| *FundamentalsApi*  | [**v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get**](src/docs/FundamentalsApi.md#v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get)                                 | **GET** /v1/fundamentals/quarterly-balance-sheet/{filing_date}/{stock_code}                 |             |
| *FundamentalsApi*  | [**v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get)                   | **GET** /v1/fundamentals/tech-indicators-by-company/stock-code/{stock_code}/{year}          |             |
| *FundamentalsApi*  | [**v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get**](src/docs/FundamentalsApi.md#v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get)     | **GET** /v1/fundamentals/tech-indicators-by-exchange/exchange-code/{exchange_code}/{year}   |             |


### Calls & Options API Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *OptionsApi*       | [**v1_stocks_contract_call_put_id_get**](src/docs/OptionsApi.md#v1_stocks_contract_call_put_id_get)                                                                                                      | **GET** /v1/stocks/contract/{call_put_id}                                                   |             |
| *OptionsApi*       | [**v1_stocks_options_stock_stock_code_get**](src/docs/OptionsApi.md#v1_stocks_options_stock_stock_code_get)                                                                                              | **GET** /v1/stocks/options/stock/{stock_code}                                               |             |

### Sentiment Analysis API Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *SentimentApi*     | [**v1_sentiment_trend_setters_stock_stock_code_get**](src/docs/SentimentApi.md#v1_sentiment_trend_setters_stock_stock_code_get)                                                                          | **GET** /v1/sentiment/trend-setters/stock/{stock_code}                                      |             |
| *SentimentApi*     | [**v1_sentiment_trending_stock_stock_code_get**](src/docs/SentimentApi.md#v1_sentiment_trending_stock_stock_code_get)                                                                                    | **GET** /v1/sentiment/trending/stock/{stock_code}                                           |             |
| *SentimentApi*     | [**v1_sentiment_tweet_stock_stock_code_get**](src/docs/SentimentApi.md#v1_sentiment_tweet_stock_stock_code_get)                                                                                          | **GET** /v1/sentiment/tweet/stock/{stock_code}                                              |             |

### Stock Data / Tickers API Documentations
| Class              | Method                                                                                                                                                                                                   | HTTP request                                                                                | Description |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| *StocksApi*        | [**v1_stock_code_stock_code_get**](src/docs/StocksApi.md#v1_stock_code_stock_code_get)                                                                                                                   | **GET** /v1/stock/code/{stock_code}                                                         |             |
| *StocksApi*        | [**v1_stocks_country_country_get**](src/docs/StocksApi.md#v1_stocks_country_country_get)                                                                                                                 | **GET** /v1/stocks/country/{country}                                                        |             |
| *StocksApi*        | [**v1_stocks_currency_currency_get**](src/docs/StocksApi.md#v1_stocks_currency_currency_get)                                                                                                             | **GET** /v1/stocks/currency/{currency}                                                      |             |
| *StocksApi*        | [**v1_stocks_exchange_code_exchange_code_get**](src/docs/StocksApi.md#v1_stocks_exchange_code_exchange_code_get)                                                                                         | **GET** /v1/stocks/exchange/code/{exchange_code}                                            |             |
| *StocksApi*        | [**v1_stocks_exchange_id_exchange_id_get**](src/docs/StocksApi.md#v1_stocks_exchange_id_exchange_id_get)                                                                                                 | **GET** /v1/stocks/exchange/id/{exchange_id}                                                |             |
| *StocksApi*        | [**v1_stocks_get**](src/docs/StocksApi.md#v1_stocks_get)                                                                                                                                                 | **GET** /v1/stocks                                                                          |             |
| *StocksApi*        | [**v1_stocks_post**](src/docs/StocksApi.md#v1_stocks_post)                                                                                                                                               | **POST** /v1/stocks                                                                         |             |

## Documentation For Models

 - [AddressResponse](src/docs/AddressResponse.md)
 - [Analyst](src/docs/Analyst.md)
 - [AnnualBalanceSheet](src/docs/AnnualBalanceSheet.md)
 - [AnnualBalanceSheetResponse](src/docs/AnnualBalanceSheetResponse.md)
 - [BalanceSheet](src/docs/BalanceSheet.md)
 - [BalanceSheets](src/docs/BalanceSheets.md)
 - [ContractResponse](src/docs/ContractResponse.md)
 - [Contracts](src/docs/Contracts.md)
 - [EODStock](src/docs/EODStock.md)
 - [EODStockListResponse](src/docs/EODStockListResponse.md)
 - [EODStockResponse](src/docs/EODStockResponse.md)
 - [Exchange](src/docs/Exchange.md)
 - [ExchangeListResponse](src/docs/ExchangeListResponse.md)
 - [ExchangeListedCompaniesResponse](src/docs/ExchangeListedCompaniesResponse.md)
 - [ExchangeListedStock](src/docs/ExchangeListedStock.md)
 - [ExchangeRequest](src/docs/ExchangeRequest.md)
 - [ExchangeResponse](src/docs/ExchangeResponse.md)
 - [ExchangeWithListedTickers](src/docs/ExchangeWithListedTickers.md)
 - [ExchangeWithTickers](src/docs/ExchangeWithTickers.md)
 - [General](src/docs/General.md)
 - [GeneralAddress](src/docs/GeneralAddress.md)
 - [GeneralContact](src/docs/GeneralContact.md)
 - [GeneralListings](src/docs/GeneralListings.md)
 - [GeneralOfficers](src/docs/GeneralOfficers.md)
 - [GeneralResponse](src/docs/GeneralResponse.md)
 - [Highlights](src/docs/Highlights.md)
 - [HighlightsResponse](src/docs/HighlightsResponse.md)
 - [News](src/docs/News.md)
 - [NewsResponseList](src/docs/NewsResponseList.md)
 - [NumberDividendsByYear](src/docs/NumberDividendsByYear.md)
 - [Options](src/docs/Options.md)
 - [OptionsResponse](src/docs/OptionsResponse.md)
 - [Payload](src/docs/Payload.md)
 - [PublicFundamental](src/docs/PublicFundamental.md)
 - [PublicFundamentalsResponse](src/docs/PublicFundamentalsResponse.md)
 - [QuarterlyBalanceResponse](src/docs/QuarterlyBalanceResponse.md)
 - [QuarterlyBalanceSheet](src/docs/QuarterlyBalanceSheet.md)
 - [RelatedTickers](src/docs/RelatedTickers.md)
 - [Resolution](src/docs/Resolution.md)
 - [Sentiment](src/docs/Sentiment.md)
 - [ShareStats](src/docs/ShareStats.md)
 - [SplitDividends](src/docs/SplitDividends.md)
 - [Stock](src/docs/Stock.md)
 - [Stock1](src/docs/Stock1.md)
 - [StockListRequest](src/docs/StockListRequest.md)
 - [StockListResponse](src/docs/StockListResponse.md)
 - [StockResponse](src/docs/StockResponse.md)
 - [StockTrendSetters](src/docs/StockTrendSetters.md)
 - [Technicals](src/docs/Technicals.md)
 - [Thumbnail](src/docs/Thumbnail.md)
 - [TickerExchangeCode](src/docs/TickerExchangeCode.md)
 - [Valuations](src/docs/Valuations.md)


## Documentation For Authorization

## basicAuth

- **Type**: 
  - apikey

To authenticate your API requests, you will need to include your API key in the request parameters. 
The API key is a unique identifier that associates your API usage with your account.

To include your API key in a request, simply include it as a parameter named "apikey" in the request URL. 
For example:

```python
    https://gateway.eod-stock-api.site/api/v1/exchanges?apikey=YOUR_API_KEY
```

Make sure to replace "YOUR_API_KEY" with your actual API key value.

Note that when using our SDK you need to initialize your SDK with your API key refer to getting started
section above.


## Author
- **MJ API Development**

    **support@eod-stock-api.site**


