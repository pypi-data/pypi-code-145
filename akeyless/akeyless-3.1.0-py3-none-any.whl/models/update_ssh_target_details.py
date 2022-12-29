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


class UpdateSSHTargetDetails(object):
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
        'host': 'str',
        'json': 'bool',
        'keep_prev_version': 'str',
        'name': 'str',
        'new_version': 'bool',
        'port': 'str',
        'private_key': 'str',
        'private_key_password': 'str',
        'protection_key': 'str',
        'ssh_password': 'str',
        'ssh_username': 'str',
        'token': 'str',
        'uid_token': 'str'
    }

    attribute_map = {
        'host': 'host',
        'json': 'json',
        'keep_prev_version': 'keep-prev-version',
        'name': 'name',
        'new_version': 'new-version',
        'port': 'port',
        'private_key': 'private-key',
        'private_key_password': 'private-key-password',
        'protection_key': 'protection_key',
        'ssh_password': 'ssh-password',
        'ssh_username': 'ssh-username',
        'token': 'token',
        'uid_token': 'uid-token'
    }

    def __init__(self, host=None, json=None, keep_prev_version=None, name=None, new_version=None, port=None, private_key=None, private_key_password=None, protection_key=None, ssh_password=None, ssh_username=None, token=None, uid_token=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSSHTargetDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._json = None
        self._keep_prev_version = None
        self._name = None
        self._new_version = None
        self._port = None
        self._private_key = None
        self._private_key_password = None
        self._protection_key = None
        self._ssh_password = None
        self._ssh_username = None
        self._token = None
        self._uid_token = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if json is not None:
            self.json = json
        if keep_prev_version is not None:
            self.keep_prev_version = keep_prev_version
        self.name = name
        if new_version is not None:
            self.new_version = new_version
        if port is not None:
            self.port = port
        if private_key is not None:
            self.private_key = private_key
        if private_key_password is not None:
            self.private_key_password = private_key_password
        if protection_key is not None:
            self.protection_key = protection_key
        if ssh_password is not None:
            self.ssh_password = ssh_password
        if ssh_username is not None:
            self.ssh_username = ssh_username
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token

    @property
    def host(self):
        """Gets the host of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The host of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UpdateSSHTargetDetails.


        :param host: The host of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def json(self):
        """Gets the json of this UpdateSSHTargetDetails.  # noqa: E501

        Set output format to JSON  # noqa: E501

        :return: The json of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this UpdateSSHTargetDetails.

        Set output format to JSON  # noqa: E501

        :param json: The json of this UpdateSSHTargetDetails.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def keep_prev_version(self):
        """Gets the keep_prev_version of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The keep_prev_version of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._keep_prev_version

    @keep_prev_version.setter
    def keep_prev_version(self, keep_prev_version):
        """Sets the keep_prev_version of this UpdateSSHTargetDetails.


        :param keep_prev_version: The keep_prev_version of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._keep_prev_version = keep_prev_version

    @property
    def name(self):
        """Gets the name of this UpdateSSHTargetDetails.  # noqa: E501

        Target name  # noqa: E501

        :return: The name of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSSHTargetDetails.

        Target name  # noqa: E501

        :param name: The name of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_version(self):
        """Gets the new_version of this UpdateSSHTargetDetails.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The new_version of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: bool
        """
        return self._new_version

    @new_version.setter
    def new_version(self, new_version):
        """Sets the new_version of this UpdateSSHTargetDetails.

        Deprecated  # noqa: E501

        :param new_version: The new_version of this UpdateSSHTargetDetails.  # noqa: E501
        :type: bool
        """

        self._new_version = new_version

    @property
    def port(self):
        """Gets the port of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The port of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateSSHTargetDetails.


        :param port: The port of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def private_key(self):
        """Gets the private_key of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The private_key of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this UpdateSSHTargetDetails.


        :param private_key: The private_key of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def private_key_password(self):
        """Gets the private_key_password of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The private_key_password of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._private_key_password

    @private_key_password.setter
    def private_key_password(self, private_key_password):
        """Sets the private_key_password of this UpdateSSHTargetDetails.


        :param private_key_password: The private_key_password of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._private_key_password = private_key_password

    @property
    def protection_key(self):
        """Gets the protection_key of this UpdateSSHTargetDetails.  # noqa: E501

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :return: The protection_key of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._protection_key

    @protection_key.setter
    def protection_key(self, protection_key):
        """Sets the protection_key of this UpdateSSHTargetDetails.

        The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)  # noqa: E501

        :param protection_key: The protection_key of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._protection_key = protection_key

    @property
    def ssh_password(self):
        """Gets the ssh_password of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The ssh_password of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        """Sets the ssh_password of this UpdateSSHTargetDetails.


        :param ssh_password: The ssh_password of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._ssh_password = ssh_password

    @property
    def ssh_username(self):
        """Gets the ssh_username of this UpdateSSHTargetDetails.  # noqa: E501


        :return: The ssh_username of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._ssh_username

    @ssh_username.setter
    def ssh_username(self, ssh_username):
        """Sets the ssh_username of this UpdateSSHTargetDetails.


        :param ssh_username: The ssh_username of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._ssh_username = ssh_username

    @property
    def token(self):
        """Gets the token of this UpdateSSHTargetDetails.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateSSHTargetDetails.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateSSHTargetDetails.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateSSHTargetDetails.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateSSHTargetDetails.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateSSHTargetDetails.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateSSHTargetDetails.  # noqa: E501
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
        if not isinstance(other, UpdateSSHTargetDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSSHTargetDetails):
            return True

        return self.to_dict() != other.to_dict()
