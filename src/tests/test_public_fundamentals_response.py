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
from src.IntelligentStockMarketAPI.models.public_fundamentals_response import PublicFundamentalsResponse  # noqa: E501
from src.IntelligentStockMarketAPI.rest import ApiException


# noinspection PyMethodMayBeStatic,DuplicatedCode
class TestPublicFundamentalsResponse(unittest.TestCase):
    """PublicFundamentalsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PublicFundamentalsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = src.IntelligentStockMarketAPI.models.public_fundamentals_response.PublicFundamentalsResponse()  # noqa: E501
        if include_optional:
            return PublicFundamentalsResponse(
                message='0',
                payload=src.IntelligentStockMarketAPI.models.public_fundamental.PublicFundamental(
                    address=src.IntelligentStockMarketAPI.models.general_address.GeneralAddress(
                        city='0',
                        country='0',
                        fundamental_id='0',
                        state='0',
                        street='0',
                        zip='0', ),
                    analyst_rankings=src.IntelligentStockMarketAPI.models.analyst.Analyst(
                        buy=56,
                        fundamental_id='0',
                        hold=56,
                        rating=1.337,
                        sell=56,
                        strong_buy=56,
                        strong_sell=56,
                        target_price=1.337, ),
                    balance_sheets=src.IntelligentStockMarketAPI.models.balance_sheets.BalanceSheets(
                        annual_balance_sheets=src.IntelligentStockMarketAPI.models.AnnualBalanceSheet(
                            balance_sheet=src.IntelligentStockMarketAPI.models.BalanceSheet(
                                accounts_payable=1.337,
                                accumulated_amortization=1.337,
                                accumulated_depreciation=1.337,
                                accumulated_other_comprehensive_income=1.337,
                                additional_paid_in_capital=1.337,
                                balance_sheet_id='0',
                                capital_lease_obligations=1.337,
                                capital_surplus=1.337,
                                cash=1.337,
                                cash_and_short_term_investments=1.337,
                                common_stock=1.337,
                                common_stock_shares_outstanding=1.337,
                                common_stock_total_equity=1.337,
                                currency='0',
                                date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                                deferred_long_term_liability=1.337,
                                earnings_assets=1.337,
                                fundamental_id='0',
                                good_will=1.337,
                                intangible_assets=1.337,
                                inventory=1.337,
                                long_term_debt=1.337,
                                long_term_debt_total=1.337,
                                long_term_investments=1.337,
                                negative_good_will=1.337,
                                net_debt=1.337,
                                net_invested_capital=1.337,
                                net_receivables=1.337,
                                net_tangible_assets=1.337,
                                networking_capital=1.337,
                                non_controlling_interest_in_consolidated_equity=1.337,
                                non_current_assets_other=1.337,
                                non_current_liabilities_other=1.337,
                                non_current_liabilities_total=1.337,
                                other_assets=1.337,
                                other_current_assets=1.337,
                                other_current_liability=1.337,
                                other_liability=1.337,
                                other_stock_holder_equity=1.337,
                                preferred_stock_redeemable=1.337,
                                preferred_stock_total_equity=1.337,
                                property_plant_and_equipment_gross=1.337,
                                property_plant_equipment=1.337,
                                retained_earnings=1.337,
                                retained_earnings_total_equity=1.337,
                                short_long_term_debt_total=1.337,
                                short_term_debt=1.337,
                                short_term_investments=1.337,
                                temporary_equity_redeemable_non_controlling_interests=1.337,
                                total_assets=1.337,
                                total_current_assets=1.337,
                                total_current_liabilities=1.337,
                                total_liability=1.337,
                                total_permanent_equity=1.337,
                                total_stock_holder_equity=1.337,
                                treasury_stock=1.337,
                                warrants=1.337, ),
                            filing_date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
                        quarterly_balance_sheets=src.IntelligentStockMarketAPI.models.quarterly_balance_sheet.QuarterlyBalanceSheet(
                            filing_date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ), ),
                    cik='0',
                    contact=src.IntelligentStockMarketAPI.models.general_contact.GeneralContact(
                        full_time_employees=56,
                        fundamental_id='0',
                        logo_url='0',
                        phone='0',
                        updated_at=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        web_url='0', ),
                    country_name='0',
                    currency='0',
                    cusip='0',
                    description='0',
                    employer_id='0',
                    exchange='0',
                    fiscal_year_end=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                    fundamental_id='0',
                    gic_group='0',
                    gic_industry='0',
                    gic_sector='0',
                    highlights=src.IntelligentStockMarketAPI.models.highlights.Highlights(
                        book_value=1.337,
                        date_created=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        diluted_eps_ttm=1.337,
                        dividend_share=1.337,
                        dividend_yield=1.337,
                        earnings_share=1.337,
                        ebitda=56,
                        eps_estimate_current_quarter=1.337,
                        eps_estimate_current_year=1.337,
                        eps_estimate_next_quarter=1.337,
                        eps_estimate_next_year=1.337,
                        fundamental_id='0',
                        growth_profit_ttm=1.337,
                        market_capitalization=56,
                        market_capitalization_mln=56,
                        most_recent_quarter=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        operating_margin_ttm=1.337,
                        pe_ratio=1.337,
                        peg_ratio=1.337,
                        profit_margin=1.337,
                        quarterly_earnings_growth_yoy=1.337,
                        quarterly_revenue_growth_yoy=1.337,
                        return_on_assets_ttm=1.337,
                        return_on_equity_ttm=1.337,
                        revenue_per_share_ttm=1.337,
                        revenue_ttm=1.337,
                        target_price=56, ),
                    home_category='0',
                    industry='0',
                    international_domestic=True,
                    ipo_date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                    is_delisted=True,
                    isin='0',
                    listings=src.IntelligentStockMarketAPI.models.general_listings.GeneralListings(
                        exchange='0',
                        fundamental_id='0',
                        listing_id='0',
                        name='0',
                        stock_symbol='0', ),
                    name='0',
                    officers=src.IntelligentStockMarketAPI.models.general_officers.GeneralOfficers(
                        fundamental_id='0',
                        name='0',
                        title='0',
                        year_born='0', ),
                    sector='0',
                    share_stats=src.IntelligentStockMarketAPI.models.share_stats.ShareStats(
                        date_created=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        fundamental_id='0',
                        percent_insiders=1.337,
                        percent_institutions=1.337,
                        shares_float=56,
                        shares_outstanding=56,
                        shares_short=56,
                        shares_short_prior_month=56,
                        short_percent_float=1.337,
                        short_percent_outstanding=1.337,
                        short_ratio=1.337, ),
                    split_dividends=src.IntelligentStockMarketAPI.models.split_dividends.SplitDividends(
                        date_created=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        dividend_date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        ex_dividend_date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        forward_annual_dividend_rate=1.337,
                        forward_annual_dividend_yield=1.337,
                        fundamental_id='0',
                        last_split_date=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        last_split_factor='0',
                        number_of_dividends_by_year=src.IntelligentStockMarketAPI.models.number_dividends_by_year.NumberDividendsByYear(
                            count=56,
                            year=56, ),
                        payout_ratio=1.337, ),
                    stock_symbol='0',
                    technicals=src.IntelligentStockMarketAPI.models.technicals.Technicals(
                        beta=1.337,
                        date_created=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        fundamental_id='0',
                        shares_short=56,
                        shares_short_prior_month=56,
                        short_percent=1.337,
                        short_ratio=1.337,
                        t_200_day_ma=1.337,
                        t_50_day_ma=1.337,
                        t_52_week_high=1.337,
                        t_52_week_low=1.337, ),
                    type='0',
                    valuation=src.IntelligentStockMarketAPI.models.valuations.Valuations(
                        date_created=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        enterprise_value=56,
                        enterprise_value_ebitda=1.337,
                        enterprise_value_revenue=1.337,
                        forward_pe=1.337,
                        fundamental_id='0',
                        price_book_mrq=1.337,
                        price_sales_ttm=1.337,
                        trailing_pe=1.337, ), ),
                status=True
            )
        else:
            return PublicFundamentalsResponse(
            )

    def testPublicFundamentalsResponse(self):
        """Test PublicFundamentalsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
