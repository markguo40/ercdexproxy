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


class IGetMarketOrderQuoteByPercentageRequest(object):
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
        'taker_address': 'str',
        'pair': 'str',
        'side': 'str',
        'percentage': 'float'
    }

    attribute_map = {
        'taker_address': 'takerAddress',
        'pair': 'pair',
        'side': 'side',
        'percentage': 'percentage'
    }

    def __init__(self, taker_address=None, pair=None, side=None, percentage=None):  # noqa: E501
        """IGetMarketOrderQuoteByPercentageRequest - a model defined in Swagger"""  # noqa: E501

        self._taker_address = None
        self._pair = None
        self._side = None
        self._percentage = None
        self.discriminator = None

        self.taker_address = taker_address
        self.pair = pair
        self.side = side
        self.percentage = percentage

    @property
    def taker_address(self):
        """Gets the taker_address of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501

        Wallet address of intended taker  # noqa: E501

        :return: The taker_address of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :rtype: str
        """
        return self._taker_address

    @taker_address.setter
    def taker_address(self, taker_address):
        """Sets the taker_address of this IGetMarketOrderQuoteByPercentageRequest.

        Wallet address of intended taker  # noqa: E501

        :param taker_address: The taker_address of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :type: str
        """
        if taker_address is None:
            raise ValueError("Invalid value for `taker_address`, must not be `None`")  # noqa: E501

        self._taker_address = taker_address

    @property
    def pair(self):
        """Gets the pair of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501

        Token pair in BASE/QUOTE format  # noqa: E501

        :return: The pair of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :rtype: str
        """
        return self._pair

    @pair.setter
    def pair(self, pair):
        """Sets the pair of this IGetMarketOrderQuoteByPercentageRequest.

        Token pair in BASE/QUOTE format  # noqa: E501

        :param pair: The pair of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :type: str
        """
        if pair is None:
            raise ValueError("Invalid value for `pair`, must not be `None`")  # noqa: E501

        self._pair = pair

    @property
    def side(self):
        """Gets the side of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501

        Trade side: 'buy' or 'sell'  # noqa: E501

        :return: The side of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this IGetMarketOrderQuoteByPercentageRequest.

        Trade side: 'buy' or 'sell'  # noqa: E501

        :param side: The side of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        allowed_values = ["buy", "sell"]  # noqa: E501
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def percentage(self):
        """Gets the percentage of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501

        Percentage (integer, 1-100)  # noqa: E501

        :return: The percentage of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this IGetMarketOrderQuoteByPercentageRequest.

        Percentage (integer, 1-100)  # noqa: E501

        :param percentage: The percentage of this IGetMarketOrderQuoteByPercentageRequest.  # noqa: E501
        :type: float
        """
        if percentage is None:
            raise ValueError("Invalid value for `percentage`, must not be `None`")  # noqa: E501

        self._percentage = percentage

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
        if not isinstance(other, IGetMarketOrderQuoteByPercentageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
