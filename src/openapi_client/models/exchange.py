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

from openapi_client.configuration import Configuration


class Exchange(object):
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
        'code': 'str',
        'country': 'str',
        'currency_symbol': 'str',
        'exchange_id': 'str',
        'name': 'str',
        'operating_mic': 'str'
    }

    attribute_map = {
        'code': 'code',
        'country': 'country',
        'currency_symbol': 'currency_symbol',
        'exchange_id': 'exchange_id',
        'name': 'name',
        'operating_mic': 'operating_mic'
    }

    def __init__(self, code=None, country=None, currency_symbol=None, exchange_id=None, name=None, operating_mic=None, local_vars_configuration=None):  # noqa: E501
        """Exchange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._country = None
        self._currency_symbol = None
        self._exchange_id = None
        self._name = None
        self._operating_mic = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if country is not None:
            self.country = country
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if name is not None:
            self.name = name
        if operating_mic is not None:
            self.operating_mic = operating_mic

    @property
    def code(self):
        """Gets the code of this Exchange.  # noqa: E501

        exchange_code code  # noqa: E501

        :return: The code of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Exchange.

        exchange_code code  # noqa: E501

        :param code: The code of this Exchange.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def country(self):
        """Gets the country of this Exchange.  # noqa: E501

        the country the exchange_code operates in  # noqa: E501

        :return: The country of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Exchange.

        the country the exchange_code operates in  # noqa: E501

        :param country: The country of this Exchange.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this Exchange.  # noqa: E501

        the currency symbol of the country the exchange_code operates in  # noqa: E501

        :return: The currency_symbol of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this Exchange.

        the currency symbol of the country the exchange_code operates in  # noqa: E501

        :param currency_symbol: The currency_symbol of this Exchange.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def exchange_id(self):
        """Gets the exchange_id of this Exchange.  # noqa: E501

        exchange_code unique id  # noqa: E501

        :return: The exchange_id of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this Exchange.

        exchange_code unique id  # noqa: E501

        :param exchange_id: The exchange_id of this Exchange.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def name(self):
        """Gets the name of this Exchange.  # noqa: E501

        name of exchange_code  # noqa: E501

        :return: The name of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Exchange.

        name of exchange_code  # noqa: E501

        :param name: The name of this Exchange.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def operating_mic(self):
        """Gets the operating_mic of this Exchange.  # noqa: E501

        exchange_code operating mic  # noqa: E501

        :return: The operating_mic of this Exchange.  # noqa: E501
        :rtype: str
        """
        return self._operating_mic

    @operating_mic.setter
    def operating_mic(self, operating_mic):
        """Sets the operating_mic of this Exchange.

        exchange_code operating mic  # noqa: E501

        :param operating_mic: The operating_mic of this Exchange.  # noqa: E501
        :type: str
        """

        self._operating_mic = operating_mic

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
        if not isinstance(other, Exchange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Exchange):
            return True

        return self.to_dict() != other.to_dict()
