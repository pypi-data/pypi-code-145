# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class GatewayMigratePersonalItems(object):
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
        '_1password_email': 'str',
        '_1password_password': 'str',
        '_1password_secret_key': 'str',
        '_1password_url': 'str',
        '_1password_vaults': 'list[str]',
        'json': 'bool',
        'protection_key': 'str',
        'target_location': 'str',
        'token': 'str',
        'type': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        '_1password_email': '1password-email',
        '_1password_password': '1password-password',
        '_1password_secret_key': '1password-secret-key',
        '_1password_url': '1password-url',
        '_1password_vaults': '1password-vaults',
        'json': 'json',
        'protection_key': 'protection-key',
        'target_location': 'target-location',
        'token': 'token',
        'type': 'type',
        'uid_token': 'uid-token'
    }

    def __init__(self, _1password_email=None, _1password_password=None, _1password_secret_key=None, _1password_url=None, _1password_vaults=None, json=None, protection_key=None, target_location=None, token=None, type='1password', uid_token=None, local_vars_configuration=None):  # noqa: E501
        """GatewayMigratePersonalItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__1password_email = None
        self.__1password_password = None
        self.__1password_secret_key = None
        self.__1password_url = None
        self.__1password_vaults = None
        self._json = None
        self._protection_key = None
        self._target_location = None
        self._token = None
        self._type = None
        self._uid_token = None
        self.discriminator = None

        if _1password_email is not None:
            self._1password_email = _1password_email
        if _1password_password is not None:
            self._1password_password = _1password_password
        if _1password_secret_key is not None:
            self._1password_secret_key = _1password_secret_key
        if _1password_url is not None:
            self._1password_url = _1password_url
        if _1password_vaults is not None:
            self._1password_vaults = _1password_vaults
        if json is not None:
            self.json = json
        if protection_key is not None:
            self.protection_key = protection_key
        if target_location is not None:
            self.target_location = target_location
        if token is not None:
            self.token = token
        if type is not None:
            self.type = type
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def _1password_email(self):
        """Gets the _1password_email of this GatewayMigratePersonalItems.  # noqa: E501

        1Password user email to connect to the API  # noqa: E501

        :return: The _1password_email of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self.__1password_email

    @_1password_email.setter
    def _1password_email(self, _1password_email):
        """Sets the _1password_email of this GatewayMigratePersonalItems.

        1Password user email to connect to the API  # noqa: E501

        :param _1password_email: The _1password_email of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self.__1password_email = _1password_email

    @property
    def _1password_password(self):
        """Gets the _1password_password of this GatewayMigratePersonalItems.  # noqa: E501

        1Password user password to connect to the API  # noqa: E501

        :return: The _1password_password of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self.__1password_password

    @_1password_password.setter
    def _1password_password(self, _1password_password):
        """Sets the _1password_password of this GatewayMigratePersonalItems.

        1Password user password to connect to the API  # noqa: E501

        :param _1password_password: The _1password_password of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self.__1password_password = _1password_password

    @property
    def _1password_secret_key(self):
        """Gets the _1password_secret_key of this GatewayMigratePersonalItems.  # noqa: E501

        1Password user secret key to connect to the API  # noqa: E501

        :return: The _1password_secret_key of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self.__1password_secret_key

    @_1password_secret_key.setter
    def _1password_secret_key(self, _1password_secret_key):
        """Sets the _1password_secret_key of this GatewayMigratePersonalItems.

        1Password user secret key to connect to the API  # noqa: E501

        :param _1password_secret_key: The _1password_secret_key of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self.__1password_secret_key = _1password_secret_key

    @property
    def _1password_url(self):
        """Gets the _1password_url of this GatewayMigratePersonalItems.  # noqa: E501

        1Password api container url  # noqa: E501

        :return: The _1password_url of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self.__1password_url

    @_1password_url.setter
    def _1password_url(self, _1password_url):
        """Sets the _1password_url of this GatewayMigratePersonalItems.

        1Password api container url  # noqa: E501

        :param _1password_url: The _1password_url of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self.__1password_url = _1password_url

    @property
    def _1password_vaults(self):
        """Gets the _1password_vaults of this GatewayMigratePersonalItems.  # noqa: E501

        1Password list of vault to get the items from  # noqa: E501

        :return: The _1password_vaults of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: list[str]
        """
        return self.__1password_vaults

    @_1password_vaults.setter
    def _1password_vaults(self, _1password_vaults):
        """Sets the _1password_vaults of this GatewayMigratePersonalItems.

        1Password list of vault to get the items from  # noqa: E501

        :param _1password_vaults: The _1password_vaults of this GatewayMigratePersonalItems.  # noqa: E501
        :type: list[str]
        """

        self.__1password_vaults = _1password_vaults

    @property
    def json(self):
        """Gets the json of this GatewayMigratePersonalItems.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this GatewayMigratePersonalItems.

        Set output format to JSON  # noqa: E501

        :param json: The json of this GatewayMigratePersonalItems.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def protection_key(self):
        """Gets the protection_key of this GatewayMigratePersonalItems.  # noqa: E501

        The name of a key that used to encrypt the secret value  # noqa: E501

        :return: The protection_key of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this GatewayMigratePersonalItems.

        The name of a key that used to encrypt the secret value  # noqa: E501

        :param protection_key: The protection_key of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def target_location(self):
        """Gets the target_location of this GatewayMigratePersonalItems.  # noqa: E501

        Target location in your Akeyless personal folder for migrated secrets  # noqa: E501

        :return: The target_location of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self._target_location

    @target_location.setter
    def target_location(self, target_location):
        """Sets the target_location of this GatewayMigratePersonalItems.

        Target location in your Akeyless personal folder for migrated secrets  # noqa: E501

        :param target_location: The target_location of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self._target_location = target_location

    @property
    def token(self):
        """Gets the token of this GatewayMigratePersonalItems.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this GatewayMigratePersonalItems.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def type(self):
        """Gets the type of this GatewayMigratePersonalItems.  # noqa: E501

        Migration type for now only 1password.  # noqa: E501

        :return: The type of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GatewayMigratePersonalItems.

        Migration type for now only 1password.  # noqa: E501

        :param type: The type of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid_token(self):
        """Gets the uid_token of this GatewayMigratePersonalItems.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this GatewayMigratePersonalItems.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this GatewayMigratePersonalItems.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this GatewayMigratePersonalItems.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

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
        if not isinstance(other, GatewayMigratePersonalItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayMigratePersonalItems):
            return True

        return self.to_dict() != other.to_dict()
