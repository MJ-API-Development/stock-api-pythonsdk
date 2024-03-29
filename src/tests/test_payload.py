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
from src.IntelligentStockMarketAPI.models.payload import Payload  # noqa: E501
from src.IntelligentStockMarketAPI.rest import ApiException

class TestPayload(unittest.TestCase):
    """Payload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Payload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = src.IntelligentStockMarketAPI.models.payload.Payload()  # noqa: E501
        if include_optional :
            return Payload(
                followers_count = 56, 
                friends_count = 56, 
                location = '0', 
                name = '0', 
                profile_image_url = '0', 
                screen_name = '0', 
                sentiments = [
                    src.IntelligentStockMarketAPI.models.sentiment.Sentiment(
                        created_at = '0', 
                        favourite_count = 56, 
                        retweet_count = 56, 
                        sentiment = '0', 
                        sentiment_id = '0', 
                        stock_code = '0', 
                        tweet_id = '0', 
                        tweet_link = '0', 
                        tweet_text = '0', 
                        uid = '0', )
                    ], 
                statuses_count = 56, 
                total_bearish = 56, 
                total_bullish = 56, 
                tweeter_profile_link = '0', 
                uid = '0'
            )
        else :
            return Payload(
        )

    def testPayload(self):
        """Test Payload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
