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

from erc_dex.models.order import Order  # noqa: F401,E501


class IExtendedOrderFill(object):
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
        'order_hash': 'str',
        'taker_amount': 'str',
        'order': 'Order'
    }

    attribute_map = {
        'order_hash': 'orderHash',
        'taker_amount': 'takerAmount',
        'order': 'order'
    }

    def __init__(self, order_hash=None, taker_amount=None, order=None):  # noqa: E501
        """IExtendedOrderFill - a model defined in Swagger"""  # noqa: E501

        self._order_hash = None
        self._taker_amount = None
        self._order = None
        self.discriminator = None

        self.order_hash = order_hash
        self.taker_amount = taker_amount
        self.order = order

    @property
    def order_hash(self):
        """Gets the order_hash of this IExtendedOrderFill.  # noqa: E501

        Computed hash verifying the authenticity of the order  # noqa: E501

        :return: The order_hash of this IExtendedOrderFill.  # noqa: E501
        :rtype: str
        """
        return self._order_hash

    @order_hash.setter
    def order_hash(self, order_hash):
        """Sets the order_hash of this IExtendedOrderFill.

        Computed hash verifying the authenticity of the order  # noqa: E501

        :param order_hash: The order_hash of this IExtendedOrderFill.  # noqa: E501
        :type: str
        """
        if order_hash is None:
            raise ValueError("Invalid value for `order_hash`, must not be `None`")  # noqa: E501

        self._order_hash = order_hash

    @property
    def taker_amount(self):
        """Gets the taker_amount of this IExtendedOrderFill.  # noqa: E501

        Taker amount in base units to fill from this order  # noqa: E501

        :return: The taker_amount of this IExtendedOrderFill.  # noqa: E501
        :rtype: str
        """
        return self._taker_amount

    @taker_amount.setter
    def taker_amount(self, taker_amount):
        """Sets the taker_amount of this IExtendedOrderFill.

        Taker amount in base units to fill from this order  # noqa: E501

        :param taker_amount: The taker_amount of this IExtendedOrderFill.  # noqa: E501
        :type: str
        """
        if taker_amount is None:
            raise ValueError("Invalid value for `taker_amount`, must not be `None`")  # noqa: E501

        self._taker_amount = taker_amount

    @property
    def order(self):
        """Gets the order of this IExtendedOrderFill.  # noqa: E501


        :return: The order of this IExtendedOrderFill.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this IExtendedOrderFill.


        :param order: The order of this IExtendedOrderFill.  # noqa: E501
        :type: Order
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

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
        if not isinstance(other, IExtendedOrderFill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
