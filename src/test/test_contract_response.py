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

import src.IntelligentStockMarketAPI
from src.IntelligentStockMarketAPI.models.contract_response import ContractResponse  # noqa: E501
from src.IntelligentStockMarketAPI.rest import ApiException

class TestContractResponse(unittest.TestCase):
    """ContractResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = src.IntelligentStockMarketAPI.models.contract_response.ContractResponse()  # noqa: E501
        if include_optional :
            return ContractResponse(
                message = '0', 
                payload = src.IntelligentStockMarketAPI.models.contracts.Contracts(
                    ask = 1.337, 
                    bid = 1.337, 
                    call_put_id = '0', 
                    change = 1.337, 
                    change_percent = 1.337, 
                    contract_name = '0', 
                    contract_period = 1.337, 
                    contract_size = 1.337, 
                    currency = '0', 
                    days_before_expiration = 1.337, 
                    delta = 1.337, 
                    expiration_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    gamma = 1.337, 
                    implied_volatility = 1.337, 
                    in_the_money = True, 
                    intrinsic_value = 1.337, 
                    last_price = 1.337, 
                    last_trade_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    open_interest = 1.337, 
                    rho = 1.337, 
                    strike = 1.337, 
                    theoretical = 1.337, 
                    theta = 1.337, 
                    time_value = 1.337, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    vega = 1.337, 
                    volume = 1.337, ), 
                status = True
            )
        else :
            return ContractResponse(
        )

    def testContractResponse(self):
        """Test ContractResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
