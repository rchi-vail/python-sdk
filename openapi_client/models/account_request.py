# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class AccountRequest(object):
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
        'alias': 'str',
        'label': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'label': 'label',
        'request_id': 'requestId'
    }

    def __init__(self, alias=None, label=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """AccountRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._label = None
        self._request_id = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if label is not None:
            self.label = label
        if request_id is not None:
            self.request_id = request_id

    @property
    def alias(self):
        """Gets the alias of this AccountRequest.  # noqa: E501

        Description for this account.  # noqa: E501

        :return: The alias of this AccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AccountRequest.

        Description for this account.  # noqa: E501

        :param alias: The alias of this AccountRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def label(self):
        """Gets the label of this AccountRequest.  # noqa: E501

        Group to which this account belongs.  # noqa: E501

        :return: The label of this AccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AccountRequest.

        Group to which this account belongs.  # noqa: E501

        :param label: The label of this AccountRequest.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def request_id(self):
        """Gets the request_id of this AccountRequest.  # noqa: E501

        RequestId for this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response, e.g. X-Pulse-Request-Id: <requestId>  # noqa: E501

        :return: The request_id of this AccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AccountRequest.

        RequestId for this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response, e.g. X-Pulse-Request-Id: <requestId>  # noqa: E501

        :param request_id: The request_id of this AccountRequest.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

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
        if not isinstance(other, AccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountRequest):
            return True

        return self.to_dict() != other.to_dict()
