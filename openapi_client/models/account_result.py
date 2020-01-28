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


class AccountResult(object):
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
        'account_id': 'str',
        'auth_token': 'str',
        'alias': 'str',
        'label': 'str',
        'type': 'str',
        'status': 'str',
        'subresource_uris': 'object'
    }

    attribute_map = {
        'uri': 'uri',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'revision': 'revision',
        'account_id': 'accountId',
        'auth_token': 'authToken',
        'alias': 'alias',
        'label': 'label',
        'type': 'type',
        'status': 'status',
        'subresource_uris': 'subresourceUris'
    }

    def __init__(self, uri=None, date_created=None, date_updated=None, revision=None, account_id=None, auth_token=None, alias=None, label=None, type=None, status=None, subresource_uris=None, local_vars_configuration=None):  # noqa: E501
        """AccountResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uri = None
        self._date_created = None
        self._date_updated = None
        self._revision = None
        self._account_id = None
        self._auth_token = None
        self._alias = None
        self._label = None
        self._type = None
        self._status = None
        self._subresource_uris = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if date_created is not None:
            self.date_created = date_created
        if date_updated is not None:
            self.date_updated = date_updated
        if revision is not None:
            self.revision = revision
        if account_id is not None:
            self.account_id = account_id
        if auth_token is not None:
            self.auth_token = auth_token
        if alias is not None:
            self.alias = alias
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if subresource_uris is not None:
            self.subresource_uris = subresource_uris

    @property
    def uri(self):
        """Gets the uri of this AccountResult.  # noqa: E501

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :return: The uri of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AccountResult.

        The URI for this resource, relative to /apiserver.  # noqa: E501

        :param uri: The uri of this AccountResult.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def date_created(self):
        """Gets the date_created of this AccountResult.  # noqa: E501

        The date that this account was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_created of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this AccountResult.

        The date that this account was created (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_created: The date_created of this AccountResult.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this AccountResult.  # noqa: E501

        The date that this account was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :return: The date_updated of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this AccountResult.

        The date that this account was last updated (GMT) in RFC 1123 format (e.g., Mon, 15 Jun 2009 20:45:30 GMT).  # noqa: E501

        :param date_updated: The date_updated of this AccountResult.  # noqa: E501
        :type: str
        """

        self._date_updated = date_updated

    @property
    def revision(self):
        """Gets the revision of this AccountResult.  # noqa: E501

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :return: The revision of this AccountResult.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this AccountResult.

        Revision count for the resource. This count is set to 1 on creation and is incremented every time it is updated.  # noqa: E501

        :param revision: The revision of this AccountResult.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def account_id(self):
        """Gets the account_id of this AccountResult.  # noqa: E501

        String that uniquely identifies this account resource.  # noqa: E501

        :return: The account_id of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountResult.

        String that uniquely identifies this account resource.  # noqa: E501

        :param account_id: The account_id of this AccountResult.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def auth_token(self):
        """Gets the auth_token of this AccountResult.  # noqa: E501

        The authorization token assigned to this account. This token must be kept a secret by the customer.  # noqa: E501

        :return: The auth_token of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this AccountResult.

        The authorization token assigned to this account. This token must be kept a secret by the customer.  # noqa: E501

        :param auth_token: The auth_token of this AccountResult.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def alias(self):
        """Gets the alias of this AccountResult.  # noqa: E501

        A description for this account.  # noqa: E501

        :return: The alias of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AccountResult.

        A description for this account.  # noqa: E501

        :param alias: The alias of this AccountResult.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def label(self):
        """Gets the label of this AccountResult.  # noqa: E501

        A string that identifies a category or group to which the account belongs.  # noqa: E501

        :return: The label of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AccountResult.

        A string that identifies a category or group to which the account belongs.  # noqa: E501

        :param label: The label of this AccountResult.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this AccountResult.  # noqa: E501

        The type of this account. It is one of: trial or full.  # noqa: E501

        :return: The type of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountResult.

        The type of this account. It is one of: trial or full.  # noqa: E501

        :param type: The type of this AccountResult.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this AccountResult.  # noqa: E501

        The status of this account. It is one of: active, suspended, or closed.  # noqa: E501

        :return: The status of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountResult.

        The status of this account. It is one of: active, suspended, or closed.  # noqa: E501

        :param status: The status of this AccountResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "suspended", "closed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subresource_uris(self):
        """Gets the subresource_uris of this AccountResult.  # noqa: E501

        The list of subresources for this account.  # noqa: E501

        :return: The subresource_uris of this AccountResult.  # noqa: E501
        :rtype: object
        """
        return self._subresource_uris

    @subresource_uris.setter
    def subresource_uris(self, subresource_uris):
        """Sets the subresource_uris of this AccountResult.

        The list of subresources for this account.  # noqa: E501

        :param subresource_uris: The subresource_uris of this AccountResult.  # noqa: E501
        :type: object
        """

        self._subresource_uris = subresource_uris

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
        if not isinstance(other, AccountResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountResult):
            return True

        return self.to_dict() != other.to_dict()
