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


class RecordingResult(object):
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
        'uri': 'str',
        'date_created': 'str',
        'date_updated': 'str',
        'revision': 'int',
        'recording_id': 'str',
        'account_id': 'str',
        'call_id': 'str',
        'duration_sec': 'int',
        'conference_id': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'revision': 'revision',
        'recording_id': 'recordingId',
        'account_id': 'accountId',
        'call_id': 'callId',
        'duration_sec': 'durationSec',
        'conference_id': 'conferenceId'
    }

    def __init__(self, uri=None, date_created=None, date_updated=None, revision=None, recording_id=None, account_id=None, call_id=None, duration_sec=None, conference_id=None, local_vars_configuration=None):  # noqa: E501
        """RecordingResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uri = None
        self._date_created = None
        self._date_updated = None
        self._revision = None
        self._recording_id = None
        self._account_id = None
        self._call_id = None
        self._duration_sec = None
        self._conference_id = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if date_created is not None:
            self.date_created = date_created
        if date_updated is not None:
            self.date_updated = date_updated
        if revision is not None:
            self.revision = revision
        if recording_id is not None:
            self.recording_id = recording_id
        if account_id is not None:
            self.account_id = account_id
        if call_id is not None:
            self.call_id = call_id
        if duration_sec is not None:
            self.duration_sec = duration_sec
        if conference_id is not None:
            self.conference_id = conference_id

    @property
    def uri(self):
        """Gets the uri of this RecordingResult.  # noqa: E501

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :return: The uri of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RecordingResult.

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :param uri: The uri of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def date_created(self):
        """Gets the date_created of this RecordingResult.  # noqa: E501

        The date that this account was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_created of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RecordingResult.

        The date that this account was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_created: The date_created of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this RecordingResult.  # noqa: E501

        The date that this account was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_updated of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this RecordingResult.

        The date that this account was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_updated: The date_updated of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._date_updated = date_updated

    @property
    def revision(self):
        """Gets the revision of this RecordingResult.  # noqa: E501

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :return: The revision of this RecordingResult.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this RecordingResult.

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :param revision: The revision of this RecordingResult.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def recording_id(self):
        """Gets the recording_id of this RecordingResult.  # noqa: E501

        String that uniquely identifies this recording resource.  # noqa: E501

        :return: The recording_id of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id):
        """Sets the recording_id of this RecordingResult.

        String that uniquely identifies this recording resource.  # noqa: E501

        :param recording_id: The recording_id of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._recording_id = recording_id

    @property
    def account_id(self):
        """Gets the account_id of this RecordingResult.  # noqa: E501

        ID of the account that created this recording.  # noqa: E501

        :return: The account_id of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RecordingResult.

        ID of the account that created this recording.  # noqa: E501

        :param account_id: The account_id of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def call_id(self):
        """Gets the call_id of this RecordingResult.  # noqa: E501

        ID of the Call that was recorded. If a Conference was recorded, this value is empty and the conferenceId property is populated.  # noqa: E501

        :return: The call_id of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._call_id

    @call_id.setter
    def call_id(self, call_id):
        """Sets the call_id of this RecordingResult.

        ID of the Call that was recorded. If a Conference was recorded, this value is empty and the conferenceId property is populated.  # noqa: E501

        :param call_id: The call_id of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._call_id = call_id

    @property
    def duration_sec(self):
        """Gets the duration_sec of this RecordingResult.  # noqa: E501

        Length of the recording in seconds.  # noqa: E501

        :return: The duration_sec of this RecordingResult.  # noqa: E501
        :rtype: int
        """
        return self._duration_sec

    @duration_sec.setter
    def duration_sec(self, duration_sec):
        """Sets the duration_sec of this RecordingResult.

        Length of the recording in seconds.  # noqa: E501

        :param duration_sec: The duration_sec of this RecordingResult.  # noqa: E501
        :type: int
        """

        self._duration_sec = duration_sec

    @property
    def conference_id(self):
        """Gets the conference_id of this RecordingResult.  # noqa: E501

        ID of the Conference that was recorded. If a Call was recorded, this value is empty and the callId property is populated.  # noqa: E501

        :return: The conference_id of this RecordingResult.  # noqa: E501
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this RecordingResult.

        ID of the Conference that was recorded. If a Call was recorded, this value is empty and the callId property is populated.  # noqa: E501

        :param conference_id: The conference_id of this RecordingResult.  # noqa: E501
        :type: str
        """

        self._conference_id = conference_id

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
        if not isinstance(other, RecordingResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordingResult):
            return True

        return self.to_dict() != other.to_dict()
