# openapi-client

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



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EodApi(api_client)
    date = 'date_example' # str | 
exchange_code = 'exchange_code_example' # str | 

    try:
        api_response = api_instance.v1_eod_date_exchange_code_get(date, exchange_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EodApi->v1_eod_date_exchange_code_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://https://gateway.eod-stock-api.site/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EodApi* | [**v1_eod_date_exchange_code_get**](docs/EodApi.md#v1_eod_date_exchange_code_get) | **GET** /v1/eod/{_date}/{exchange_code} | 
*EodApi* | [**v1_eod_date_exchange_code_stock_code_get**](docs/EodApi.md#v1_eod_date_exchange_code_stock_code_get) | **GET** /v1/eod/{_date}/{exchange_code}.{stock_code} | 
*EodApi* | [**v1_eod_from_to_exchange_code_get**](docs/EodApi.md#v1_eod_from_to_exchange_code_get) | **GET** /v1/eod/{_from}.{_to}/{exchange_code} | 
*EodApi* | [**v1_eod_from_to_stock_code_get**](docs/EodApi.md#v1_eod_from_to_stock_code_get) | **GET** /v1/eod/{_from}.{_to}/{stock_code} | 
*ExchangesApi* | [**v1_exchange_code_exchange_code_get**](docs/ExchangesApi.md#v1_exchange_code_exchange_code_get) | **GET** /v1/exchange/code/{exchange_code} | 
*ExchangesApi* | [**v1_exchange_exchange_with_tickers_code_exchange_code_get**](docs/ExchangesApi.md#v1_exchange_exchange_with_tickers_code_exchange_code_get) | **GET** /v1/exchange/exchange-with-tickers/code/{exchange_code} | 
*ExchangesApi* | [**v1_exchange_id_exchange_id_get**](docs/ExchangesApi.md#v1_exchange_id_exchange_id_get) | **GET** /v1/exchange/id/{exchange_id} | 
*ExchangesApi* | [**v1_exchange_listed_companies_exchange_code_get**](docs/ExchangesApi.md#v1_exchange_listed_companies_exchange_code_get) | **GET** /v1/exchange/listed-companies/{exchange_code} | 
*ExchangesApi* | [**v1_exchange_listed_stocks_exchange_code_get**](docs/ExchangesApi.md#v1_exchange_listed_stocks_exchange_code_get) | **GET** /v1/exchange/listed-stocks/{exchange_code} | 
*ExchangesApi* | [**v1_exchange_post**](docs/ExchangesApi.md#v1_exchange_post) | **POST** /v1/exchange | 
*ExchangesApi* | [**v1_exchanges_get**](docs/ExchangesApi.md#v1_exchanges_get) | **GET** /v1/exchanges | 
*FinancialNewsApi* | [**v1_news_article_uuid_get**](docs/FinancialNewsApi.md#v1_news_article_uuid_get) | **GET** /v1/news/article/{uuid} | 
*FinancialNewsApi* | [**v1_news_articles_bounded_upper_bound_get**](docs/FinancialNewsApi.md#v1_news_articles_bounded_upper_bound_get) | **GET** /v1/news/articles-bounded/{upper_bound} | 
*FinancialNewsApi* | [**v1_news_articles_by_date_date_get**](docs/FinancialNewsApi.md#v1_news_articles_by_date_date_get) | **GET** /v1/news/articles-by-date/{_date} | 
*FinancialNewsApi* | [**v1_news_articles_by_publisher_publisher_get**](docs/FinancialNewsApi.md#v1_news_articles_by_publisher_publisher_get) | **GET** /v1/news/articles-by-publisher/{publisher} | 
*FinancialNewsApi* | [**v1_news_articles_by_ticker_stock_code_get**](docs/FinancialNewsApi.md#v1_news_articles_by_ticker_stock_code_get) | **GET** /v1/news/articles-by-ticker/{stock_code} | 
*FundamentalsApi* | [**v1_fundamental_company_stock_code_get**](docs/FundamentalsApi.md#v1_fundamental_company_stock_code_get) | **GET** /v1/fundamental/company/{stock_code} | 
*FundamentalsApi* | [**v1_fundamental_general_get**](docs/FundamentalsApi.md#v1_fundamental_general_get) | **GET** /v1/fundamental/general | 
*FundamentalsApi* | [**v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_annual_balance_sheet_filing_date_stock_code_get) | **GET** /v1/fundamentals/annual-balance-sheet/{filing_date}/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_company_address_id_fundamental_id_get**](docs/FundamentalsApi.md#v1_fundamentals_company_address_id_fundamental_id_get) | **GET** /v1/fundamentals/company-address/id/{fundamental_id} | 
*FundamentalsApi* | [**v1_fundamentals_company_address_stock_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_company_address_stock_stock_code_get) | **GET** /v1/fundamentals/company-address/stock/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_company_details_id_fundamental_id_get**](docs/FundamentalsApi.md#v1_fundamentals_company_details_id_fundamental_id_get) | **GET** /v1/fundamentals/company-details/id/{fundamental_id} | 
*FundamentalsApi* | [**v1_fundamentals_company_details_stock_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_company_details_stock_stock_code_get) | **GET** /v1/fundamentals/company-details/stock/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_company_insider_transactions_stock_code_stock_code_year_get) | **GET** /v1/fundamentals/company-insider-transactions/stock-code/{stock_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_company_valuations_stock_code_stock_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_company_valuations_stock_code_stock_code_year_get) | **GET** /v1/fundamentals/company-valuations/stock-code/{stock_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_exchange_analyst_rankings_exchange_code_exchange_code_year_get) | **GET** /v1/fundamentals/exchange-analyst-rankings/exchange-code/{exchange_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_exchange_outstanding_shares_exchange_code_exchange_code_year_get) | **GET** /v1/fundamentals/exchange-outstanding-shares/exchange-code/{exchange_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get**](docs/FundamentalsApi.md#v1_fundamentals_financial_statements_by_term_from_to_stock_code_term_get) | **GET** /v1/fundamentals/financial-statements/by-term/{_from}.{_to}/{stock_code}/{term} | 
*FundamentalsApi* | [**v1_fundamentals_financial_statements_company_statement_stock_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_financial_statements_company_statement_stock_code_year_get) | **GET** /v1/fundamentals/financial-statements/company-statement/{stock_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_financial_statements_exchange_year_exchange_code_year_get) | **GET** /v1/fundamentals/financial-statements/exchange-year/{exchange_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_financial_statements_filing_date_ticker_filing_date_stock_code_get) | **GET** /v1/fundamentals/financial-statements/filing-date-ticker/{filing_date}/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_financial_statements_ticker_date_range_from_to_stock_code_get) | **GET** /v1/fundamentals/financial-statements/ticker-date-range/{_from}.{_to}/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_financials_income_statements_statement_id_get**](docs/FundamentalsApi.md#v1_fundamentals_financials_income_statements_statement_id_get) | **GET** /v1/fundamentals/financials/income-statements/{statement_id} | 
*FundamentalsApi* | [**v1_fundamentals_highlights_id_fundamental_id_get**](docs/FundamentalsApi.md#v1_fundamentals_highlights_id_fundamental_id_get) | **GET** /v1/fundamentals/highlights/id/{fundamental_id} | 
*FundamentalsApi* | [**v1_fundamentals_highlights_stock_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_highlights_stock_stock_code_get) | **GET** /v1/fundamentals/highlights/stock/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get**](docs/FundamentalsApi.md#v1_fundamentals_quarterly_balance_sheet_filing_date_stock_code_get) | **GET** /v1/fundamentals/quarterly-balance-sheet/{filing_date}/{stock_code} | 
*FundamentalsApi* | [**v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_tech_indicators_by_company_stock_code_stock_code_year_get) | **GET** /v1/fundamentals/tech-indicators-by-company/stock-code/{stock_code}/{year} | 
*FundamentalsApi* | [**v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get**](docs/FundamentalsApi.md#v1_fundamentals_tech_indicators_by_exchange_exchange_code_exchange_code_year_get) | **GET** /v1/fundamentals/tech-indicators-by-exchange/exchange-code/{exchange_code}/{year} | 
*OptionsApi* | [**v1_stocks_contract_call_put_id_get**](docs/OptionsApi.md#v1_stocks_contract_call_put_id_get) | **GET** /v1/stocks/contract/{call_put_id} | 
*OptionsApi* | [**v1_stocks_options_stock_stock_code_get**](docs/OptionsApi.md#v1_stocks_options_stock_stock_code_get) | **GET** /v1/stocks/options/stock/{stock_code} | 
*SentimentApi* | [**v1_sentiment_trend_setters_stock_stock_code_get**](docs/SentimentApi.md#v1_sentiment_trend_setters_stock_stock_code_get) | **GET** /v1/sentiment/trend-setters/stock/{stock_code} | 
*SentimentApi* | [**v1_sentiment_trending_stock_stock_code_get**](docs/SentimentApi.md#v1_sentiment_trending_stock_stock_code_get) | **GET** /v1/sentiment/trending/stock/{stock_code} | 
*SentimentApi* | [**v1_sentiment_tweet_stock_stock_code_get**](docs/SentimentApi.md#v1_sentiment_tweet_stock_stock_code_get) | **GET** /v1/sentiment/tweet/stock/{stock_code} | 
*StocksApi* | [**v1_stock_code_stock_code_get**](docs/StocksApi.md#v1_stock_code_stock_code_get) | **GET** /v1/stock/code/{stock_code} | 
*StocksApi* | [**v1_stocks_country_country_get**](docs/StocksApi.md#v1_stocks_country_country_get) | **GET** /v1/stocks/country/{country} | 
*StocksApi* | [**v1_stocks_currency_currency_get**](docs/StocksApi.md#v1_stocks_currency_currency_get) | **GET** /v1/stocks/currency/{currency} | 
*StocksApi* | [**v1_stocks_exchange_code_exchange_code_get**](docs/StocksApi.md#v1_stocks_exchange_code_exchange_code_get) | **GET** /v1/stocks/exchange/code/{exchange_code} | 
*StocksApi* | [**v1_stocks_exchange_id_exchange_id_get**](docs/StocksApi.md#v1_stocks_exchange_id_exchange_id_get) | **GET** /v1/stocks/exchange/id/{exchange_id} | 
*StocksApi* | [**v1_stocks_get**](docs/StocksApi.md#v1_stocks_get) | **GET** /v1/stocks | 
*StocksApi* | [**v1_stocks_post**](docs/StocksApi.md#v1_stocks_post) | **POST** /v1/stocks | 


## Documentation For Models

 - [AddressResponse](docs/AddressResponse.md)
 - [Analyst](docs/Analyst.md)
 - [AnnualBalanceSheet](docs/AnnualBalanceSheet.md)
 - [AnnualBalanceSheetResponse](docs/AnnualBalanceSheetResponse.md)
 - [BalanceSheet](docs/BalanceSheet.md)
 - [BalanceSheets](docs/BalanceSheets.md)
 - [ContractResponse](docs/ContractResponse.md)
 - [Contracts](docs/Contracts.md)
 - [EODStock](docs/EODStock.md)
 - [EODStockListResponse](docs/EODStockListResponse.md)
 - [EODStockResponse](docs/EODStockResponse.md)
 - [Exchange](docs/Exchange.md)
 - [ExchangeListResponse](docs/ExchangeListResponse.md)
 - [ExchangeListedCompaniesResponse](docs/ExchangeListedCompaniesResponse.md)
 - [ExchangeListedStock](docs/ExchangeListedStock.md)
 - [ExchangeRequest](docs/ExchangeRequest.md)
 - [ExchangeResponse](docs/ExchangeResponse.md)
 - [ExchangeWithListedTickers](docs/ExchangeWithListedTickers.md)
 - [ExchangeWithTickers](docs/ExchangeWithTickers.md)
 - [General](docs/General.md)
 - [GeneralAddress](docs/GeneralAddress.md)
 - [GeneralContact](docs/GeneralContact.md)
 - [GeneralListings](docs/GeneralListings.md)
 - [GeneralOfficers](docs/GeneralOfficers.md)
 - [GeneralResponse](docs/GeneralResponse.md)
 - [Highlights](docs/Highlights.md)
 - [HighlightsResponse](docs/HighlightsResponse.md)
 - [News](docs/News.md)
 - [NewsResponseList](docs/NewsResponseList.md)
 - [NumberDividendsByYear](docs/NumberDividendsByYear.md)
 - [Options](docs/Options.md)
 - [OptionsResponse](docs/OptionsResponse.md)
 - [Payload](docs/Payload.md)
 - [PublicFundamental](docs/PublicFundamental.md)
 - [PublicFundamentalsResponse](docs/PublicFundamentalsResponse.md)
 - [QuarterlyBalanceResponse](docs/QuarterlyBalanceResponse.md)
 - [QuarterlyBalanceSheet](docs/QuarterlyBalanceSheet.md)
 - [RelatedTickers](docs/RelatedTickers.md)
 - [Resolution](docs/Resolution.md)
 - [Sentiment](docs/Sentiment.md)
 - [ShareStats](docs/ShareStats.md)
 - [SplitDividends](docs/SplitDividends.md)
 - [Stock](docs/Stock.md)
 - [Stock1](docs/Stock1.md)
 - [StockListRequest](docs/StockListRequest.md)
 - [StockListResponse](docs/StockListResponse.md)
 - [StockResponse](docs/StockResponse.md)
 - [StockTrendSetters](docs/StockTrendSetters.md)
 - [Technicals](docs/Technicals.md)
 - [Thumbnail](docs/Thumbnail.md)
 - [TickerExchangeCode](docs/TickerExchangeCode.md)
 - [Valuations](docs/Valuations.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

support@eod-stock-api.site


