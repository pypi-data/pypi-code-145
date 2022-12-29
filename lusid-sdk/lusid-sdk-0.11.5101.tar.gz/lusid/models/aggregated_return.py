# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5101
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class AggregatedReturn(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'effective_at': 'datetime',
        'end_of_period': 'datetime',
        'opening_market_value': 'float',
        'closing_market_value': 'float',
        'metrics_value': 'dict(str, float)',
        'frequency': 'str',
        'composite_members': 'int',
        'composite_members_without_return': 'list[ResourceId]'
    }

    attribute_map = {
        'effective_at': 'effectiveAt',
        'end_of_period': 'endOfPeriod',
        'opening_market_value': 'openingMarketValue',
        'closing_market_value': 'closingMarketValue',
        'metrics_value': 'metricsValue',
        'frequency': 'frequency',
        'composite_members': 'compositeMembers',
        'composite_members_without_return': 'compositeMembersWithoutReturn'
    }

    required_map = {
        'effective_at': 'required',
        'end_of_period': 'required',
        'opening_market_value': 'optional',
        'closing_market_value': 'optional',
        'metrics_value': 'required',
        'frequency': 'optional',
        'composite_members': 'optional',
        'composite_members_without_return': 'optional'
    }

    def __init__(self, effective_at=None, end_of_period=None, opening_market_value=None, closing_market_value=None, metrics_value=None, frequency=None, composite_members=None, composite_members_without_return=None, local_vars_configuration=None):  # noqa: E501
        """AggregatedReturn - a model defined in OpenAPI"
        
        :param effective_at:  The effectiveAt for the return. (required)
        :type effective_at: datetime
        :param end_of_period:  The end of period date. For the monthly period this will be the Month End Date. (required)
        :type end_of_period: datetime
        :param opening_market_value:  The opening market value.
        :type opening_market_value: float
        :param closing_market_value:  The closing market value.
        :type closing_market_value: float
        :param metrics_value:  The value for the specified metric. (required)
        :type metrics_value: dict(str, float)
        :param frequency:  Show the aggregated output returns on a Daily or Monthly period.
        :type frequency: str
        :param composite_members:  The number of members in the Composite on the given day.
        :type composite_members: int
        :param composite_members_without_return:  List containing Composite members which post no return on the given day.
        :type composite_members_without_return: list[lusid.ResourceId]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_at = None
        self._end_of_period = None
        self._opening_market_value = None
        self._closing_market_value = None
        self._metrics_value = None
        self._frequency = None
        self._composite_members = None
        self._composite_members_without_return = None
        self.discriminator = None

        self.effective_at = effective_at
        self.end_of_period = end_of_period
        self.opening_market_value = opening_market_value
        self.closing_market_value = closing_market_value
        self.metrics_value = metrics_value
        self.frequency = frequency
        self.composite_members = composite_members
        self.composite_members_without_return = composite_members_without_return

    @property
    def effective_at(self):
        """Gets the effective_at of this AggregatedReturn.  # noqa: E501

        The effectiveAt for the return.  # noqa: E501

        :return: The effective_at of this AggregatedReturn.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this AggregatedReturn.

        The effectiveAt for the return.  # noqa: E501

        :param effective_at: The effective_at of this AggregatedReturn.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def end_of_period(self):
        """Gets the end_of_period of this AggregatedReturn.  # noqa: E501

        The end of period date. For the monthly period this will be the Month End Date.  # noqa: E501

        :return: The end_of_period of this AggregatedReturn.  # noqa: E501
        :rtype: datetime
        """
        return self._end_of_period

    @end_of_period.setter
    def end_of_period(self, end_of_period):
        """Sets the end_of_period of this AggregatedReturn.

        The end of period date. For the monthly period this will be the Month End Date.  # noqa: E501

        :param end_of_period: The end_of_period of this AggregatedReturn.  # noqa: E501
        :type end_of_period: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_of_period is None:  # noqa: E501
            raise ValueError("Invalid value for `end_of_period`, must not be `None`")  # noqa: E501

        self._end_of_period = end_of_period

    @property
    def opening_market_value(self):
        """Gets the opening_market_value of this AggregatedReturn.  # noqa: E501

        The opening market value.  # noqa: E501

        :return: The opening_market_value of this AggregatedReturn.  # noqa: E501
        :rtype: float
        """
        return self._opening_market_value

    @opening_market_value.setter
    def opening_market_value(self, opening_market_value):
        """Sets the opening_market_value of this AggregatedReturn.

        The opening market value.  # noqa: E501

        :param opening_market_value: The opening_market_value of this AggregatedReturn.  # noqa: E501
        :type opening_market_value: float
        """

        self._opening_market_value = opening_market_value

    @property
    def closing_market_value(self):
        """Gets the closing_market_value of this AggregatedReturn.  # noqa: E501

        The closing market value.  # noqa: E501

        :return: The closing_market_value of this AggregatedReturn.  # noqa: E501
        :rtype: float
        """
        return self._closing_market_value

    @closing_market_value.setter
    def closing_market_value(self, closing_market_value):
        """Sets the closing_market_value of this AggregatedReturn.

        The closing market value.  # noqa: E501

        :param closing_market_value: The closing_market_value of this AggregatedReturn.  # noqa: E501
        :type closing_market_value: float
        """

        self._closing_market_value = closing_market_value

    @property
    def metrics_value(self):
        """Gets the metrics_value of this AggregatedReturn.  # noqa: E501

        The value for the specified metric.  # noqa: E501

        :return: The metrics_value of this AggregatedReturn.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._metrics_value

    @metrics_value.setter
    def metrics_value(self, metrics_value):
        """Sets the metrics_value of this AggregatedReturn.

        The value for the specified metric.  # noqa: E501

        :param metrics_value: The metrics_value of this AggregatedReturn.  # noqa: E501
        :type metrics_value: dict(str, float)
        """
        if self.local_vars_configuration.client_side_validation and metrics_value is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics_value`, must not be `None`")  # noqa: E501

        self._metrics_value = metrics_value

    @property
    def frequency(self):
        """Gets the frequency of this AggregatedReturn.  # noqa: E501

        Show the aggregated output returns on a Daily or Monthly period.  # noqa: E501

        :return: The frequency of this AggregatedReturn.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this AggregatedReturn.

        Show the aggregated output returns on a Daily or Monthly period.  # noqa: E501

        :param frequency: The frequency of this AggregatedReturn.  # noqa: E501
        :type frequency: str
        """

        self._frequency = frequency

    @property
    def composite_members(self):
        """Gets the composite_members of this AggregatedReturn.  # noqa: E501

        The number of members in the Composite on the given day.  # noqa: E501

        :return: The composite_members of this AggregatedReturn.  # noqa: E501
        :rtype: int
        """
        return self._composite_members

    @composite_members.setter
    def composite_members(self, composite_members):
        """Sets the composite_members of this AggregatedReturn.

        The number of members in the Composite on the given day.  # noqa: E501

        :param composite_members: The composite_members of this AggregatedReturn.  # noqa: E501
        :type composite_members: int
        """

        self._composite_members = composite_members

    @property
    def composite_members_without_return(self):
        """Gets the composite_members_without_return of this AggregatedReturn.  # noqa: E501

        List containing Composite members which post no return on the given day.  # noqa: E501

        :return: The composite_members_without_return of this AggregatedReturn.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._composite_members_without_return

    @composite_members_without_return.setter
    def composite_members_without_return(self, composite_members_without_return):
        """Sets the composite_members_without_return of this AggregatedReturn.

        List containing Composite members which post no return on the given day.  # noqa: E501

        :param composite_members_without_return: The composite_members_without_return of this AggregatedReturn.  # noqa: E501
        :type composite_members_without_return: list[lusid.ResourceId]
        """

        self._composite_members_without_return = composite_members_without_return

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AggregatedReturn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatedReturn):
            return True

        return self.to_dict() != other.to_dict()
