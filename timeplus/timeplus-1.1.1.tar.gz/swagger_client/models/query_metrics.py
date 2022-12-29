# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class QueryMetrics(object):
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
        'count': 'int',
        'latency': 'Latency',
        'throughput': 'Throughput'
    }

    attribute_map = {
        'count': 'count',
        'latency': 'latency',
        'throughput': 'throughput'
    }

    def __init__(self, count=None, latency=None, throughput=None):  # noqa: E501
        """QueryMetrics - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._latency = None
        self._throughput = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if latency is not None:
            self.latency = latency
        if throughput is not None:
            self.throughput = throughput

    @property
    def count(self):
        """Gets the count of this QueryMetrics.  # noqa: E501


        :return: The count of this QueryMetrics.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this QueryMetrics.


        :param count: The count of this QueryMetrics.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def latency(self):
        """Gets the latency of this QueryMetrics.  # noqa: E501


        :return: The latency of this QueryMetrics.  # noqa: E501
        :rtype: Latency
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this QueryMetrics.


        :param latency: The latency of this QueryMetrics.  # noqa: E501
        :type: Latency
        """

        self._latency = latency

    @property
    def throughput(self):
        """Gets the throughput of this QueryMetrics.  # noqa: E501


        :return: The throughput of this QueryMetrics.  # noqa: E501
        :rtype: Throughput
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this QueryMetrics.


        :param throughput: The throughput of this QueryMetrics.  # noqa: E501
        :type: Throughput
        """

        self._throughput = throughput

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
        if issubclass(QueryMetrics, dict):
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
        if not isinstance(other, QueryMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
