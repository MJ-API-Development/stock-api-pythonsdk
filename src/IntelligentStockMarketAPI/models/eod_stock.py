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


class EODStock(object):
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
        'adjusted_close': 'int',
        'close': 'int',
        'code': 'str',
        'date': 'date',
        'high': 'int',
        'low': 'int',
        'market_capitalization': 'int',
        'name': 'str',
        'open': 'int',
        'previous_close': 'int',
        'type': 'str',
        'volume': 'int'
    }

    attribute_map = {
        'adjusted_close': 'adjusted_close',
        'close': 'close',
        'code': 'code',
        'date': 'date',
        'high': 'high',
        'low': 'low',
        'market_capitalization': 'market_capitalization',
        'name': 'name',
        'open': 'open',
        'previous_close': 'previous_close',
        'type': 'type',
        'volume': 'volume'
    }

    def __init__(self, adjusted_close=None, close=None, code=None, date=None, high=None, low=None, market_capitalization=None, name=None, open=None, previous_close=None, type=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """EODStock - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._adjusted_close = None
        self._close = None
        self._code = None
        self._date = None
        self._high = None
        self._low = None
        self._market_capitalization = None
        self._name = None
        self._open = None
        self._previous_close = None
        self._type = None
        self._volume = None
        self.discriminator = None

        if adjusted_close is not None:
            self.adjusted_close = adjusted_close
        if close is not None:
            self.close = close
        if code is not None:
            self.code = code
        if date is not None:
            self.date = date
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if market_capitalization is not None:
            self.market_capitalization = market_capitalization
        if name is not None:
            self.name = name
        if open is not None:
            self.open = open
        if previous_close is not None:
            self.previous_close = previous_close
        if type is not None:
            self.type = type
        if volume is not None:
            self.volume = volume

    @property
    def adjusted_close(self):
        """Gets the adjusted_close of this EODStock.  # noqa: E501

        Stock Adjusted Close Position  # noqa: E501

        :return: The adjusted_close of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._adjusted_close

    @adjusted_close.setter
    def adjusted_close(self, adjusted_close):
        """Sets the adjusted_close of this EODStock.

        Stock Adjusted Close Position  # noqa: E501

        :param adjusted_close: The adjusted_close of this EODStock.  # noqa: E501
        :type: int
        """

        self._adjusted_close = adjusted_close

    @property
    def close(self):
        """Gets the close of this EODStock.  # noqa: E501

        Stock Close Position  # noqa: E501

        :return: The close of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this EODStock.

        Stock Close Position  # noqa: E501

        :param close: The close of this EODStock.  # noqa: E501
        :type: int
        """

        self._close = close

    @property
    def code(self):
        """Gets the code of this EODStock.  # noqa: E501

        stock code  # noqa: E501

        :return: The code of this EODStock.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EODStock.

        stock code  # noqa: E501

        :param code: The code of this EODStock.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def date(self):
        """Gets the date of this EODStock.  # noqa: E501

        date of stock trade  # noqa: E501

        :return: The date of this EODStock.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EODStock.

        date of stock trade  # noqa: E501

        :param date: The date of this EODStock.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def high(self):
        """Gets the high of this EODStock.  # noqa: E501

        Stock High Position  # noqa: E501

        :return: The high of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this EODStock.

        Stock High Position  # noqa: E501

        :param high: The high of this EODStock.  # noqa: E501
        :type: int
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this EODStock.  # noqa: E501

        Stock Low Position  # noqa: E501

        :return: The low of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this EODStock.

        Stock Low Position  # noqa: E501

        :param low: The low of this EODStock.  # noqa: E501
        :type: int
        """

        self._low = low

    @property
    def market_capitalization(self):
        """Gets the market_capitalization of this EODStock.  # noqa: E501

        market capitalization  # noqa: E501

        :return: The market_capitalization of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._market_capitalization

    @market_capitalization.setter
    def market_capitalization(self, market_capitalization):
        """Sets the market_capitalization of this EODStock.

        market capitalization  # noqa: E501

        :param market_capitalization: The market_capitalization of this EODStock.  # noqa: E501
        :type: int
        """

        self._market_capitalization = market_capitalization

    @property
    def name(self):
        """Gets the name of this EODStock.  # noqa: E501

        name of exchange_code  # noqa: E501

        :return: The name of this EODStock.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EODStock.

        name of exchange_code  # noqa: E501

        :param name: The name of this EODStock.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def open(self):
        """Gets the open of this EODStock.  # noqa: E501

        Stock Open Position  # noqa: E501

        :return: The open of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this EODStock.

        Stock Open Position  # noqa: E501

        :param open: The open of this EODStock.  # noqa: E501
        :type: int
        """

        self._open = open

    @property
    def previous_close(self):
        """Gets the previous_close of this EODStock.  # noqa: E501

        Stock Previous Close Position  # noqa: E501

        :return: The previous_close of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._previous_close

    @previous_close.setter
    def previous_close(self, previous_close):
        """Sets the previous_close of this EODStock.

        Stock Previous Close Position  # noqa: E501

        :param previous_close: The previous_close of this EODStock.  # noqa: E501
        :type: int
        """

        self._previous_close = previous_close

    @property
    def type(self):
        """Gets the type of this EODStock.  # noqa: E501

        type of stock  # noqa: E501

        :return: The type of this EODStock.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EODStock.

        type of stock  # noqa: E501

        :param type: The type of this EODStock.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def volume(self):
        """Gets the volume of this EODStock.  # noqa: E501

        Stock Volume Traded  # noqa: E501

        :return: The volume of this EODStock.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this EODStock.

        Stock Volume Traded  # noqa: E501

        :param volume: The volume of this EODStock.  # noqa: E501
        :type: int
        """

        self._volume = volume

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
        if not isinstance(other, EODStock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EODStock):
            return True

        return self.to_dict() != other.to_dict()
