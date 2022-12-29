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


class KMIPClient(object):
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
        'activate_keys_on_creation': 'bool',
        'certificate_issue_date': 'datetime',
        'certificate_ttl_in_seconds': 'int',
        'id': 'str',
        'name': 'str',
        'rules': 'list[PathRule]'
    }

    attribute_map = {
        'activate_keys_on_creation': 'activate_keys_on_creation',
        'certificate_issue_date': 'certificate_issue_date',
        'certificate_ttl_in_seconds': 'certificate_ttl_in_seconds',
        'id': 'id',
        'name': 'name',
        'rules': 'rules'
    }

    def __init__(self, activate_keys_on_creation=None, certificate_issue_date=None, certificate_ttl_in_seconds=None, id=None, name=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """KMIPClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._activate_keys_on_creation = None
        self._certificate_issue_date = None
        self._certificate_ttl_in_seconds = None
        self._id = None
        self._name = None
        self._rules = None
        self.discriminator = None

        if activate_keys_on_creation is not None:
            self.activate_keys_on_creation = activate_keys_on_creation
        if certificate_issue_date is not None:
            self.certificate_issue_date = certificate_issue_date
        if certificate_ttl_in_seconds is not None:
            self.certificate_ttl_in_seconds = certificate_ttl_in_seconds
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules

    @property
    def activate_keys_on_creation(self):
        """Gets the activate_keys_on_creation of this KMIPClient.  # noqa: E501


        :return: The activate_keys_on_creation of this KMIPClient.  # noqa: E501
        :rtype: bool
        """
        return self._activate_keys_on_creation

    @activate_keys_on_creation.setter
    def activate_keys_on_creation(self, activate_keys_on_creation):
        """Sets the activate_keys_on_creation of this KMIPClient.


        :param activate_keys_on_creation: The activate_keys_on_creation of this KMIPClient.  # noqa: E501
        :type: bool
        """

        self._activate_keys_on_creation = activate_keys_on_creation

    @property
    def certificate_issue_date(self):
        """Gets the certificate_issue_date of this KMIPClient.  # noqa: E501


        :return: The certificate_issue_date of this KMIPClient.  # noqa: E501
        :rtype: datetime
        """
        return self._certificate_issue_date

    @certificate_issue_date.setter
    def certificate_issue_date(self, certificate_issue_date):
        """Sets the certificate_issue_date of this KMIPClient.


        :param certificate_issue_date: The certificate_issue_date of this KMIPClient.  # noqa: E501
        :type: datetime
        """

        self._certificate_issue_date = certificate_issue_date

    @property
    def certificate_ttl_in_seconds(self):
        """Gets the certificate_ttl_in_seconds of this KMIPClient.  # noqa: E501


        :return: The certificate_ttl_in_seconds of this KMIPClient.  # noqa: E501
        :rtype: int
        """
        return self._certificate_ttl_in_seconds

    @certificate_ttl_in_seconds.setter
    def certificate_ttl_in_seconds(self, certificate_ttl_in_seconds):
        """Sets the certificate_ttl_in_seconds of this KMIPClient.


        :param certificate_ttl_in_seconds: The certificate_ttl_in_seconds of this KMIPClient.  # noqa: E501
        :type: int
        """

        self._certificate_ttl_in_seconds = certificate_ttl_in_seconds

    @property
    def id(self):
        """Gets the id of this KMIPClient.  # noqa: E501


        :return: The id of this KMIPClient.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KMIPClient.


        :param id: The id of this KMIPClient.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this KMIPClient.  # noqa: E501


        :return: The name of this KMIPClient.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KMIPClient.


        :param name: The name of this KMIPClient.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rules(self):
        """Gets the rules of this KMIPClient.  # noqa: E501


        :return: The rules of this KMIPClient.  # noqa: E501
        :rtype: list[PathRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this KMIPClient.


        :param rules: The rules of this KMIPClient.  # noqa: E501
        :type: list[PathRule]
        """

        self._rules = rules

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
        if not isinstance(other, KMIPClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KMIPClient):
            return True

        return self.to_dict() != other.to_dict()
