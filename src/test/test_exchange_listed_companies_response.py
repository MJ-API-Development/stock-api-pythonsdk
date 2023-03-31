# coding: utf-8

"""
    EOD STOCK API

     <h2>Intelligent EOD Stocks API</h2>     <p>     End of day stock world wide STOCK API, this api is intended for use by web application developers,      and service providers looking for up-to-date always available.     <ul>         <li>Exchange Information</li>         <li>Stock Tickers Data</li>         <li>End of Day (EOD) Stock Data</li>         <li>Fundamental Data</li>         <li>Stock Options And Splits Data</li>         <li>Financial News API</li>         <li>Social Media Trend Data For Stocks</li>         <li>Sentiment Analysis for News & Social Media</li>     </ul>                The information provided covers more than 150 000 tickers, stocks, mutual funds and more around the world.         we provide information for any period, including daily, weekly.     </p>    # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@eod-stock-api.site
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.exchange_listed_companies_response import ExchangeListedCompaniesResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestExchangeListedCompaniesResponse(unittest.TestCase):
    """ExchangeListedCompaniesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExchangeListedCompaniesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.exchange_listed_companies_response.ExchangeListedCompaniesResponse()  # noqa: E501
        if include_optional :
            return ExchangeListedCompaniesResponse(
                message = '0', 
                payload = openapi_client.models.general.General(
                    cik = '0', 
                    country_name = '0', 
                    currency = '0', 
                    cusip = '0', 
                    description = '0', 
                    employer_id = '0', 
                    exchange = '0', 
                    fiscal_year_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    fundamental_id = '0', 
                    gic_group = '0', 
                    gic_industry = '0', 
                    gic_sector = '0', 
                    home_category = '0', 
                    industry = '0', 
                    international_domestic = True, 
                    ipo_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    is_delisted = True, 
                    isin = '0', 
                    name = '0', 
                    sector = '0', 
                    stock_symbol = '0', 
                    type = '0', ), 
                status = True
            )
        else :
            return ExchangeListedCompaniesResponse(
        )

    def testExchangeListedCompaniesResponse(self):
        """Test ExchangeListedCompaniesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
