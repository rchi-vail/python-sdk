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


class ApplicationRequest(object):
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
        'voice_url': 'str',
        'voice_fallback_url': 'str',
        'call_connect_url': 'str',
        'status_callback_url': 'str',
        'sms_url': 'str',
        'sms_fallback_url': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'voice_url': 'voiceUrl',
        'voice_fallback_url': 'voiceFallbackUrl',
        'call_connect_url': 'callConnectUrl',
        'status_callback_url': 'statusCallbackUrl',
        'sms_url': 'smsUrl',
        'sms_fallback_url': 'smsFallbackUrl',
        'request_id': 'requestId'
    }

    def __init__(self, alias=None, voice_url=None, voice_fallback_url=None, call_connect_url=None, status_callback_url=None, sms_url=None, sms_fallback_url=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._voice_url = None
        self._voice_fallback_url = None
        self._call_connect_url = None
        self._status_callback_url = None
        self._sms_url = None
        self._sms_fallback_url = None
        self._request_id = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if voice_url is not None:
            self.voice_url = voice_url
        if voice_fallback_url is not None:
            self.voice_fallback_url = voice_fallback_url
        if call_connect_url is not None:
            self.call_connect_url = call_connect_url
        if status_callback_url is not None:
            self.status_callback_url = status_callback_url
        if sms_url is not None:
            self.sms_url = sms_url
        if sms_fallback_url is not None:
            self.sms_fallback_url = sms_fallback_url
        if request_id is not None:
            self.request_id = request_id

    @property
    def alias(self):
        """Gets the alias of this ApplicationRequest.  # noqa: E501

        A human readable description of the application, with maximum length 64 characters.  # noqa: E501

        :return: The alias of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ApplicationRequest.

        A human readable description of the application, with maximum length 64 characters.  # noqa: E501

        :param alias: The alias of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def voice_url(self):
        """Gets the voice_url of this ApplicationRequest.  # noqa: E501

        The URL that FreeClimb will request when an inbound call arrives on a phone number assigned to this application. Used only for inbound calls.  # noqa: E501

        :return: The voice_url of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._voice_url

    @voice_url.setter
    def voice_url(self, voice_url):
        """Sets the voice_url of this ApplicationRequest.

        The URL that FreeClimb will request when an inbound call arrives on a phone number assigned to this application. Used only for inbound calls.  # noqa: E501

        :param voice_url: The voice_url of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._voice_url = voice_url

    @property
    def voice_fallback_url(self):
        """Gets the voice_fallback_url of this ApplicationRequest.  # noqa: E501

        The URL that FreeClimb will request if it times out waiting for a response from the voiceUrl. Used for inbound calls only. Note: A PerCL response is expected to control the inbound call.  # noqa: E501

        :return: The voice_fallback_url of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._voice_fallback_url

    @voice_fallback_url.setter
    def voice_fallback_url(self, voice_fallback_url):
        """Sets the voice_fallback_url of this ApplicationRequest.

        The URL that FreeClimb will request if it times out waiting for a response from the voiceUrl. Used for inbound calls only. Note: A PerCL response is expected to control the inbound call.  # noqa: E501

        :param voice_fallback_url: The voice_fallback_url of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._voice_fallback_url = voice_fallback_url

    @property
    def call_connect_url(self):
        """Gets the call_connect_url of this ApplicationRequest.  # noqa: E501

        The URL that FreeClimb will request when an outbound call request is complete. Used for outbound calls only.  Note: A PerCL response is expected if the outbound call is connected (status=InProgress) to control the call.  # noqa: E501

        :return: The call_connect_url of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._call_connect_url

    @call_connect_url.setter
    def call_connect_url(self, call_connect_url):
        """Sets the call_connect_url of this ApplicationRequest.

        The URL that FreeClimb will request when an outbound call request is complete. Used for outbound calls only.  Note: A PerCL response is expected if the outbound call is connected (status=InProgress) to control the call.  # noqa: E501

        :param call_connect_url: The call_connect_url of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._call_connect_url = call_connect_url

    @property
    def status_callback_url(self):
        """Gets the status_callback_url of this ApplicationRequest.  # noqa: E501

        The URL that FreeClimb will request to pass call status (such as call ended) to the application.  Note: This is a notification only; any PerCL returned will be ignored.  # noqa: E501

        :return: The status_callback_url of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_callback_url

    @status_callback_url.setter
    def status_callback_url(self, status_callback_url):
        """Sets the status_callback_url of this ApplicationRequest.

        The URL that FreeClimb will request to pass call status (such as call ended) to the application.  Note: This is a notification only; any PerCL returned will be ignored.  # noqa: E501

        :param status_callback_url: The status_callback_url of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._status_callback_url = status_callback_url

    @property
    def sms_url(self):
        """Gets the sms_url of this ApplicationRequest.  # noqa: E501

        The URL that FreeClimb will request when a phone number assigned to this application receives an incoming SMS message. Used for inbound SMS only.  Note: Any PerCL returned will be ignored.  # noqa: E501

        :return: The sms_url of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._sms_url

    @sms_url.setter
    def sms_url(self, sms_url):
        """Sets the sms_url of this ApplicationRequest.

        The URL that FreeClimb will request when a phone number assigned to this application receives an incoming SMS message. Used for inbound SMS only.  Note: Any PerCL returned will be ignored.  # noqa: E501

        :param sms_url: The sms_url of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._sms_url = sms_url

    @property
    def sms_fallback_url(self):
        """Gets the sms_fallback_url of this ApplicationRequest.  # noqa: E501

        The URL that FreeClimb will request if it times out waiting for a response from the smsUrl. Used for inbound SMS only.  Note: Any PerCL returned will be ignored.  # noqa: E501

        :return: The sms_fallback_url of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._sms_fallback_url

    @sms_fallback_url.setter
    def sms_fallback_url(self, sms_fallback_url):
        """Sets the sms_fallback_url of this ApplicationRequest.

        The URL that FreeClimb will request if it times out waiting for a response from the smsUrl. Used for inbound SMS only.  Note: Any PerCL returned will be ignored.  # noqa: E501

        :param sms_fallback_url: The sms_fallback_url of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._sms_fallback_url = sms_fallback_url

    @property
    def request_id(self):
        """Gets the request_id of this ApplicationRequest.  # noqa: E501

        The requestId for this request starting with prefix \"RQ\" followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response, e.g. X-Pulse-Request-Id: <requestId>  # noqa: E501

        :return: The request_id of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ApplicationRequest.

        The requestId for this request starting with prefix \"RQ\" followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request will include this requestId. If it is not provided, FreeClimb will generate a requestId and return it as a header in the response, e.g. X-Pulse-Request-Id: <requestId>  # noqa: E501

        :param request_id: The request_id of this ApplicationRequest.  # noqa: E501
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
        if not isinstance(other, ApplicationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationRequest):
            return True

        return self.to_dict() != other.to_dict()
