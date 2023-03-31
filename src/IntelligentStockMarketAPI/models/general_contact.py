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


class GeneralContact(object):
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
        'full_time_employees': 'int',
        'fundamental_id': 'str',
        'logo_url': 'str',
        'phone': 'str',
        'updated_at': 'date',
        'web_url': 'str'
    }

    attribute_map = {
        'full_time_employees': 'full_time_employees',
        'fundamental_id': 'fundamental_id',
        'logo_url': 'logo_url',
        'phone': 'phone',
        'updated_at': 'updated_at',
        'web_url': 'web_url'
    }

    def __init__(self, full_time_employees=None, fundamental_id=None, logo_url=None, phone=None, updated_at=None, web_url=None, local_vars_configuration=None):  # noqa: E501
        """GeneralContact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._full_time_employees = None
        self._fundamental_id = None
        self._logo_url = None
        self._phone = None
        self._updated_at = None
        self._web_url = None
        self.discriminator = None

        if full_time_employees is not None:
            self.full_time_employees = full_time_employees
        if fundamental_id is not None:
            self.fundamental_id = fundamental_id
        if logo_url is not None:
            self.logo_url = logo_url
        if phone is not None:
            self.phone = phone
        if updated_at is not None:
            self.updated_at = updated_at
        if web_url is not None:
            self.web_url = web_url

    @property
    def full_time_employees(self):
        """Gets the full_time_employees of this GeneralContact.  # noqa: E501

        Total number of full time employees  # noqa: E501

        :return: The full_time_employees of this GeneralContact.  # noqa: E501
        :rtype: int
        """
        return self._full_time_employees

    @full_time_employees.setter
    def full_time_employees(self, full_time_employees):
        """Sets the full_time_employees of this GeneralContact.

        Total number of full time employees  # noqa: E501

        :param full_time_employees: The full_time_employees of this GeneralContact.  # noqa: E501
        :type: int
        """

        self._full_time_employees = full_time_employees

    @property
    def fundamental_id(self):
        """Gets the fundamental_id of this GeneralContact.  # noqa: E501

        a unique id for the General Fundamental Company Data  # noqa: E501

        :return: The fundamental_id of this GeneralContact.  # noqa: E501
        :rtype: str
        """
        return self._fundamental_id

    @fundamental_id.setter
    def fundamental_id(self, fundamental_id):
        """Sets the fundamental_id of this GeneralContact.

        a unique id for the General Fundamental Company Data  # noqa: E501

        :param fundamental_id: The fundamental_id of this GeneralContact.  # noqa: E501
        :type: str
        """

        self._fundamental_id = fundamental_id

    @property
    def logo_url(self):
        """Gets the logo_url of this GeneralContact.  # noqa: E501

        Link  to Official Company logo  # noqa: E501

        :return: The logo_url of this GeneralContact.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this GeneralContact.

        Link  to Official Company logo  # noqa: E501

        :param logo_url: The logo_url of this GeneralContact.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def phone(self):
        """Gets the phone of this GeneralContact.  # noqa: E501

        Official Company Phone Number  # noqa: E501

        :return: The phone of this GeneralContact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this GeneralContact.

        Official Company Phone Number  # noqa: E501

        :param phone: The phone of this GeneralContact.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def updated_at(self):
        """Gets the updated_at of this GeneralContact.  # noqa: E501

        the date the company details where last updated  # noqa: E501

        :return: The updated_at of this GeneralContact.  # noqa: E501
        :rtype: date
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GeneralContact.

        the date the company details where last updated  # noqa: E501

        :param updated_at: The updated_at of this GeneralContact.  # noqa: E501
        :type: date
        """

        self._updated_at = updated_at

    @property
    def web_url(self):
        """Gets the web_url of this GeneralContact.  # noqa: E501

        official company website address  # noqa: E501

        :return: The web_url of this GeneralContact.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this GeneralContact.

        official company website address  # noqa: E501

        :param web_url: The web_url of this GeneralContact.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

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
        if not isinstance(other, GeneralContact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralContact):
            return True

        return self.to_dict() != other.to_dict()