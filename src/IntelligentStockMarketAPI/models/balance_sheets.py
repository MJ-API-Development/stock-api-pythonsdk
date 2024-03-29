# coding: utf-8

"""
    EOD STOCK API

     <h2>Intelligent EOD Stocks API</h2>     <p>     End of day stock world wide STOCK API, this api is intended for use by web application developers,      and service providers looking for up-to-date always available.     <ul>         <li>Exchange Information</li>         <li>Stock Tickers Data</li>         <li>End of Day (EOD) Stock Data</li>         <li>Fundamental Data</li>         <li>Stock Options And Splits Data</li>         <li>Financial News API</li>         <li>Social Media Trend Data For Stocks</li>         <li>Sentiment Analysis for News & Social Media</li>     </ul>                The information provided covers more than 150 000 tickers, stocks, mutual funds and more around the world.         we provide information for any period, including daily, weekly.     </p>    # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@eod-stock-api.site
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from src.IntelligentStockMarketAPI.configuration import Configuration


class BalanceSheets(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'annual_balance_sheets': 'AnnualBalanceSheet',
        'quarterly_balance_sheets': 'QuarterlyBalanceSheet'
    }

    attribute_map = {
        'annual_balance_sheets': 'annual_balance_sheets',
        'quarterly_balance_sheets': 'quarterly_balance_sheets'
    }

    def __init__(self, annual_balance_sheets=None, quarterly_balance_sheets=None, local_vars_configuration=None):  # noqa: E501
        """BalanceSheets - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annual_balance_sheets = None
        self._quarterly_balance_sheets = None
        self.discriminator = None

        if annual_balance_sheets is not None:
            self.annual_balance_sheets = annual_balance_sheets
        if quarterly_balance_sheets is not None:
            self.quarterly_balance_sheets = quarterly_balance_sheets

    @property
    def annual_balance_sheets(self):
        """Gets the annual_balance_sheets of this BalanceSheets.  # noqa: E501


        :return: The annual_balance_sheets of this BalanceSheets.  # noqa: E501
        :rtype: AnnualBalanceSheet
        """
        return self._annual_balance_sheets

    @annual_balance_sheets.setter
    def annual_balance_sheets(self, annual_balance_sheets):
        """Sets the annual_balance_sheets of this BalanceSheets.


        :param annual_balance_sheets: The annual_balance_sheets of this BalanceSheets.  # noqa: E501
        :type: AnnualBalanceSheet
        """

        self._annual_balance_sheets = annual_balance_sheets

    @property
    def quarterly_balance_sheets(self):
        """Gets the quarterly_balance_sheets of this BalanceSheets.  # noqa: E501


        :return: The quarterly_balance_sheets of this BalanceSheets.  # noqa: E501
        :rtype: QuarterlyBalanceSheet
        """
        return self._quarterly_balance_sheets

    @quarterly_balance_sheets.setter
    def quarterly_balance_sheets(self, quarterly_balance_sheets):
        """Sets the quarterly_balance_sheets of this BalanceSheets.


        :param quarterly_balance_sheets: The quarterly_balance_sheets of this BalanceSheets.  # noqa: E501
        :type: QuarterlyBalanceSheet
        """

        self._quarterly_balance_sheets = quarterly_balance_sheets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BalanceSheets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BalanceSheets):
            return True

        return self.to_dict() != other.to_dict()
