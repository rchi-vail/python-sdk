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


class UpdateConferenceParticipantRequest(object):
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
        'talk': 'bool',
        'listen': 'bool',
        'request_id': 'str'
    }

    attribute_map = {
        'talk': 'talk',
        'listen': 'listen',
        'request_id': 'requestId'
    }

    def __init__(self, talk=None, listen=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """UpdateConferenceParticipantRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._talk = None
        self._listen = None
        self._request_id = None
        self.discriminator = None

        if talk is not None:
            self.talk = talk
        if listen is not None:
            self.listen = listen
        if request_id is not None:
            self.request_id = request_id

    @property
    def talk(self):
        """Gets the talk of this UpdateConferenceParticipantRequest.  # noqa: E501

        (Optional) Default is `true`. Setting to `false` mutes the Participant. FreeClimb returns an error and ignores any other value.  # noqa: E501

        :return: The talk of this UpdateConferenceParticipantRequest.  # noqa: E501
        :rtype: bool
        """
        return self._talk

    @talk.setter
    def talk(self, talk):
        """Sets the talk of this UpdateConferenceParticipantRequest.

        (Optional) Default is `true`. Setting to `false` mutes the Participant. FreeClimb returns an error and ignores any other value.  # noqa: E501

        :param talk: The talk of this UpdateConferenceParticipantRequest.  # noqa: E501
        :type: bool
        """

        self._talk = talk

    @property
    def listen(self):
        """Gets the listen of this UpdateConferenceParticipantRequest.  # noqa: E501

        (Optional) Default is `true`. Setting to `false` silences the Conference for this Participant. FreeClimb returns an error and ignores any other value.  # noqa: E501

        :return: The listen of this UpdateConferenceParticipantRequest.  # noqa: E501
        :rtype: bool
        """
        return self._listen

    @listen.setter
    def listen(self, listen):
        """Sets the listen of this UpdateConferenceParticipantRequest.

        (Optional) Default is `true`. Setting to `false` silences the Conference for this Participant. FreeClimb returns an error and ignores any other value.  # noqa: E501

        :param listen: The listen of this UpdateConferenceParticipantRequest.  # noqa: E501
        :type: bool
        """

        self._listen = listen

    @property
    def request_id(self):
        """Gets the request_id of this UpdateConferenceParticipantRequest.  # noqa: E501

        ID of this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request include this requestId. If this value is not provided, FreeClimb generates a requestId and returns it as a header in the response (e.g., X-Pulse-Request-Id: <requestId>).  # noqa: E501

        :return: The request_id of this UpdateConferenceParticipantRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateConferenceParticipantRequest.

        ID of this request starting with prefix *RQ* followed by 40 hexadecimal characters. FreeClimb logs generated while processing this request include this requestId. If this value is not provided, FreeClimb generates a requestId and returns it as a header in the response (e.g., X-Pulse-Request-Id: <requestId>).  # noqa: E501

        :param request_id: The request_id of this UpdateConferenceParticipantRequest.  # noqa: E501
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
        if not isinstance(other, UpdateConferenceParticipantRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateConferenceParticipantRequest):
            return True

        return self.to_dict() != other.to_dict()