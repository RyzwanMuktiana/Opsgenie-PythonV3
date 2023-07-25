# coding: utf-8

"""
    Python SDK for Opsgenie REST API

    Python SDK for Opsgenie REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@opsgenie.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CreateHeartbeatPayload(object):
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
        'name': 'str',
        'description': 'str',
        'interval': 'int',
        'interval_unit': 'str',
        'enabled': 'bool',
        'owner_team': 'CreateHeartbeatPayloadAllOfOwnerTeam',
        'alert_message': 'str',
        'alert_tags': 'list[str]',
        'alert_priority': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'interval': 'interval',
        'interval_unit': 'intervalUnit',
        'enabled': 'enabled',
        'owner_team': 'ownerTeam',
        'alert_message': 'alertMessage',
        'alert_tags': 'alertTags',
        'alert_priority': 'alertPriority'
    }

    def __init__(self, name=None, description=None, interval=None, interval_unit=None, enabled=None, owner_team=None, alert_message=None, alert_tags=None, alert_priority=None):  # noqa: E501
        """CreateHeartbeatPayload - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._interval = None
        self._interval_unit = None
        self._enabled = None
        self._owner_team = None
        self._alert_message = None
        self._alert_tags = None
        self._alert_priority = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.interval = interval
        self.interval_unit = interval_unit
        self.enabled = enabled
        if owner_team is not None:
            self.owner_team = owner_team
        if alert_message is not None:
            self.alert_message = alert_message
        if alert_tags is not None:
            self.alert_tags = alert_tags
        if alert_priority is not None:
            self.alert_priority = alert_priority

    @property
    def name(self):
        """Gets the name of this CreateHeartbeatPayload.  # noqa: E501

        Name of the heartbeat  # noqa: E501

        :return: The name of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHeartbeatPayload.

        Name of the heartbeat  # noqa: E501

        :param name: The name of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateHeartbeatPayload.  # noqa: E501

        An optional description of the heartbeat  # noqa: E501

        :return: The description of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHeartbeatPayload.

        An optional description of the heartbeat  # noqa: E501

        :param description: The description of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")  # noqa: E501

        self._description = description

    @property
    def interval(self):
        """Gets the interval of this CreateHeartbeatPayload.  # noqa: E501

        Specifies how often a heartbeat message should be expected  # noqa: E501

        :return: The interval of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreateHeartbeatPayload.

        Specifies how often a heartbeat message should be expected  # noqa: E501

        :param interval: The interval of this CreateHeartbeatPayload.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501
        if interval is not None and interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._interval = interval

    @property
    def interval_unit(self):
        """Gets the interval_unit of this CreateHeartbeatPayload.  # noqa: E501

        Interval specified as 'minutes', 'hours' or 'days'  # noqa: E501

        :return: The interval_unit of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._interval_unit

    @interval_unit.setter
    def interval_unit(self, interval_unit):
        """Sets the interval_unit of this CreateHeartbeatPayload.

        Interval specified as 'minutes', 'hours' or 'days'  # noqa: E501

        :param interval_unit: The interval_unit of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if interval_unit is None:
            raise ValueError("Invalid value for `interval_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["minutes", "hours", "days"]  # noqa: E501
        if interval_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `interval_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(interval_unit, allowed_values)
            )

        self._interval_unit = interval_unit

    @property
    def enabled(self):
        """Gets the enabled of this CreateHeartbeatPayload.  # noqa: E501

        Enable/disable heartbeat monitoring  # noqa: E501

        :return: The enabled of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateHeartbeatPayload.

        Enable/disable heartbeat monitoring  # noqa: E501

        :param enabled: The enabled of this CreateHeartbeatPayload.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def owner_team(self):
        """Gets the owner_team of this CreateHeartbeatPayload.  # noqa: E501


        :return: The owner_team of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: CreateHeartbeatPayloadAllOfOwnerTeam
        """
        return self._owner_team

    @owner_team.setter
    def owner_team(self, owner_team):
        """Sets the owner_team of this CreateHeartbeatPayload.


        :param owner_team: The owner_team of this CreateHeartbeatPayload.  # noqa: E501
        :type: CreateHeartbeatPayloadAllOfOwnerTeam
        """

        self._owner_team = owner_team

    @property
    def alert_message(self):
        """Gets the alert_message of this CreateHeartbeatPayload.  # noqa: E501

        Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is 'HeartbeatName is expired'  # noqa: E501

        :return: The alert_message of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._alert_message

    @alert_message.setter
    def alert_message(self, alert_message):
        """Sets the alert_message of this CreateHeartbeatPayload.

        Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is 'HeartbeatName is expired'  # noqa: E501

        :param alert_message: The alert_message of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        if alert_message is not None and len(alert_message) > 130:
            raise ValueError("Invalid value for `alert_message`, length must be less than or equal to `130`")  # noqa: E501

        self._alert_message = alert_message

    @property
    def alert_tags(self):
        """Gets the alert_tags of this CreateHeartbeatPayload.  # noqa: E501

        Specifies the alert tags for heartbeat expiration alert  # noqa: E501

        :return: The alert_tags of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_tags

    @alert_tags.setter
    def alert_tags(self, alert_tags):
        """Sets the alert_tags of this CreateHeartbeatPayload.

        Specifies the alert tags for heartbeat expiration alert  # noqa: E501

        :param alert_tags: The alert_tags of this CreateHeartbeatPayload.  # noqa: E501
        :type: list[str]
        """

        self._alert_tags = alert_tags

    @property
    def alert_priority(self):
        """Gets the alert_priority of this CreateHeartbeatPayload.  # noqa: E501

        Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3  # noqa: E501

        :return: The alert_priority of this CreateHeartbeatPayload.  # noqa: E501
        :rtype: str
        """
        return self._alert_priority

    @alert_priority.setter
    def alert_priority(self, alert_priority):
        """Sets the alert_priority of this CreateHeartbeatPayload.

        Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3  # noqa: E501

        :param alert_priority: The alert_priority of this CreateHeartbeatPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["P1", "P2", "P3", "P4", "P5"]  # noqa: E501
        if alert_priority not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_priority` ({0}), must be one of {1}"  # noqa: E501
                .format(alert_priority, allowed_values)
            )

        self._alert_priority = alert_priority

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
        if not isinstance(other, CreateHeartbeatPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
