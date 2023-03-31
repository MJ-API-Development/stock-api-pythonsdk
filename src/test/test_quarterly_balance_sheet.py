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
from openapi_client.models.quarterly_balance_sheet import QuarterlyBalanceSheet  # noqa: E501
from openapi_client.rest import ApiException

class TestQuarterlyBalanceSheet(unittest.TestCase):
    """QuarterlyBalanceSheet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QuarterlyBalanceSheet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.quarterly_balance_sheet.QuarterlyBalanceSheet()  # noqa: E501
        if include_optional :
            return QuarterlyBalanceSheet(
                balance_sheet = openapi_client.models._balance_sheet._BalanceSheet(
                    accounts_payable = 1.337, 
                    accumulated_amortization = 1.337, 
                    accumulated_depreciation = 1.337, 
                    accumulated_other_comprehensive_income = 1.337, 
                    additional_paid_in_capital = 1.337, 
                    balance_sheet_id = '0', 
                    capital_lease_obligations = 1.337, 
                    capital_surplus = 1.337, 
                    cash = 1.337, 
                    cash_and_short_term_investments = 1.337, 
                    common_stock = 1.337, 
                    common_stock_shares_outstanding = 1.337, 
                    common_stock_total_equity = 1.337, 
                    currency = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    deferred_long_term_liability = 1.337, 
                    earnings_assets = 1.337, 
                    fundamental_id = '0', 
                    good_will = 1.337, 
                    intangible_assets = 1.337, 
                    inventory = 1.337, 
                    long_term_debt = 1.337, 
                    long_term_debt_total = 1.337, 
                    long_term_investments = 1.337, 
                    negative_good_will = 1.337, 
                    net_debt = 1.337, 
                    net_invested_capital = 1.337, 
                    net_receivables = 1.337, 
                    net_tangible_assets = 1.337, 
                    networking_capital = 1.337, 
                    non_controlling_interest_in_consolidated_equity = 1.337, 
                    non_current_assets_other = 1.337, 
                    non_current_liabilities_other = 1.337, 
                    non_current_liabilities_total = 1.337, 
                    other_assets = 1.337, 
                    other_current_assets = 1.337, 
                    other_current_liability = 1.337, 
                    other_liability = 1.337, 
                    other_stock_holder_equity = 1.337, 
                    preferred_stock_redeemable = 1.337, 
                    preferred_stock_total_equity = 1.337, 
                    property_plant_and_equipment_gross = 1.337, 
                    property_plant_equipment = 1.337, 
                    retained_earnings = 1.337, 
                    retained_earnings_total_equity = 1.337, 
                    short_long_term_debt_total = 1.337, 
                    short_term_debt = 1.337, 
                    short_term_investments = 1.337, 
                    temporary_equity_redeemable_non_controlling_interests = 1.337, 
                    total_assets = 1.337, 
                    total_current_assets = 1.337, 
                    total_current_liabilities = 1.337, 
                    total_liability = 1.337, 
                    total_permanent_equity = 1.337, 
                    total_stock_holder_equity = 1.337, 
                    treasury_stock = 1.337, 
                    warrants = 1.337, ), 
                filing_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return QuarterlyBalanceSheet(
        )

    def testQuarterlyBalanceSheet(self):
        """Test QuarterlyBalanceSheet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
