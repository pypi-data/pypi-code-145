# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventInferResponse(object):
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
        'inferred_columns': 'list[ColumnDef]',
        'recommeneded_columns': 'list[ColumnDef]'
    }

    attribute_map = {
        'inferred_columns': 'inferred_columns',
        'recommeneded_columns': 'recommeneded_columns'
    }

    def __init__(self, inferred_columns=None, recommeneded_columns=None):  # noqa: E501
        """EventInferResponse - a model defined in Swagger"""  # noqa: E501
        self._inferred_columns = None
        self._recommeneded_columns = None
        self.discriminator = None
        if inferred_columns is not None:
            self.inferred_columns = inferred_columns
        if recommeneded_columns is not None:
            self.recommeneded_columns = recommeneded_columns

    @property
    def inferred_columns(self):
        """Gets the inferred_columns of this EventInferResponse.  # noqa: E501


        :return: The inferred_columns of this EventInferResponse.  # noqa: E501
        :rtype: list[ColumnDef]
        """
        return self._inferred_columns

    @inferred_columns.setter
    def inferred_columns(self, inferred_columns):
        """Sets the inferred_columns of this EventInferResponse.


        :param inferred_columns: The inferred_columns of this EventInferResponse.  # noqa: E501
        :type: list[ColumnDef]
        """

        self._inferred_columns = inferred_columns

    @property
    def recommeneded_columns(self):
        """Gets the recommeneded_columns of this EventInferResponse.  # noqa: E501


        :return: The recommeneded_columns of this EventInferResponse.  # noqa: E501
        :rtype: list[ColumnDef]
        """
        return self._recommeneded_columns

    @recommeneded_columns.setter
    def recommeneded_columns(self, recommeneded_columns):
        """Sets the recommeneded_columns of this EventInferResponse.


        :param recommeneded_columns: The recommeneded_columns of this EventInferResponse.  # noqa: E501
        :type: list[ColumnDef]
        """

        self._recommeneded_columns = recommeneded_columns

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
        if issubclass(EventInferResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventInferResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
