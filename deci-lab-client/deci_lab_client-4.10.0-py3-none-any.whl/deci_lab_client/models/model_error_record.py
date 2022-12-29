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


class ModelErrorRecord(object):
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
        'error_type': 'str',
        'level': 'ErrorLevel',
        'params': 'object',
        'message': 'str'
    }

    attribute_map = {
        'error_type': 'errorType',
        'level': 'level',
        'params': 'params',
        'message': 'message'
    }

    def __init__(self, error_type=None, level=None, params=None, message='', local_vars_configuration=None):  # noqa: E501
        """ModelErrorRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_type = None
        self._level = None
        self._params = None
        self._message = None
        self.discriminator = None

        self.error_type = error_type
        if level is not None:
            self.level = level
        self.params = params
        if message is not None:
            self.message = message

    @property
    def error_type(self):
        """Gets the error_type of this ModelErrorRecord.  # noqa: E501


        :return: The error_type of this ModelErrorRecord.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this ModelErrorRecord.


        :param error_type: The error_type of this ModelErrorRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error_type is None:  # noqa: E501
            raise ValueError("Invalid value for `error_type`, must not be `None`")  # noqa: E501

        self._error_type = error_type

    @property
    def level(self):
        """Gets the level of this ModelErrorRecord.  # noqa: E501


        :return: The level of this ModelErrorRecord.  # noqa: E501
        :rtype: ErrorLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ModelErrorRecord.


        :param level: The level of this ModelErrorRecord.  # noqa: E501
        :type: ErrorLevel
        """

        self._level = level

    @property
    def params(self):
        """Gets the params of this ModelErrorRecord.  # noqa: E501


        :return: The params of this ModelErrorRecord.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ModelErrorRecord.


        :param params: The params of this ModelErrorRecord.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and params is None:  # noqa: E501
            raise ValueError("Invalid value for `params`, must not be `None`")  # noqa: E501

        self._params = params

    @property
    def message(self):
        """Gets the message of this ModelErrorRecord.  # noqa: E501


        :return: The message of this ModelErrorRecord.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ModelErrorRecord.


        :param message: The message of this ModelErrorRecord.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ModelErrorRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelErrorRecord):
            return True

        return self.to_dict() != other.to_dict()
