# coding: utf-8

"""
    StockX API

    PRERELEASE API - Subject to change before release. Provides access to StockX's public services, allowing end users to query for product and order information.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProductInfoMeta(object):
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
        'charity': 'bool',
        'raffle': 'bool',
        'mobile_only': 'bool',
        'restock': 'bool',
        'deleted': 'bool',
        'hidden': 'bool',
        'lock_buying': 'bool',
        'lock_selling': 'bool',
        'redirected': 'bool'
    }

    attribute_map = {
        'charity': 'charity',
        'raffle': 'raffle',
        'mobile_only': 'mobile_only',
        'restock': 'restock',
        'deleted': 'deleted',
        'hidden': 'hidden',
        'lock_buying': 'lock_buying',
        'lock_selling': 'lock_selling',
        'redirected': 'redirected'
    }

    def __init__(self, charity=None, raffle=None, mobile_only=None, restock=None, deleted=None, hidden=None, lock_buying=None, lock_selling=None, redirected=None):  # noqa: E501
        """ProductInfoMeta - a model defined in Swagger"""  # noqa: E501

        self._charity = None
        self._raffle = None
        self._mobile_only = None
        self._restock = None
        self._deleted = None
        self._hidden = None
        self._lock_buying = None
        self._lock_selling = None
        self._redirected = None
        self.discriminator = None

        if charity is not None:
            self.charity = charity
        if raffle is not None:
            self.raffle = raffle
        if mobile_only is not None:
            self.mobile_only = mobile_only
        if restock is not None:
            self.restock = restock
        if deleted is not None:
            self.deleted = deleted
        if hidden is not None:
            self.hidden = hidden
        if lock_buying is not None:
            self.lock_buying = lock_buying
        if lock_selling is not None:
            self.lock_selling = lock_selling
        if redirected is not None:
            self.redirected = redirected

    @property
    def charity(self):
        """Gets the charity of this ProductInfoMeta.  # noqa: E501


        :return: The charity of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._charity

    @charity.setter
    def charity(self, charity):
        """Sets the charity of this ProductInfoMeta.


        :param charity: The charity of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._charity = charity

    @property
    def raffle(self):
        """Gets the raffle of this ProductInfoMeta.  # noqa: E501


        :return: The raffle of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._raffle

    @raffle.setter
    def raffle(self, raffle):
        """Sets the raffle of this ProductInfoMeta.


        :param raffle: The raffle of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._raffle = raffle

    @property
    def mobile_only(self):
        """Gets the mobile_only of this ProductInfoMeta.  # noqa: E501


        :return: The mobile_only of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._mobile_only

    @mobile_only.setter
    def mobile_only(self, mobile_only):
        """Sets the mobile_only of this ProductInfoMeta.


        :param mobile_only: The mobile_only of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._mobile_only = mobile_only

    @property
    def restock(self):
        """Gets the restock of this ProductInfoMeta.  # noqa: E501


        :return: The restock of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._restock

    @restock.setter
    def restock(self, restock):
        """Sets the restock of this ProductInfoMeta.


        :param restock: The restock of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._restock = restock

    @property
    def deleted(self):
        """Gets the deleted of this ProductInfoMeta.  # noqa: E501


        :return: The deleted of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ProductInfoMeta.


        :param deleted: The deleted of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def hidden(self):
        """Gets the hidden of this ProductInfoMeta.  # noqa: E501


        :return: The hidden of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ProductInfoMeta.


        :param hidden: The hidden of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def lock_buying(self):
        """Gets the lock_buying of this ProductInfoMeta.  # noqa: E501


        :return: The lock_buying of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._lock_buying

    @lock_buying.setter
    def lock_buying(self, lock_buying):
        """Sets the lock_buying of this ProductInfoMeta.


        :param lock_buying: The lock_buying of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._lock_buying = lock_buying

    @property
    def lock_selling(self):
        """Gets the lock_selling of this ProductInfoMeta.  # noqa: E501


        :return: The lock_selling of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._lock_selling

    @lock_selling.setter
    def lock_selling(self, lock_selling):
        """Sets the lock_selling of this ProductInfoMeta.


        :param lock_selling: The lock_selling of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._lock_selling = lock_selling

    @property
    def redirected(self):
        """Gets the redirected of this ProductInfoMeta.  # noqa: E501


        :return: The redirected of this ProductInfoMeta.  # noqa: E501
        :rtype: bool
        """
        return self._redirected

    @redirected.setter
    def redirected(self, redirected):
        """Sets the redirected of this ProductInfoMeta.


        :param redirected: The redirected of this ProductInfoMeta.  # noqa: E501
        :type: bool
        """

        self._redirected = redirected

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
        if not isinstance(other, ProductInfoMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
