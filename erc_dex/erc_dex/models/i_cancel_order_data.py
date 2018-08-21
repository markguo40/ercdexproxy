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


class ICancelOrderData(object):
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
        'signature': 'str'
    }

    attribute_map = {
        'order_hash': 'orderHash',
        'signature': 'signature'
    }

    def __init__(self, order_hash=None, signature=None):  # noqa: E501
        """ICancelOrderData - a model defined in Swagger"""  # noqa: E501

        self._order_hash = None
        self._signature = None
        self.discriminator = None

        self.order_hash = order_hash
        self.signature = signature

    @property
    def order_hash(self):
        """Gets the order_hash of this ICancelOrderData.  # noqa: E501

        Computed unique order hash  # noqa: E501

        :return: The order_hash of this ICancelOrderData.  # noqa: E501
        :rtype: str
        """
        return self._order_hash

    @order_hash.setter
    def order_hash(self, order_hash):
        """Sets the order_hash of this ICancelOrderData.

        Computed unique order hash  # noqa: E501

        :param order_hash: The order_hash of this ICancelOrderData.  # noqa: E501
        :type: str
        """
        if order_hash is None:
            raise ValueError("Invalid value for `order_hash`, must not be `None`")  # noqa: E501

        self._order_hash = order_hash

    @property
    def signature(self):
        """Gets the signature of this ICancelOrderData.  # noqa: E501

        Signed message indicating intent to cancel. Sign a hex of a message with format `cancel:ORDER_HASH_GOES_HERE`  # noqa: E501

        :return: The signature of this ICancelOrderData.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ICancelOrderData.

        Signed message indicating intent to cancel. Sign a hex of a message with format `cancel:ORDER_HASH_GOES_HERE`  # noqa: E501

        :param signature: The signature of this ICancelOrderData.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

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
        if not isinstance(other, ICancelOrderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
