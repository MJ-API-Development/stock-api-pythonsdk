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


class Valuations(object):
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
        'date_created': 'date',
        'enterprise_value': 'int',
        'enterprise_value_ebitda': 'float',
        'enterprise_value_revenue': 'float',
        'forward_pe': 'float',
        'fundamental_id': 'str',
        'price_book_mrq': 'float',
        'price_sales_ttm': 'float',
        'trailing_pe': 'float'
    }

    attribute_map = {
        'date_created': 'date_created',
        'enterprise_value': 'enterprise_value',
        'enterprise_value_ebitda': 'enterprise_value_ebitda',
        'enterprise_value_revenue': 'enterprise_value_revenue',
        'forward_pe': 'forward_pe',
        'fundamental_id': 'fundamental_id',
        'price_book_mrq': 'price_book_mrq',
        'price_sales_ttm': 'price_sales_ttm',
        'trailing_pe': 'trailing_pe'
    }

    def __init__(self, date_created=None, enterprise_value=None, enterprise_value_ebitda=None, enterprise_value_revenue=None, forward_pe=None, fundamental_id=None, price_book_mrq=None, price_sales_ttm=None, trailing_pe=None, local_vars_configuration=None):  # noqa: E501
        """Valuations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date_created = None
        self._enterprise_value = None
        self._enterprise_value_ebitda = None
        self._enterprise_value_revenue = None
        self._forward_pe = None
        self._fundamental_id = None
        self._price_book_mrq = None
        self._price_sales_ttm = None
        self._trailing_pe = None
        self.discriminator = None

        if date_created is not None:
            self.date_created = date_created
        if enterprise_value is not None:
            self.enterprise_value = enterprise_value
        if enterprise_value_ebitda is not None:
            self.enterprise_value_ebitda = enterprise_value_ebitda
        if enterprise_value_revenue is not None:
            self.enterprise_value_revenue = enterprise_value_revenue
        if forward_pe is not None:
            self.forward_pe = forward_pe
        if fundamental_id is not None:
            self.fundamental_id = fundamental_id
        if price_book_mrq is not None:
            self.price_book_mrq = price_book_mrq
        if price_sales_ttm is not None:
            self.price_sales_ttm = price_sales_ttm
        if trailing_pe is not None:
            self.trailing_pe = trailing_pe

    @property
    def date_created(self):
        """Gets the date_created of this Valuations.  # noqa: E501

        Date of valuation  # noqa: E501

        :return: The date_created of this Valuations.  # noqa: E501
        :rtype: date
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Valuations.

        Date of valuation  # noqa: E501

        :param date_created: The date_created of this Valuations.  # noqa: E501
        :type: date
        """

        self._date_created = date_created

    @property
    def enterprise_value(self):
        """Gets the enterprise_value of this Valuations.  # noqa: E501

        Enterprise value  # noqa: E501

        :return: The enterprise_value of this Valuations.  # noqa: E501
        :rtype: int
        """
        return self._enterprise_value

    @enterprise_value.setter
    def enterprise_value(self, enterprise_value):
        """Sets the enterprise_value of this Valuations.

        Enterprise value  # noqa: E501

        :param enterprise_value: The enterprise_value of this Valuations.  # noqa: E501
        :type: int
        """

        self._enterprise_value = enterprise_value

    @property
    def enterprise_value_ebitda(self):
        """Gets the enterprise_value_ebitda of this Valuations.  # noqa: E501

        Enterprise value/EBITDA is a popular valuation manyple used to determine the fair market value of a company.  # noqa: E501

        :return: The enterprise_value_ebitda of this Valuations.  # noqa: E501
        :rtype: float
        """
        return self._enterprise_value_ebitda

    @enterprise_value_ebitda.setter
    def enterprise_value_ebitda(self, enterprise_value_ebitda):
        """Sets the enterprise_value_ebitda of this Valuations.

        Enterprise value/EBITDA is a popular valuation manyple used to determine the fair market value of a company.  # noqa: E501

        :param enterprise_value_ebitda: The enterprise_value_ebitda of this Valuations.  # noqa: E501
        :type: float
        """

        self._enterprise_value_ebitda = enterprise_value_ebitda

    @property
    def enterprise_value_revenue(self):
        """Gets the enterprise_value_revenue of this Valuations.  # noqa: E501

        The enterprise value-to-revenue manyple (EV/R) is a measure of the value of a stock that compares a company's enterprise value to its revenue.  # noqa: E501

        :return: The enterprise_value_revenue of this Valuations.  # noqa: E501
        :rtype: float
        """
        return self._enterprise_value_revenue

    @enterprise_value_revenue.setter
    def enterprise_value_revenue(self, enterprise_value_revenue):
        """Sets the enterprise_value_revenue of this Valuations.

        The enterprise value-to-revenue manyple (EV/R) is a measure of the value of a stock that compares a company's enterprise value to its revenue.  # noqa: E501

        :param enterprise_value_revenue: The enterprise_value_revenue of this Valuations.  # noqa: E501
        :type: float
        """

        self._enterprise_value_revenue = enterprise_value_revenue

    @property
    def forward_pe(self):
        """Gets the forward_pe of this Valuations.  # noqa: E501

        A variation of the price-to-earnings ratio (P/E ratio) is the forward P/E ratio, which is based on a prediction of a company's future earnings  # noqa: E501

        :return: The forward_pe of this Valuations.  # noqa: E501
        :rtype: float
        """
        return self._forward_pe

    @forward_pe.setter
    def forward_pe(self, forward_pe):
        """Sets the forward_pe of this Valuations.

        A variation of the price-to-earnings ratio (P/E ratio) is the forward P/E ratio, which is based on a prediction of a company's future earnings  # noqa: E501

        :param forward_pe: The forward_pe of this Valuations.  # noqa: E501
        :type: float
        """

        self._forward_pe = forward_pe

    @property
    def fundamental_id(self):
        """Gets the fundamental_id of this Valuations.  # noqa: E501

        Fundamental id  # noqa: E501

        :return: The fundamental_id of this Valuations.  # noqa: E501
        :rtype: str
        """
        return self._fundamental_id

    @fundamental_id.setter
    def fundamental_id(self, fundamental_id):
        """Sets the fundamental_id of this Valuations.

        Fundamental id  # noqa: E501

        :param fundamental_id: The fundamental_id of this Valuations.  # noqa: E501
        :type: str
        """

        self._fundamental_id = fundamental_id

    @property
    def price_book_mrq(self):
        """Gets the price_book_mrq of this Valuations.  # noqa: E501

        This is the Current Price divided by the latest annual Tangible Book Value Per Share.  # noqa: E501

        :return: The price_book_mrq of this Valuations.  # noqa: E501
        :rtype: float
        """
        return self._price_book_mrq

    @price_book_mrq.setter
    def price_book_mrq(self, price_book_mrq):
        """Sets the price_book_mrq of this Valuations.

        This is the Current Price divided by the latest annual Tangible Book Value Per Share.  # noqa: E501

        :param price_book_mrq: The price_book_mrq of this Valuations.  # noqa: E501
        :type: float
        """

        self._price_book_mrq = price_book_mrq

    @property
    def price_sales_ttm(self):
        """Gets the price_sales_ttm of this Valuations.  # noqa: E501

        The price-to-sales ratio shows how much the market values every dollar of the company's sales.  # noqa: E501

        :return: The price_sales_ttm of this Valuations.  # noqa: E501
        :rtype: float
        """
        return self._price_sales_ttm

    @price_sales_ttm.setter
    def price_sales_ttm(self, price_sales_ttm):
        """Sets the price_sales_ttm of this Valuations.

        The price-to-sales ratio shows how much the market values every dollar of the company's sales.  # noqa: E501

        :param price_sales_ttm: The price_sales_ttm of this Valuations.  # noqa: E501
        :type: float
        """

        self._price_sales_ttm = price_sales_ttm

    @property
    def trailing_pe(self):
        """Gets the trailing_pe of this Valuations.  # noqa: E501

         relative valuation multiple that is based on the last 12 months of actual earnings  # noqa: E501

        :return: The trailing_pe of this Valuations.  # noqa: E501
        :rtype: float
        """
        return self._trailing_pe

    @trailing_pe.setter
    def trailing_pe(self, trailing_pe):
        """Sets the trailing_pe of this Valuations.

         relative valuation multiple that is based on the last 12 months of actual earnings  # noqa: E501

        :param trailing_pe: The trailing_pe of this Valuations.  # noqa: E501
        :type: float
        """

        self._trailing_pe = trailing_pe

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
        if not isinstance(other, Valuations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Valuations):
            return True

        return self.to_dict() != other.to_dict()