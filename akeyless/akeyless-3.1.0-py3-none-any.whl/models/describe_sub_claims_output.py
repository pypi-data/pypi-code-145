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


class DescribeSubClaimsOutput(object):
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
        'sub_claims': 'dict(str, list[str])'
    }

    attribute_map = {
        'sub_claims': 'sub_claims'
    }

    def __init__(self, sub_claims=None, local_vars_configuration=None):  # noqa: E501
        """DescribeSubClaimsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sub_claims = None
        self.discriminator = None

        if sub_claims is not None:
            self.sub_claims = sub_claims

    @property
    def sub_claims(self):
        """Gets the sub_claims of this DescribeSubClaimsOutput.  # noqa: E501


        :return: The sub_claims of this DescribeSubClaimsOutput.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._sub_claims

    @sub_claims.setter
    def sub_claims(self, sub_claims):
        """Sets the sub_claims of this DescribeSubClaimsOutput.


        :param sub_claims: The sub_claims of this DescribeSubClaimsOutput.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._sub_claims = sub_claims

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
        if not isinstance(other, DescribeSubClaimsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSubClaimsOutput):
            return True

        return self.to_dict() != other.to_dict()
