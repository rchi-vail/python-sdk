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


class AccountResultAllOf(object):
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
        'account_id': 'str',
        'api_key': 'str',
        'alias': 'str',
        'label': 'str',
        'type': 'str',
        'status': 'str',
        'subresource_uris': 'object'
    }

    attribute_map = {
        'account_id': 'accountId',
        'api_key': 'apiKey',
        'alias': 'alias',
        'label': 'label',
        'type': 'type',
        'status': 'status',
        'subresource_uris': 'subresourceUris'
    }

    def __init__(self, account_id=None, api_key=None, alias=None, label=None, type=None, status=None, subresource_uris=None, local_vars_configuration=None):  # noqa: E501
        """AccountResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._api_key = None
        self._alias = None
        self._label = None
        self._type = None
        self._status = None
        self._subresource_uris = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if api_key is not None:
            self.api_key = api_key
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
    def account_id(self):
        """Gets the account_id of this AccountResultAllOf.  # noqa: E501

        String that uniquely identifies this account resource.  # noqa: E501

        :return: The account_id of this AccountResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountResultAllOf.

        String that uniquely identifies this account resource.  # noqa: E501

        :param account_id: The account_id of this AccountResultAllOf.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def api_key(self):
        """Gets the api_key of this AccountResultAllOf.  # noqa: E501

        The API key assigned to this account. This token must be kept a secret by the customer.  # noqa: E501

        :return: The api_key of this AccountResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this AccountResultAllOf.

        The API key assigned to this account. This token must be kept a secret by the customer.  # noqa: E501

        :param api_key: The api_key of this AccountResultAllOf.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def alias(self):
        """Gets the alias of this AccountResultAllOf.  # noqa: E501

        A description for this account.  # noqa: E501

        :return: The alias of this AccountResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AccountResultAllOf.

        A description for this account.  # noqa: E501

        :param alias: The alias of this AccountResultAllOf.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def label(self):
        """Gets the label of this AccountResultAllOf.  # noqa: E501

        A string that identifies a category or group to which the account belongs.  # noqa: E501

        :return: The label of this AccountResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AccountResultAllOf.

        A string that identifies a category or group to which the account belongs.  # noqa: E501

        :param label: The label of this AccountResultAllOf.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this AccountResultAllOf.  # noqa: E501

        The type of this account. It is one of: trial or full.  # noqa: E501

        :return: The type of this AccountResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountResultAllOf.

        The type of this account. It is one of: trial or full.  # noqa: E501

        :param type: The type of this AccountResultAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this AccountResultAllOf.  # noqa: E501

        The status of this account. It is one of: active, suspended, or closed.  # noqa: E501

        :return: The status of this AccountResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountResultAllOf.

        The status of this account. It is one of: active, suspended, or closed.  # noqa: E501

        :param status: The status of this AccountResultAllOf.  # noqa: E501
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
        """Gets the subresource_uris of this AccountResultAllOf.  # noqa: E501

        The list of subresources for this account.  # noqa: E501

        :return: The subresource_uris of this AccountResultAllOf.  # noqa: E501
        :rtype: object
        """
        return self._subresource_uris

    @subresource_uris.setter
    def subresource_uris(self, subresource_uris):
        """Sets the subresource_uris of this AccountResultAllOf.

        The list of subresources for this account.  # noqa: E501

        :param subresource_uris: The subresource_uris of this AccountResultAllOf.  # noqa: E501
        :type: object
        """

        self._subresource_uris = subresource_uris

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
        if not isinstance(other, AccountResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountResultAllOf):
            return True

        return self.to_dict() != other.to_dict()

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
