# coding: utf-8

"""
    ERC dEX REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from erc_dex.models.fill_receipt import FillReceipt  # noqa: F401,E501


class IGetReceiptsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'float',
        'page': 'float',
        'per_page': 'float',
        'records': 'list[FillReceipt]'
    }

    attribute_map = {
        'total': 'total',
        'page': 'page',
        'per_page': 'per_page',
        'records': 'records'
    }

    def __init__(self, total=None, page=None, per_page=None, records=None):  # noqa: E501
        """IGetReceiptsResponse - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._page = None
        self._per_page = None
        self._records = None
        self.discriminator = None

        self.total = total
        self.page = page
        self.per_page = per_page
        self.records = records

    @property
    def total(self):
        """Gets the total of this IGetReceiptsResponse.  # noqa: E501


        :return: The total of this IGetReceiptsResponse.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this IGetReceiptsResponse.


        :param total: The total of this IGetReceiptsResponse.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def page(self):
        """Gets the page of this IGetReceiptsResponse.  # noqa: E501


        :return: The page of this IGetReceiptsResponse.  # noqa: E501
        :rtype: float
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this IGetReceiptsResponse.


        :param page: The page of this IGetReceiptsResponse.  # noqa: E501
        :type: float
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this IGetReceiptsResponse.  # noqa: E501


        :return: The per_page of this IGetReceiptsResponse.  # noqa: E501
        :rtype: float
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this IGetReceiptsResponse.


        :param per_page: The per_page of this IGetReceiptsResponse.  # noqa: E501
        :type: float
        """
        if per_page is None:
            raise ValueError("Invalid value for `per_page`, must not be `None`")  # noqa: E501

        self._per_page = per_page

    @property
    def records(self):
        """Gets the records of this IGetReceiptsResponse.  # noqa: E501


        :return: The records of this IGetReceiptsResponse.  # noqa: E501
        :rtype: list[FillReceipt]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this IGetReceiptsResponse.


        :param records: The records of this IGetReceiptsResponse.  # noqa: E501
        :type: list[FillReceipt]
        """
        if records is None:
            raise ValueError("Invalid value for `records`, must not be `None`")  # noqa: E501

        self._records = records

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, IGetReceiptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
