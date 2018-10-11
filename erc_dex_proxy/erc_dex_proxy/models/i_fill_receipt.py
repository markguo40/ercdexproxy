# coding: utf-8

"""
    ERC dEX Proxy Service

    Command line app for ERC dEX Trading Automation  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from erc_dex_proxy.models.i_fill_receipt_log import IFillReceiptLog  # noqa: F401,E501


class IFillReceipt(object):
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
        'id': 'float',
        'date_created': 'datetime',
        'date_updated': 'datetime',
        'tx_hash': 'str',
        'taker': 'str',
        'status': 'str',
        'side': 'str',
        'taker_amount': 'str',
        'maker_amount': 'str',
        'price': 'str',
        'base_asset_address': 'str',
        'base_symbol': 'str',
        'quote_symbol': 'str',
        'quote_asset_address': 'str',
        'fee_amount': 'str',
        'fee_asset_address': 'str',
        'logs': 'list[IFillReceiptLog]'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'tx_hash': 'txHash',
        'taker': 'taker',
        'status': 'status',
        'side': 'side',
        'taker_amount': 'takerAmount',
        'maker_amount': 'makerAmount',
        'price': 'price',
        'base_asset_address': 'baseAssetAddress',
        'base_symbol': 'baseSymbol',
        'quote_symbol': 'quoteSymbol',
        'quote_asset_address': 'quoteAssetAddress',
        'fee_amount': 'feeAmount',
        'fee_asset_address': 'feeAssetAddress',
        'logs': 'logs'
    }

    def __init__(self, id=None, date_created=None, date_updated=None, tx_hash=None, taker=None, status=None, side=None, taker_amount=None, maker_amount=None, price=None, base_asset_address=None, base_symbol=None, quote_symbol=None, quote_asset_address=None, fee_amount=None, fee_asset_address=None, logs=None):  # noqa: E501
        """IFillReceipt - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._date_updated = None
        self._tx_hash = None
        self._taker = None
        self._status = None
        self._side = None
        self._taker_amount = None
        self._maker_amount = None
        self._price = None
        self._base_asset_address = None
        self._base_symbol = None
        self._quote_symbol = None
        self._quote_asset_address = None
        self._fee_amount = None
        self._fee_asset_address = None
        self._logs = None
        self.discriminator = None

        self.id = id
        self.date_created = date_created
        self.date_updated = date_updated
        self.tx_hash = tx_hash
        self.taker = taker
        self.status = status
        self.side = side
        self.taker_amount = taker_amount
        self.maker_amount = maker_amount
        self.price = price
        self.base_asset_address = base_asset_address
        self.base_symbol = base_symbol
        self.quote_symbol = quote_symbol
        self.quote_asset_address = quote_asset_address
        self.fee_amount = fee_amount
        self.fee_asset_address = fee_asset_address
        self.logs = logs

    @property
    def id(self):
        """Gets the id of this IFillReceipt.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this IFillReceipt.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IFillReceipt.

        Unique Identifier  # noqa: E501

        :param id: The id of this IFillReceipt.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this IFillReceipt.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The date_created of this IFillReceipt.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this IFillReceipt.

        Date of creation  # noqa: E501

        :param date_created: The date_created of this IFillReceipt.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this IFillReceipt.  # noqa: E501

        Date of updated  # noqa: E501

        :return: The date_updated of this IFillReceipt.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this IFillReceipt.

        Date of updated  # noqa: E501

        :param date_updated: The date_updated of this IFillReceipt.  # noqa: E501
        :type: datetime
        """
        if date_updated is None:
            raise ValueError("Invalid value for `date_updated`, must not be `None`")  # noqa: E501

        self._date_updated = date_updated

    @property
    def tx_hash(self):
        """Gets the tx_hash of this IFillReceipt.  # noqa: E501


        :return: The tx_hash of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, tx_hash):
        """Sets the tx_hash of this IFillReceipt.


        :param tx_hash: The tx_hash of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if tx_hash is None:
            raise ValueError("Invalid value for `tx_hash`, must not be `None`")  # noqa: E501

        self._tx_hash = tx_hash

    @property
    def taker(self):
        """Gets the taker of this IFillReceipt.  # noqa: E501


        :return: The taker of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._taker

    @taker.setter
    def taker(self, taker):
        """Sets the taker of this IFillReceipt.


        :param taker: The taker of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if taker is None:
            raise ValueError("Invalid value for `taker`, must not be `None`")  # noqa: E501

        self._taker = taker

    @property
    def status(self):
        """Gets the status of this IFillReceipt.  # noqa: E501

        Receipt status: success | error | pending  # noqa: E501

        :return: The status of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IFillReceipt.

        Receipt status: success | error | pending  # noqa: E501

        :param status: The status of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def side(self):
        """Gets the side of this IFillReceipt.  # noqa: E501


        :return: The side of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this IFillReceipt.


        :param side: The side of this IFillReceipt.  # noqa: E501
        :type: str
        """
        # if side is None:
        #     raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def taker_amount(self):
        """Gets the taker_amount of this IFillReceipt.  # noqa: E501


        :return: The taker_amount of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._taker_amount

    @taker_amount.setter
    def taker_amount(self, taker_amount):
        """Sets the taker_amount of this IFillReceipt.


        :param taker_amount: The taker_amount of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if taker_amount is None:
            raise ValueError("Invalid value for `taker_amount`, must not be `None`")  # noqa: E501

        self._taker_amount = taker_amount

    @property
    def maker_amount(self):
        """Gets the maker_amount of this IFillReceipt.  # noqa: E501


        :return: The maker_amount of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._maker_amount

    @maker_amount.setter
    def maker_amount(self, maker_amount):
        """Sets the maker_amount of this IFillReceipt.


        :param maker_amount: The maker_amount of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if maker_amount is None:
            raise ValueError("Invalid value for `maker_amount`, must not be `None`")  # noqa: E501

        self._maker_amount = maker_amount

    @property
    def price(self):
        """Gets the price of this IFillReceipt.  # noqa: E501


        :return: The price of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this IFillReceipt.


        :param price: The price of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def base_asset_address(self):
        """Gets the base_asset_address of this IFillReceipt.  # noqa: E501


        :return: The base_asset_address of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._base_asset_address

    @base_asset_address.setter
    def base_asset_address(self, base_asset_address):
        """Sets the base_asset_address of this IFillReceipt.


        :param base_asset_address: The base_asset_address of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if base_asset_address is None:
            raise ValueError("Invalid value for `base_asset_address`, must not be `None`")  # noqa: E501

        self._base_asset_address = base_asset_address

    @property
    def base_symbol(self):
        """Gets the base_symbol of this IFillReceipt.  # noqa: E501


        :return: The base_symbol of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._base_symbol

    @base_symbol.setter
    def base_symbol(self, base_symbol):
        """Sets the base_symbol of this IFillReceipt.


        :param base_symbol: The base_symbol of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if base_symbol is None:
            raise ValueError("Invalid value for `base_symbol`, must not be `None`")  # noqa: E501

        self._base_symbol = base_symbol

    @property
    def quote_symbol(self):
        """Gets the quote_symbol of this IFillReceipt.  # noqa: E501


        :return: The quote_symbol of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._quote_symbol

    @quote_symbol.setter
    def quote_symbol(self, quote_symbol):
        """Sets the quote_symbol of this IFillReceipt.


        :param quote_symbol: The quote_symbol of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if quote_symbol is None:
            raise ValueError("Invalid value for `quote_symbol`, must not be `None`")  # noqa: E501

        self._quote_symbol = quote_symbol

    @property
    def quote_asset_address(self):
        """Gets the quote_asset_address of this IFillReceipt.  # noqa: E501


        :return: The quote_asset_address of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._quote_asset_address

    @quote_asset_address.setter
    def quote_asset_address(self, quote_asset_address):
        """Sets the quote_asset_address of this IFillReceipt.


        :param quote_asset_address: The quote_asset_address of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if quote_asset_address is None:
            raise ValueError("Invalid value for `quote_asset_address`, must not be `None`")  # noqa: E501

        self._quote_asset_address = quote_asset_address

    @property
    def fee_amount(self):
        """Gets the fee_amount of this IFillReceipt.  # noqa: E501


        :return: The fee_amount of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this IFillReceipt.


        :param fee_amount: The fee_amount of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if fee_amount is None:
            raise ValueError("Invalid value for `fee_amount`, must not be `None`")  # noqa: E501

        self._fee_amount = fee_amount

    @property
    def fee_asset_address(self):
        """Gets the fee_asset_address of this IFillReceipt.  # noqa: E501


        :return: The fee_asset_address of this IFillReceipt.  # noqa: E501
        :rtype: str
        """
        return self._fee_asset_address

    @fee_asset_address.setter
    def fee_asset_address(self, fee_asset_address):
        """Sets the fee_asset_address of this IFillReceipt.


        :param fee_asset_address: The fee_asset_address of this IFillReceipt.  # noqa: E501
        :type: str
        """
        if fee_asset_address is None:
            raise ValueError("Invalid value for `fee_asset_address`, must not be `None`")  # noqa: E501

        self._fee_asset_address = fee_asset_address

    @property
    def logs(self):
        """Gets the logs of this IFillReceipt.  # noqa: E501


        :return: The logs of this IFillReceipt.  # noqa: E501
        :rtype: list[IFillReceiptLog]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this IFillReceipt.


        :param logs: The logs of this IFillReceipt.  # noqa: E501
        :type: list[IFillReceiptLog]
        """
        if logs is None:
            raise ValueError("Invalid value for `logs`, must not be `None`")  # noqa: E501

        self._logs = logs

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
        if not isinstance(other, IFillReceipt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
