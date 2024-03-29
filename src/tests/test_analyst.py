# coding: utf-8

"""
    EOD STOCK API

     <h2>Intelligent EOD Stocks API</h2>     <p>     End of day stock world wide STOCK API, this api is intended for use by web application developers,      and service providers looking for up-to-date always available.     <ul>         <li>Exchange Information</li>         <li>Stock Tickers Data</li>         <li>End of Day (EOD) Stock Data</li>         <li>Fundamental Data</li>         <li>Stock Options And Splits Data</li>         <li>Financial News API</li>         <li>Social Media Trend Data For Stocks</li>         <li>Sentiment Analysis for News & Social Media</li>     </ul>                The information provided covers more than 150 000 tickers, stocks, mutual funds and more around the world.         we provide information for any period, including daily, weekly.     </p>    # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@eod-stock-api.site
"""

from __future__ import absolute_import

import unittest

from src.IntelligentStockMarketAPI.models.analyst import Analyst  # noqa: E501


# noinspection PyMethodMayBeStatic
class TestAnalyst(unittest.TestCase):
    """Analyst unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Analyst
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = src.IntelligentStockMarketAPI.models.analyst.Analyst()  # noqa: E501
        if include_optional:
            return Analyst(
                buy=56,
                fundamental_id='0',
                hold=56,
                rating=1.337,
                sell=56,
                strong_buy=56,
                strong_sell=56,
                target_price=1.337
            )
        else:
            return Analyst(
            )

    def testAnalyst(self):
        """Test Analyst"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
