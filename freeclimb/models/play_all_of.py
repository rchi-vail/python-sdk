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


class PlayAllOf(object):
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
        'file': 'str',
        'loop': 'int',
        'conference_id': 'str',
        'privacy_mode': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'loop': 'loop',
        'conference_id': 'conferenceId',
        'privacy_mode': 'privacyMode'
    }

    def __init__(self, file=None, loop=None, conference_id=None, privacy_mode=None, local_vars_configuration=None):  # noqa: E501
        """PlayAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file = None
        self._loop = None
        self._conference_id = None
        self._privacy_mode = None
        self.discriminator = None

        self.file = file
        if loop is not None:
            self.loop = loop
        if conference_id is not None:
            self.conference_id = conference_id
        if privacy_mode is not None:
            self.privacy_mode = privacy_mode

    @property
    def file(self):
        """Gets the file of this PlayAllOf.  # noqa: E501

        RL of the audio file to be played to the caller. The URL can be the `recordingUrl` generated from the `RecordUtterance` or `StartRecordCall` PerCL commands.   # noqa: E501

        :return: The file of this PlayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this PlayAllOf.

        RL of the audio file to be played to the caller. The URL can be the `recordingUrl` generated from the `RecordUtterance` or `StartRecordCall` PerCL commands.   # noqa: E501

        :param file: The file of this PlayAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def loop(self):
        """Gets the loop of this PlayAllOf.  # noqa: E501

        Number of times the audio file is played. Specifying '0' causes the Play action to loop until the Call is hung up.  # noqa: E501

        :return: The loop of this PlayAllOf.  # noqa: E501
        :rtype: int
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this PlayAllOf.

        Number of times the audio file is played. Specifying '0' causes the Play action to loop until the Call is hung up.  # noqa: E501

        :param loop: The loop of this PlayAllOf.  # noqa: E501
        :type: int
        """

        self._loop = loop

    @property
    def conference_id(self):
        """Gets the conference_id of this PlayAllOf.  # noqa: E501

        ID of the Conference the audio should be rendered to. If this is not specified, the audio is by default rendered to the caller associated with the call leg that corresponds to the current PerCL execution context. The call leg associated with this command must be in the specified Conference or the command will return an error.  # noqa: E501

        :return: The conference_id of this PlayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this PlayAllOf.

        ID of the Conference the audio should be rendered to. If this is not specified, the audio is by default rendered to the caller associated with the call leg that corresponds to the current PerCL execution context. The call leg associated with this command must be in the specified Conference or the command will return an error.  # noqa: E501

        :param conference_id: The conference_id of this PlayAllOf.  # noqa: E501
        :type: str
        """

        self._conference_id = conference_id

    @property
    def privacy_mode(self):
        """Gets the privacy_mode of this PlayAllOf.  # noqa: E501

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :return: The privacy_mode of this PlayAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._privacy_mode

    @privacy_mode.setter
    def privacy_mode(self, privacy_mode):
        """Sets the privacy_mode of this PlayAllOf.

        Parameter `privacyMode` will not log the `text` as required by PCI compliance.  # noqa: E501

        :param privacy_mode: The privacy_mode of this PlayAllOf.  # noqa: E501
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
        if not isinstance(other, PlayAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayAllOf):
            return True

        return self.to_dict() != other.to_dict()
