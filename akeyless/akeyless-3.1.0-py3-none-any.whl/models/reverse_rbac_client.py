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


class ReverseRBACClient(object):
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
        'assocs': 'list[AuthMethodRoleAssociation]',
        'auth_method_name': 'str'
    }

    attribute_map = {
        'assocs': 'assocs',
        'auth_method_name': 'auth_method_name'
    }

    def __init__(self, assocs=None, auth_method_name=None, local_vars_configuration=None):  # noqa: E501
        """ReverseRBACClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assocs = None
        self._auth_method_name = None
        self.discriminator = None

        if assocs is not None:
            self.assocs = assocs
        if auth_method_name is not None:
            self.auth_method_name = auth_method_name

    @property
    def assocs(self):
        """Gets the assocs of this ReverseRBACClient.  # noqa: E501


        :return: The assocs of this ReverseRBACClient.  # noqa: E501
        :rtype: list[AuthMethodRoleAssociation]
        """
        return self._assocs

    @assocs.setter
    def assocs(self, assocs):
        """Sets the assocs of this ReverseRBACClient.


        :param assocs: The assocs of this ReverseRBACClient.  # noqa: E501
        :type: list[AuthMethodRoleAssociation]
        """

        self._assocs = assocs

    @property
    def auth_method_name(self):
        """Gets the auth_method_name of this ReverseRBACClient.  # noqa: E501


        :return: The auth_method_name of this ReverseRBACClient.  # noqa: E501
        :rtype: str
        """
        return self._auth_method_name

    @auth_method_name.setter
    def auth_method_name(self, auth_method_name):
        """Sets the auth_method_name of this ReverseRBACClient.


        :param auth_method_name: The auth_method_name of this ReverseRBACClient.  # noqa: E501
        :type: str
        """

        self._auth_method_name = auth_method_name

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
        if not isinstance(other, ReverseRBACClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReverseRBACClient):
            return True

        return self.to_dict() != other.to_dict()
