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

from freeclimb.configuration import Configuration


class BuyIncomingNumberRequest(object):
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
        'phone_number': 'str',
        'alias': 'str',
        'application_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'phone_number': 'phoneNumber',
        'alias': 'alias',
        'application_id': 'applicationId',
        'request_id': 'requestId'
    }

    def __init__(self, phone_number=None, alias=None, application_id=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """BuyIncomingNumberRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._phone_number = None
        self._alias = None
        self._application_id = None
        self._request_id = None
        self.discriminator = None

        self.phone_number = phone_number
        if alias is not None:
            self.alias = alias
        if application_id is not None:
            self.application_id = application_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def phone_number(self):
        """Gets the phone_number of this BuyIncomingNumberRequest.  # noqa: E501

        Phone number to purchase in E.164 format (as returned in the list of Available Phone Numbers).  # noqa: E501

        :return: The phone_number of this BuyIncomingNumberRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this BuyIncomingNumberRequest.

        Phone number to purchase in E.164 format (as returned in the list of Available Phone Numbers).  # noqa: E501

        :param phone_number: The phone_number of this BuyIncomingNumberRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def alias(self):
        """Gets the alias of this BuyIncomingNumberRequest.  # noqa: E501

        Description for this new incoming phone number (max 64 characters).  # noqa: E501

        :return: The alias of this BuyIncomingNumberRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this BuyIncomingNumberRequest.

        Description for this new incoming phone number (max 64 characters).  # noqa: E501

        :param alias: The alias of this BuyIncomingNumberRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def application_id(self):
        """Gets the application_id of this BuyIncomingNumberRequest.  # noqa: E501

        ID of the application that should handle phone calls to the number.  # noqa: E501

        :return: The application_id of this BuyIncomingNumberRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this BuyIncomingNumberRequest.

        ID of the application that should handle phone calls to the number.  # noqa: E501

        :param application_id: The application_id of this BuyIncomingNumberRequest.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def request_id(self):
        """Gets the request_id of this BuyIncomingNumberRequest.  # noqa: E501

        RequestId for this request starting with prefix `RQ` followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response, (e.g., `X-Pulse-Request-Id: <requestId>`).  # noqa: E501

        :return: The request_id of this BuyIncomingNumberRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this BuyIncomingNumberRequest.

        RequestId for this request starting with prefix `RQ` followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response, (e.g., `X-Pulse-Request-Id: <requestId>`).  # noqa: E501

        :param request_id: The request_id of this BuyIncomingNumberRequest.  # noqa: E501
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
        if not isinstance(other, BuyIncomingNumberRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuyIncomingNumberRequest):
            return True

        return self.to_dict() != other.to_dict()