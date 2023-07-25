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


class ListHeartbeatResponse(object):
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
        'request_id': 'str',
        'took': 'float',
        'data': 'ListHeartbeatResponseAllOfData'
    }

    attribute_map = {
        'request_id': 'requestId',
        'took': 'took',
        'data': 'data'
    }

    def __init__(self, request_id=None, took=0.0, data=None):  # noqa: E501
        """ListHeartbeatResponse - a model defined in OpenAPI"""  # noqa: E501

        self._request_id = None
        self._took = None
        self._data = None
        self.discriminator = None

        self.request_id = request_id
        self.took = took
        if data is not None:
            self.data = data

    @property
    def request_id(self):
        """Gets the request_id of this ListHeartbeatResponse.  # noqa: E501


        :return: The request_id of this ListHeartbeatResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListHeartbeatResponse.


        :param request_id: The request_id of this ListHeartbeatResponse.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def took(self):
        """Gets the took of this ListHeartbeatResponse.  # noqa: E501


        :return: The took of this ListHeartbeatResponse.  # noqa: E501
        :rtype: float
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this ListHeartbeatResponse.


        :param took: The took of this ListHeartbeatResponse.  # noqa: E501
        :type: float
        """
        if took is None:
            raise ValueError("Invalid value for `took`, must not be `None`")  # noqa: E501

        self._took = took

    @property
    def data(self):
        """Gets the data of this ListHeartbeatResponse.  # noqa: E501


        :return: The data of this ListHeartbeatResponse.  # noqa: E501
        :rtype: ListHeartbeatResponseAllOfData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListHeartbeatResponse.


        :param data: The data of this ListHeartbeatResponse.  # noqa: E501
        :type: ListHeartbeatResponseAllOfData
        """

        self._data = data

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
        if not isinstance(other, ListHeartbeatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
