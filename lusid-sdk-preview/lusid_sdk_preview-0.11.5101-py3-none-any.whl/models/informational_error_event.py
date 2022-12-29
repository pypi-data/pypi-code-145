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


class InformationalErrorEvent(object):
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
        'error_detail': 'str',
        'error_reason': 'str',
        'effective_at': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'error_detail': 'errorDetail',
        'error_reason': 'errorReason',
        'effective_at': 'effectiveAt',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'error_detail': 'required',
        'error_reason': 'required',
        'effective_at': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, error_detail=None, error_reason=None, effective_at=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """InformationalErrorEvent - a model defined in OpenAPI"
        
        :param error_detail:  The details of the error (required)
        :type error_detail: str
        :param error_reason:  The error reason (required)
        :type error_reason: str
        :param effective_at:  The effective date of the evaulation (required)
        :type effective_at: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._error_detail = None
        self._error_reason = None
        self._effective_at = None
        self._instrument_event_type = None
        self.discriminator = None

        self.error_detail = error_detail
        self.error_reason = error_reason
        self.effective_at = effective_at
        self.instrument_event_type = instrument_event_type

    @property
    def error_detail(self):
        """Gets the error_detail of this InformationalErrorEvent.  # noqa: E501

        The details of the error  # noqa: E501

        :return: The error_detail of this InformationalErrorEvent.  # noqa: E501
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        """Sets the error_detail of this InformationalErrorEvent.

        The details of the error  # noqa: E501

        :param error_detail: The error_detail of this InformationalErrorEvent.  # noqa: E501
        :type error_detail: str
        """
        if self.local_vars_configuration.client_side_validation and error_detail is None:  # noqa: E501
            raise ValueError("Invalid value for `error_detail`, must not be `None`")  # noqa: E501

        self._error_detail = error_detail

    @property
    def error_reason(self):
        """Gets the error_reason of this InformationalErrorEvent.  # noqa: E501

        The error reason  # noqa: E501

        :return: The error_reason of this InformationalErrorEvent.  # noqa: E501
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this InformationalErrorEvent.

        The error reason  # noqa: E501

        :param error_reason: The error_reason of this InformationalErrorEvent.  # noqa: E501
        :type error_reason: str
        """
        if self.local_vars_configuration.client_side_validation and error_reason is None:  # noqa: E501
            raise ValueError("Invalid value for `error_reason`, must not be `None`")  # noqa: E501

        self._error_reason = error_reason

    @property
    def effective_at(self):
        """Gets the effective_at of this InformationalErrorEvent.  # noqa: E501

        The effective date of the evaulation  # noqa: E501

        :return: The effective_at of this InformationalErrorEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this InformationalErrorEvent.

        The effective date of the evaulation  # noqa: E501

        :param effective_at: The effective_at of this InformationalErrorEvent.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this InformationalErrorEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :return: The instrument_event_type of this InformationalErrorEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this InformationalErrorEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this InformationalErrorEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, InformationalErrorEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InformationalErrorEvent):
            return True

        return self.to_dict() != other.to_dict()
