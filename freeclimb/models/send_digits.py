# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from freeclimb.configuration import Configuration


class SendDigits(object):
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
        'digits': 'str',
        'pause_ms': 'int',
        'privacy_mode': 'bool'
    }

    attribute_map = {
        'digits': 'digits',
        'pause_ms': 'pauseMs',
        'privacy_mode': 'privacyMode'
    }

    def __init__(self, digits=None, pause_ms=None, privacy_mode=None, local_vars_configuration=None):  # noqa: E501
        """SendDigits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._digits = None
        self._pause_ms = None
        self._privacy_mode = None
        self.discriminator = None

        self.digits = digits
        if pause_ms is not None:
            self.pause_ms = pause_ms
        if privacy_mode is not None:
            self.privacy_mode = privacy_mode

    @property
    def digits(self):
        """Gets the digits of this SendDigits.  # noqa: E501

        String containing the digits to be played. The string cannot be empty and can include any digit, plus `#`, or `*`, and allows embedding specification for delay or pause between the output of individual digits.  # noqa: E501

        :return: The digits of this SendDigits.  # noqa: E501
        :rtype: str
        """
        return self._digits

    @digits.setter
    def digits(self, digits):
        """Sets the digits of this SendDigits.

        String containing the digits to be played. The string cannot be empty and can include any digit, plus `#`, or `*`, and allows embedding specification for delay or pause between the output of individual digits.  # noqa: E501

        :param digits: The digits of this SendDigits.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and digits is None:  # noqa: E501
            raise ValueError("Invalid value for `digits`, must not be `None`")  # noqa: E501

        self._digits = digits

    @property
    def pause_ms(self):
        """Gets the pause_ms of this SendDigits.  # noqa: E501

        Pause between digits in milliseconds. Valid values are 100-1000 milliseconds and will be adjusted by FreeClimb to satisfy the constraint.  # noqa: E501

        :return: The pause_ms of this SendDigits.  # noqa: E501
        :rtype: int
        """
        return self._pause_ms

    @pause_ms.setter
    def pause_ms(self, pause_ms):
        """Sets the pause_ms of this SendDigits.

        Pause between digits in milliseconds. Valid values are 100-1000 milliseconds and will be adjusted by FreeClimb to satisfy the constraint.  # noqa: E501

        :param pause_ms: The pause_ms of this SendDigits.  # noqa: E501
        :type: int
        """

        self._pause_ms = pause_ms

    @property
    def privacy_mode(self):
        """Gets the privacy_mode of this SendDigits.  # noqa: E501

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :return: The privacy_mode of this SendDigits.  # noqa: E501
        :rtype: bool
        """
        return self._privacy_mode

    @privacy_mode.setter
    def privacy_mode(self, privacy_mode):
        """Sets the privacy_mode of this SendDigits.

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :param privacy_mode: The privacy_mode of this SendDigits.  # noqa: E501
        :type: bool
        """

        self._privacy_mode = privacy_mode

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
        if not isinstance(other, SendDigits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendDigits):
            return True

        return self.to_dict() != other.to_dict()
