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


class IncomingNumberResult(object):
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
        'phone_number_id': 'str',
        'account_id': 'str',
        'application_id': 'str',
        'phone_number': 'str',
        'alias': 'str',
        'region': 'str',
        'country': 'str',
        'voice_enabled': 'bool',
        'sms_enabled': 'bool'
    }

    attribute_map = {
        'uri': 'uri',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'revision': 'revision',
        'phone_number_id': 'phoneNumberId',
        'account_id': 'accountId',
        'application_id': 'applicationId',
        'phone_number': 'phoneNumber',
        'alias': 'alias',
        'region': 'region',
        'country': 'country',
        'voice_enabled': 'voiceEnabled',
        'sms_enabled': 'smsEnabled'
    }

    def __init__(self, uri=None, date_created=None, date_updated=None, revision=None, phone_number_id=None, account_id=None, application_id=None, phone_number=None, alias=None, region=None, country=None, voice_enabled=None, sms_enabled=None, local_vars_configuration=None):  # noqa: E501
        """IncomingNumberResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uri = None
        self._date_created = None
        self._date_updated = None
        self._revision = None
        self._phone_number_id = None
        self._account_id = None
        self._application_id = None
        self._phone_number = None
        self._alias = None
        self._region = None
        self._country = None
        self._voice_enabled = None
        self._sms_enabled = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if date_created is not None:
            self.date_created = date_created
        if date_updated is not None:
            self.date_updated = date_updated
        if revision is not None:
            self.revision = revision
        if phone_number_id is not None:
            self.phone_number_id = phone_number_id
        if account_id is not None:
            self.account_id = account_id
        if application_id is not None:
            self.application_id = application_id
        if phone_number is not None:
            self.phone_number = phone_number
        if alias is not None:
            self.alias = alias
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if voice_enabled is not None:
            self.voice_enabled = voice_enabled
        if sms_enabled is not None:
            self.sms_enabled = sms_enabled

    @property
    def uri(self):
        """Gets the uri of this IncomingNumberResult.  # noqa: E501

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :return: The uri of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this IncomingNumberResult.

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :param uri: The uri of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def date_created(self):
        """Gets the date_created of this IncomingNumberResult.  # noqa: E501

        The date that this account was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_created of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this IncomingNumberResult.

        The date that this account was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_created: The date_created of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this IncomingNumberResult.  # noqa: E501

        The date that this account was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_updated of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this IncomingNumberResult.

        The date that this account was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_updated: The date_updated of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._date_updated = date_updated

    @property
    def revision(self):
        """Gets the revision of this IncomingNumberResult.  # noqa: E501

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :return: The revision of this IncomingNumberResult.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this IncomingNumberResult.

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :param revision: The revision of this IncomingNumberResult.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def phone_number_id(self):
        """Gets the phone_number_id of this IncomingNumberResult.  # noqa: E501

        String that uniquely identifies this phone number resource.  # noqa: E501

        :return: The phone_number_id of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_id

    @phone_number_id.setter
    def phone_number_id(self, phone_number_id):
        """Sets the phone_number_id of this IncomingNumberResult.

        String that uniquely identifies this phone number resource.  # noqa: E501

        :param phone_number_id: The phone_number_id of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._phone_number_id = phone_number_id

    @property
    def account_id(self):
        """Gets the account_id of this IncomingNumberResult.  # noqa: E501

        ID of the account that owns this phone number.  # noqa: E501

        :return: The account_id of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this IncomingNumberResult.

        ID of the account that owns this phone number.  # noqa: E501

        :param account_id: The account_id of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def application_id(self):
        """Gets the application_id of this IncomingNumberResult.  # noqa: E501

        ID of the Application that FreeClimb should contact if a Call or SMS arrives for this phone number or a Call from this number is placed. An incoming phone number is not useful until associated with an applicationId.  # noqa: E501

        :return: The application_id of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this IncomingNumberResult.

        ID of the Application that FreeClimb should contact if a Call or SMS arrives for this phone number or a Call from this number is placed. An incoming phone number is not useful until associated with an applicationId.  # noqa: E501

        :param application_id: The application_id of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def phone_number(self):
        """Gets the phone_number of this IncomingNumberResult.  # noqa: E501

        Phone number in E.164 format.  # noqa: E501

        :return: The phone_number of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this IncomingNumberResult.

        Phone number in E.164 format.  # noqa: E501

        :param phone_number: The phone_number of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def alias(self):
        """Gets the alias of this IncomingNumberResult.  # noqa: E501

        Description for this phone number. Typically the conventionally-formatted version of the phone number.  # noqa: E501

        :return: The alias of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this IncomingNumberResult.

        Description for this phone number. Typically the conventionally-formatted version of the phone number.  # noqa: E501

        :param alias: The alias of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def region(self):
        """Gets the region of this IncomingNumberResult.  # noqa: E501

        State or province of this phone number.  # noqa: E501

        :return: The region of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this IncomingNumberResult.

        State or province of this phone number.  # noqa: E501

        :param region: The region of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """Gets the country of this IncomingNumberResult.  # noqa: E501

        Country of this phone number.  # noqa: E501

        :return: The country of this IncomingNumberResult.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IncomingNumberResult.

        Country of this phone number.  # noqa: E501

        :param country: The country of this IncomingNumberResult.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def voice_enabled(self):
        """Gets the voice_enabled of this IncomingNumberResult.  # noqa: E501

        Indicates whether the phone number can handle Calls. Typically set to true for all numbers.  # noqa: E501

        :return: The voice_enabled of this IncomingNumberResult.  # noqa: E501
        :rtype: bool
        """
        return self._voice_enabled

    @voice_enabled.setter
    def voice_enabled(self, voice_enabled):
        """Sets the voice_enabled of this IncomingNumberResult.

        Indicates whether the phone number can handle Calls. Typically set to true for all numbers.  # noqa: E501

        :param voice_enabled: The voice_enabled of this IncomingNumberResult.  # noqa: E501
        :type: bool
        """

        self._voice_enabled = voice_enabled

    @property
    def sms_enabled(self):
        """Gets the sms_enabled of this IncomingNumberResult.  # noqa: E501

        Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers.  # noqa: E501

        :return: The sms_enabled of this IncomingNumberResult.  # noqa: E501
        :rtype: bool
        """
        return self._sms_enabled

    @sms_enabled.setter
    def sms_enabled(self, sms_enabled):
        """Sets the sms_enabled of this IncomingNumberResult.

        Indication of whether the phone number can handle sending and receiving SMS messages. Typically set to true for all numbers.  # noqa: E501

        :param sms_enabled: The sms_enabled of this IncomingNumberResult.  # noqa: E501
        :type: bool
        """

        self._sms_enabled = sms_enabled

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
        if not isinstance(other, IncomingNumberResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncomingNumberResult):
            return True

        return self.to_dict() != other.to_dict()
