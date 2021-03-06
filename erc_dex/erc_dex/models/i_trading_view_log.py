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


class ITradingViewLog(object):
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
        'time': 'float',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'volume': 'float'
    }

    attribute_map = {
        'time': 'time',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close',
        'volume': 'volume'
    }

    def __init__(self, time=None, open=None, high=None, low=None, close=None, volume=None):  # noqa: E501
        """ITradingViewLog - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._open = None
        self._high = None
        self._low = None
        self._close = None
        self._volume = None
        self.discriminator = None

        self.time = time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        if volume is not None:
            self.volume = volume

    @property
    def time(self):
        """Gets the time of this ITradingViewLog.  # noqa: E501


        :return: The time of this ITradingViewLog.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ITradingViewLog.


        :param time: The time of this ITradingViewLog.  # noqa: E501
        :type: float
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def open(self):
        """Gets the open of this ITradingViewLog.  # noqa: E501


        :return: The open of this ITradingViewLog.  # noqa: E501
        :rtype: float
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this ITradingViewLog.


        :param open: The open of this ITradingViewLog.  # noqa: E501
        :type: float
        """
        if open is None:
            raise ValueError("Invalid value for `open`, must not be `None`")  # noqa: E501

        self._open = open

    @property
    def high(self):
        """Gets the high of this ITradingViewLog.  # noqa: E501


        :return: The high of this ITradingViewLog.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this ITradingViewLog.


        :param high: The high of this ITradingViewLog.  # noqa: E501
        :type: float
        """
        if high is None:
            raise ValueError("Invalid value for `high`, must not be `None`")  # noqa: E501

        self._high = high

    @property
    def low(self):
        """Gets the low of this ITradingViewLog.  # noqa: E501


        :return: The low of this ITradingViewLog.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this ITradingViewLog.


        :param low: The low of this ITradingViewLog.  # noqa: E501
        :type: float
        """
        if low is None:
            raise ValueError("Invalid value for `low`, must not be `None`")  # noqa: E501

        self._low = low

    @property
    def close(self):
        """Gets the close of this ITradingViewLog.  # noqa: E501


        :return: The close of this ITradingViewLog.  # noqa: E501
        :rtype: float
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this ITradingViewLog.


        :param close: The close of this ITradingViewLog.  # noqa: E501
        :type: float
        """
        if close is None:
            raise ValueError("Invalid value for `close`, must not be `None`")  # noqa: E501

        self._close = close

    @property
    def volume(self):
        """Gets the volume of this ITradingViewLog.  # noqa: E501


        :return: The volume of this ITradingViewLog.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ITradingViewLog.


        :param volume: The volume of this ITradingViewLog.  # noqa: E501
        :type: float
        """

        self._volume = volume

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
        if not isinstance(other, ITradingViewLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
