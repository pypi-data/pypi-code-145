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


class ManagedKeyDetailsInfo(object):
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
        'is_provided_by_user': 'bool',
        'is_unexportable': 'bool',
        'key_state': 'str',
        'key_type': 'str',
        'managed_key_id': 'str',
        'target_alias_helper': 'str',
        'targets': 'list[ManagedKeyTargetInfo]'
    }

    attribute_map = {
        'is_provided_by_user': 'is_provided_by_user',
        'is_unexportable': 'is_unexportable',
        'key_state': 'key_state',
        'key_type': 'key_type',
        'managed_key_id': 'managed_key_id',
        'target_alias_helper': 'target_alias_helper',
        'targets': 'targets'
    }

    def __init__(self, is_provided_by_user=None, is_unexportable=None, key_state=None, key_type=None, managed_key_id=None, target_alias_helper=None, targets=None, local_vars_configuration=None):  # noqa: E501
        """ManagedKeyDetailsInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_provided_by_user = None
        self._is_unexportable = None
        self._key_state = None
        self._key_type = None
        self._managed_key_id = None
        self._target_alias_helper = None
        self._targets = None
        self.discriminator = None

        if is_provided_by_user is not None:
            self.is_provided_by_user = is_provided_by_user
        if is_unexportable is not None:
            self.is_unexportable = is_unexportable
        if key_state is not None:
            self.key_state = key_state
        if key_type is not None:
            self.key_type = key_type
        if managed_key_id is not None:
            self.managed_key_id = managed_key_id
        if target_alias_helper is not None:
            self.target_alias_helper = target_alias_helper
        if targets is not None:
            self.targets = targets

    @property
    def is_provided_by_user(self):
        """Gets the is_provided_by_user of this ManagedKeyDetailsInfo.  # noqa: E501


        :return: The is_provided_by_user of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_provided_by_user

    @is_provided_by_user.setter
    def is_provided_by_user(self, is_provided_by_user):
        """Sets the is_provided_by_user of this ManagedKeyDetailsInfo.


        :param is_provided_by_user: The is_provided_by_user of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._is_provided_by_user = is_provided_by_user

    @property
    def is_unexportable(self):
        """Gets the is_unexportable of this ManagedKeyDetailsInfo.  # noqa: E501


        :return: The is_unexportable of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_unexportable

    @is_unexportable.setter
    def is_unexportable(self, is_unexportable):
        """Sets the is_unexportable of this ManagedKeyDetailsInfo.


        :param is_unexportable: The is_unexportable of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: bool
        """

        self._is_unexportable = is_unexportable

    @property
    def key_state(self):
        """Gets the key_state of this ManagedKeyDetailsInfo.  # noqa: E501

        ItemState defines the different states an Item can be in  # noqa: E501

        :return: The key_state of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """Sets the key_state of this ManagedKeyDetailsInfo.

        ItemState defines the different states an Item can be in  # noqa: E501

        :param key_state: The key_state of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._key_state = key_state

    @property
    def key_type(self):
        """Gets the key_type of this ManagedKeyDetailsInfo.  # noqa: E501


        :return: The key_type of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this ManagedKeyDetailsInfo.


        :param key_type: The key_type of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def managed_key_id(self):
        """Gets the managed_key_id of this ManagedKeyDetailsInfo.  # noqa: E501


        :return: The managed_key_id of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._managed_key_id

    @managed_key_id.setter
    def managed_key_id(self, managed_key_id):
        """Sets the managed_key_id of this ManagedKeyDetailsInfo.


        :param managed_key_id: The managed_key_id of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._managed_key_id = managed_key_id

    @property
    def target_alias_helper(self):
        """Gets the target_alias_helper of this ManagedKeyDetailsInfo.  # noqa: E501


        :return: The target_alias_helper of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._target_alias_helper

    @target_alias_helper.setter
    def target_alias_helper(self, target_alias_helper):
        """Sets the target_alias_helper of this ManagedKeyDetailsInfo.


        :param target_alias_helper: The target_alias_helper of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: str
        """

        self._target_alias_helper = target_alias_helper

    @property
    def targets(self):
        """Gets the targets of this ManagedKeyDetailsInfo.  # noqa: E501


        :return: The targets of this ManagedKeyDetailsInfo.  # noqa: E501
        :rtype: list[ManagedKeyTargetInfo]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this ManagedKeyDetailsInfo.


        :param targets: The targets of this ManagedKeyDetailsInfo.  # noqa: E501
        :type: list[ManagedKeyTargetInfo]
        """

        self._targets = targets

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
        if not isinstance(other, ManagedKeyDetailsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManagedKeyDetailsInfo):
            return True

        return self.to_dict() != other.to_dict()
