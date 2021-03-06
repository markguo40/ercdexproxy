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


class Account(object):
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
        'name': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'address': 'str',
        'account_type': 'str',
        'phone_number': 'str',
        'referrer_account_id': 'float',
        'referral_wallet_id': 'float',
        'is_confirmed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'name': 'name',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'address': 'address',
        'account_type': 'accountType',
        'phone_number': 'phoneNumber',
        'referrer_account_id': 'referrerAccountId',
        'referral_wallet_id': 'referralWalletId',
        'is_confirmed': 'isConfirmed'
    }

    def __init__(self, id=None, date_created=None, date_updated=None, name=None, city=None, state=None, country=None, address=None, account_type=None, phone_number=None, referrer_account_id=None, referral_wallet_id=None, is_confirmed=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._date_updated = None
        self._name = None
        self._city = None
        self._state = None
        self._country = None
        self._address = None
        self._account_type = None
        self._phone_number = None
        self._referrer_account_id = None
        self._referral_wallet_id = None
        self._is_confirmed = None
        self.discriminator = None

        self.id = id
        self.date_created = date_created
        self.date_updated = date_updated
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        self.address = address
        if account_type is not None:
            self.account_type = account_type
        if phone_number is not None:
            self.phone_number = phone_number
        if referrer_account_id is not None:
            self.referrer_account_id = referrer_account_id
        if referral_wallet_id is not None:
            self.referral_wallet_id = referral_wallet_id
        self.is_confirmed = is_confirmed

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this Account.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        Unique Identifier  # noqa: E501

        :param id: The id of this Account.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this Account.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The date_created of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Account.

        Date of creation  # noqa: E501

        :param date_created: The date_created of this Account.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this Account.  # noqa: E501

        Date of updated  # noqa: E501

        :return: The date_updated of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this Account.

        Date of updated  # noqa: E501

        :param date_updated: The date_updated of this Account.  # noqa: E501
        :type: datetime
        """
        if date_updated is None:
            raise ValueError("Invalid value for `date_updated`, must not be `None`")  # noqa: E501

        self._date_updated = date_updated

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501


        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.


        :param name: The name of this Account.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def city(self):
        """Gets the city of this Account.  # noqa: E501


        :return: The city of this Account.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Account.


        :param city: The city of this Account.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self):
        """Gets the state of this Account.  # noqa: E501


        :return: The state of this Account.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Account.


        :param state: The state of this Account.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def country(self):
        """Gets the country of this Account.  # noqa: E501


        :return: The country of this Account.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Account.


        :param country: The country of this Account.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def address(self):
        """Gets the address of this Account.  # noqa: E501


        :return: The address of this Account.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Account.


        :param address: The address of this Account.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def account_type(self):
        """Gets the account_type of this Account.  # noqa: E501


        :return: The account_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this Account.


        :param account_type: The account_type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["relayer", "market-maker", "developer", "trader", "other"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def phone_number(self):
        """Gets the phone_number of this Account.  # noqa: E501


        :return: The phone_number of this Account.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Account.


        :param phone_number: The phone_number of this Account.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def referrer_account_id(self):
        """Gets the referrer_account_id of this Account.  # noqa: E501


        :return: The referrer_account_id of this Account.  # noqa: E501
        :rtype: float
        """
        return self._referrer_account_id

    @referrer_account_id.setter
    def referrer_account_id(self, referrer_account_id):
        """Sets the referrer_account_id of this Account.


        :param referrer_account_id: The referrer_account_id of this Account.  # noqa: E501
        :type: float
        """

        self._referrer_account_id = referrer_account_id

    @property
    def referral_wallet_id(self):
        """Gets the referral_wallet_id of this Account.  # noqa: E501


        :return: The referral_wallet_id of this Account.  # noqa: E501
        :rtype: float
        """
        return self._referral_wallet_id

    @referral_wallet_id.setter
    def referral_wallet_id(self, referral_wallet_id):
        """Sets the referral_wallet_id of this Account.


        :param referral_wallet_id: The referral_wallet_id of this Account.  # noqa: E501
        :type: float
        """

        self._referral_wallet_id = referral_wallet_id

    @property
    def is_confirmed(self):
        """Gets the is_confirmed of this Account.  # noqa: E501


        :return: The is_confirmed of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._is_confirmed

    @is_confirmed.setter
    def is_confirmed(self, is_confirmed):
        """Sets the is_confirmed of this Account.


        :param is_confirmed: The is_confirmed of this Account.  # noqa: E501
        :type: bool
        """
        if is_confirmed is None:
            raise ValueError("Invalid value for `is_confirmed`, must not be `None`")  # noqa: E501

        self._is_confirmed = is_confirmed

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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
