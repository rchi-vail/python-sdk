# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from freeclimb.configuration import Configuration


class FilterLogsRequest(object):
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
        'pql': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'pql': 'pql',
        'request_id': 'requestId'
    }

    def __init__(self, pql=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """FilterLogsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pql = None
        self._request_id = None
        self.discriminator = None

        self.pql = pql
        if request_id is not None:
            self.request_id = request_id

    @property
    def pql(self):
        """Gets the pql of this FilterLogsRequest.  # noqa: E501

        The filter query for retrieving logs. See **Performance Query Language** below.  # noqa: E501

        :return: The pql of this FilterLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._pql

    @pql.setter
    def pql(self, pql):
        """Sets the pql of this FilterLogsRequest.

        The filter query for retrieving logs. See **Performance Query Language** below.  # noqa: E501

        :param pql: The pql of this FilterLogsRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pql is None:  # noqa: E501
            raise ValueError("Invalid value for `pql`, must not be `None`")  # noqa: E501

        self._pql = pql

    @property
    def request_id(self):
        """Gets the request_id of this FilterLogsRequest.  # noqa: E501

        RequestId for this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response (e.g., X-Pulse-Request-Id: <requestId>).  # noqa: E501

        :return: The request_id of this FilterLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this FilterLogsRequest.

        RequestId for this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response (e.g., X-Pulse-Request-Id: <requestId>).  # noqa: E501

        :param request_id: The request_id of this FilterLogsRequest.  # noqa: E501
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
        if not isinstance(other, FilterLogsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterLogsRequest):
            return True

        return self.to_dict() != other.to_dict()
