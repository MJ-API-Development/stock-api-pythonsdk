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
from src.IntelligentStockMarketAPI.models.news import News  # noqa: E501
from src.IntelligentStockMarketAPI.rest import ApiException

class TestNews(unittest.TestCase):
    """News unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test News
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = src.IntelligentStockMarketAPI.models.news.News()  # noqa: E501
        if include_optional :
            return News(
                link = '0', 
                provider_publish_time = 56, 
                publisher = '0', 
                related_tickers = src.IntelligentStockMarketAPI.models.related_tickers.RelatedTickers(
                    ticker = '0', ), 
                thumbnail = src.IntelligentStockMarketAPI.models.thumbnail.Thumbnail(
                    resolutions = src.IntelligentStockMarketAPI.models.resolution.Resolution(
                        height = 56, 
                        tag = '0', 
                        url = '0', 
                        width = 56, ), ), 
                title = '0', 
                type = '0', 
                uuid = '0'
            )
        else :
            return News(
        )

    def testNews(self):
        """Test News"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
