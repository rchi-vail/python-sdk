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


class AddToConference(object):
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
        'allow_call_control': 'bool',
        'call_control_sequence': 'str',
        'call_control_url': 'str',
        'conference_id': 'str',
        'call_id': 'bool',
        'leave_conference_url': 'str',
        'listen': 'bool',
        'notification_url': 'str',
        'start_conf_on_enter': 'bool',
        'talk': 'bool'
    }

    attribute_map = {
        'allow_call_control': 'allowCallControl',
        'call_control_sequence': 'callControlSequence',
        'call_control_url': 'callControlUrl',
        'conference_id': 'conferenceId',
        'call_id': 'callId',
        'leave_conference_url': 'leaveConferenceUrl',
        'listen': 'listen',
        'notification_url': 'notificationUrl',
        'start_conf_on_enter': 'startConfOnEnter',
        'talk': 'talk'
    }

    def __init__(self, allow_call_control=None, call_control_sequence=None, call_control_url=None, conference_id=None, call_id=None, leave_conference_url=None, listen=None, notification_url=None, start_conf_on_enter=None, talk=None, local_vars_configuration=None):  # noqa: E501
        """AddToConference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_call_control = None
        self._call_control_sequence = None
        self._call_control_url = None
        self._conference_id = None
        self._call_id = None
        self._leave_conference_url = None
        self._listen = None
        self._notification_url = None
        self._start_conf_on_enter = None
        self._talk = None
        self.discriminator = None

        if allow_call_control is not None:
            self.allow_call_control = allow_call_control
        if call_control_sequence is not None:
            self.call_control_sequence = call_control_sequence
        if call_control_url is not None:
            self.call_control_url = call_control_url
        self.conference_id = conference_id
        if call_id is not None:
            self.call_id = call_id
        if leave_conference_url is not None:
            self.leave_conference_url = leave_conference_url
        if listen is not None:
            self.listen = listen
        if notification_url is not None:
            self.notification_url = notification_url
        if start_conf_on_enter is not None:
            self.start_conf_on_enter = start_conf_on_enter
        if talk is not None:
            self.talk = talk

    @property
    def allow_call_control(self):
        """Gets the allow_call_control of this AddToConference.  # noqa: E501

        If `true`, Call control will be enabled for this Participant's Call leg.  # noqa: E501

        :return: The allow_call_control of this AddToConference.  # noqa: E501
        :rtype: bool
        """
        return self._allow_call_control

    @allow_call_control.setter
    def allow_call_control(self, allow_call_control):
        """Sets the allow_call_control of this AddToConference.

        If `true`, Call control will be enabled for this Participant's Call leg.  # noqa: E501

        :param allow_call_control: The allow_call_control of this AddToConference.  # noqa: E501
        :type: bool
        """

        self._allow_call_control = allow_call_control

    @property
    def call_control_sequence(self):
        """Gets the call_control_sequence of this AddToConference.  # noqa: E501

        Defines a sequence of digits that, when entered by this caller, invokes the `callControlUrl`. Only digits plus '*', and '#' may be used.  # noqa: E501

        :return: The call_control_sequence of this AddToConference.  # noqa: E501
        :rtype: str
        """
        return self._call_control_sequence

    @call_control_sequence.setter
    def call_control_sequence(self, call_control_sequence):
        """Sets the call_control_sequence of this AddToConference.

        Defines a sequence of digits that, when entered by this caller, invokes the `callControlUrl`. Only digits plus '*', and '#' may be used.  # noqa: E501

        :param call_control_sequence: The call_control_sequence of this AddToConference.  # noqa: E501
        :type: str
        """

        self._call_control_sequence = call_control_sequence

    @property
    def call_control_url(self):
        """Gets the call_control_url of this AddToConference.  # noqa: E501

        URL to be invoked when this Participant enters the digit sequence defined in the `callControlSequence` attribute.  # noqa: E501

        :return: The call_control_url of this AddToConference.  # noqa: E501
        :rtype: str
        """
        return self._call_control_url

    @call_control_url.setter
    def call_control_url(self, call_control_url):
        """Sets the call_control_url of this AddToConference.

        URL to be invoked when this Participant enters the digit sequence defined in the `callControlSequence` attribute.  # noqa: E501

        :param call_control_url: The call_control_url of this AddToConference.  # noqa: E501
        :type: str
        """

        self._call_control_url = call_control_url

    @property
    def conference_id(self):
        """Gets the conference_id of this AddToConference.  # noqa: E501

        ID of the Conference to which to add the Participant (Call leg). Conference must exist or an error will result.  # noqa: E501

        :return: The conference_id of this AddToConference.  # noqa: E501
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this AddToConference.

        ID of the Conference to which to add the Participant (Call leg). Conference must exist or an error will result.  # noqa: E501

        :param conference_id: The conference_id of this AddToConference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and conference_id is None:  # noqa: E501
            raise ValueError("Invalid value for `conference_id`, must not be `None`")  # noqa: E501

        self._conference_id = conference_id

    @property
    def call_id(self):
        """Gets the call_id of this AddToConference.  # noqa: E501

        ID of the Call that will be added to the specified Conference. The Call must be in progress or an error will result. If the Call is part of an existing Conference, it is first removed from that Conference and is then moved to the new one.  # noqa: E501

        :return: The call_id of this AddToConference.  # noqa: E501
        :rtype: bool
        """
        return self._call_id

    @call_id.setter
    def call_id(self, call_id):
        """Sets the call_id of this AddToConference.

        ID of the Call that will be added to the specified Conference. The Call must be in progress or an error will result. If the Call is part of an existing Conference, it is first removed from that Conference and is then moved to the new one.  # noqa: E501

        :param call_id: The call_id of this AddToConference.  # noqa: E501
        :type: bool
        """

        self._call_id = call_id

    @property
    def leave_conference_url(self):
        """Gets the leave_conference_url of this AddToConference.  # noqa: E501

        URL to be invoked when the Participant leaves the Conference.   # noqa: E501

        :return: The leave_conference_url of this AddToConference.  # noqa: E501
        :rtype: str
        """
        return self._leave_conference_url

    @leave_conference_url.setter
    def leave_conference_url(self, leave_conference_url):
        """Sets the leave_conference_url of this AddToConference.

        URL to be invoked when the Participant leaves the Conference.   # noqa: E501

        :param leave_conference_url: The leave_conference_url of this AddToConference.  # noqa: E501
        :type: str
        """

        self._leave_conference_url = leave_conference_url

    @property
    def listen(self):
        """Gets the listen of this AddToConference.  # noqa: E501

        If `true`, the Participant joins the Conference with listen privileges. This may be modified later via the REST API or `SetListen` PerCL command.  # noqa: E501

        :return: The listen of this AddToConference.  # noqa: E501
        :rtype: bool
        """
        return self._listen

    @listen.setter
    def listen(self, listen):
        """Sets the listen of this AddToConference.

        If `true`, the Participant joins the Conference with listen privileges. This may be modified later via the REST API or `SetListen` PerCL command.  # noqa: E501

        :param listen: The listen of this AddToConference.  # noqa: E501
        :type: bool
        """

        self._listen = listen

    @property
    def notification_url(self):
        """Gets the notification_url of this AddToConference.  # noqa: E501

        When the Participant enters the Conference, this URL will be invoked using an HTTP POST request with the standard request parameters.  # noqa: E501

        :return: The notification_url of this AddToConference.  # noqa: E501
        :rtype: str
        """
        return self._notification_url

    @notification_url.setter
    def notification_url(self, notification_url):
        """Sets the notification_url of this AddToConference.

        When the Participant enters the Conference, this URL will be invoked using an HTTP POST request with the standard request parameters.  # noqa: E501

        :param notification_url: The notification_url of this AddToConference.  # noqa: E501
        :type: str
        """

        self._notification_url = notification_url

    @property
    def start_conf_on_enter(self):
        """Gets the start_conf_on_enter of this AddToConference.  # noqa: E501

        Flag that indicates whether a Conference starts upon entry of this particular Participant. This is usually set to `true` for moderators and `false` for all other Participants.  # noqa: E501

        :return: The start_conf_on_enter of this AddToConference.  # noqa: E501
        :rtype: bool
        """
        return self._start_conf_on_enter

    @start_conf_on_enter.setter
    def start_conf_on_enter(self, start_conf_on_enter):
        """Sets the start_conf_on_enter of this AddToConference.

        Flag that indicates whether a Conference starts upon entry of this particular Participant. This is usually set to `true` for moderators and `false` for all other Participants.  # noqa: E501

        :param start_conf_on_enter: The start_conf_on_enter of this AddToConference.  # noqa: E501
        :type: bool
        """

        self._start_conf_on_enter = start_conf_on_enter

    @property
    def talk(self):
        """Gets the talk of this AddToConference.  # noqa: E501

        If `true`, the Participant joins the Conference with talk privileges. This may be modified later via the REST API or `SetTalk` PerCL command.   # noqa: E501

        :return: The talk of this AddToConference.  # noqa: E501
        :rtype: bool
        """
        return self._talk

    @talk.setter
    def talk(self, talk):
        """Sets the talk of this AddToConference.

        If `true`, the Participant joins the Conference with talk privileges. This may be modified later via the REST API or `SetTalk` PerCL command.   # noqa: E501

        :param talk: The talk of this AddToConference.  # noqa: E501
        :type: bool
        """

        self._talk = talk

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.to_camel_case(attr)
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
            elif value is None:
                continue
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
        if not isinstance(other, AddToConference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddToConference):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
