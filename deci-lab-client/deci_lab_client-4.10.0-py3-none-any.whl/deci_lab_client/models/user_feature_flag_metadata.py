# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deci_lab_client.configuration import Configuration


class UserFeatureFlagMetadata(object):
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
        'feature_id': 'str',
        'is_on': 'bool'
    }

    attribute_map = {
        'feature_id': 'featureId',
        'is_on': 'isOn'
    }

    def __init__(self, feature_id=None, is_on=None, local_vars_configuration=None):  # noqa: E501
        """UserFeatureFlagMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feature_id = None
        self._is_on = None
        self.discriminator = None

        self.feature_id = feature_id
        self.is_on = is_on

    @property
    def feature_id(self):
        """Gets the feature_id of this UserFeatureFlagMetadata.  # noqa: E501


        :return: The feature_id of this UserFeatureFlagMetadata.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this UserFeatureFlagMetadata.


        :param feature_id: The feature_id of this UserFeatureFlagMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and feature_id is None:  # noqa: E501
            raise ValueError("Invalid value for `feature_id`, must not be `None`")  # noqa: E501

        self._feature_id = feature_id

    @property
    def is_on(self):
        """Gets the is_on of this UserFeatureFlagMetadata.  # noqa: E501


        :return: The is_on of this UserFeatureFlagMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_on

    @is_on.setter
    def is_on(self, is_on):
        """Sets the is_on of this UserFeatureFlagMetadata.


        :param is_on: The is_on of this UserFeatureFlagMetadata.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_on is None:  # noqa: E501
            raise ValueError("Invalid value for `is_on`, must not be `None`")  # noqa: E501

        self._is_on = is_on

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
        if not isinstance(other, UserFeatureFlagMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserFeatureFlagMetadata):
            return True

        return self.to_dict() != other.to_dict()
