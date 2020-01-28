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


class MessagesList(object):
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
        'total': 'int',
        'start': 'int',
        'end': 'int',
        'page': 'int',
        'num_pages': 'int',
        'page_size': 'int',
        'next_page_uri': 'str',
        'messages': 'list[MessageResult]'
    }

    attribute_map = {
        'total': 'total',
        'start': 'start',
        'end': 'end',
        'page': 'page',
        'num_pages': 'numPages',
        'page_size': 'pageSize',
        'next_page_uri': 'nextPageUri',
        'messages': 'messages'
    }

    def __init__(self, total=None, start=None, end=None, page=None, num_pages=None, page_size=None, next_page_uri=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """MessagesList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._start = None
        self._end = None
        self._page = None
        self._num_pages = None
        self._page_size = None
        self._next_page_uri = None
        self._messages = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if page is not None:
            self.page = page
        if num_pages is not None:
            self.num_pages = num_pages
        if page_size is not None:
            self.page_size = page_size
        if next_page_uri is not None:
            self.next_page_uri = next_page_uri
        if messages is not None:
            self.messages = messages

    @property
    def total(self):
        """Gets the total of this MessagesList.  # noqa: E501

        Total amount of requested resource.  # noqa: E501

        :return: The total of this MessagesList.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MessagesList.

        Total amount of requested resource.  # noqa: E501

        :param total: The total of this MessagesList.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def start(self):
        """Gets the start of this MessagesList.  # noqa: E501

        Resource index at start of current page  # noqa: E501

        :return: The start of this MessagesList.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this MessagesList.

        Resource index at start of current page  # noqa: E501

        :param start: The start of this MessagesList.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this MessagesList.  # noqa: E501

        Resource index at end of current page  # noqa: E501

        :return: The end of this MessagesList.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MessagesList.

        Resource index at end of current page  # noqa: E501

        :param end: The end of this MessagesList.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def page(self):
        """Gets the page of this MessagesList.  # noqa: E501

        Current page  # noqa: E501

        :return: The page of this MessagesList.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this MessagesList.

        Current page  # noqa: E501

        :param page: The page of this MessagesList.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def num_pages(self):
        """Gets the num_pages of this MessagesList.  # noqa: E501

        Total number of pages  # noqa: E501

        :return: The num_pages of this MessagesList.  # noqa: E501
        :rtype: int
        """
        return self._num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        """Sets the num_pages of this MessagesList.

        Total number of pages  # noqa: E501

        :param num_pages: The num_pages of this MessagesList.  # noqa: E501
        :type: int
        """

        self._num_pages = num_pages

    @property
    def page_size(self):
        """Gets the page_size of this MessagesList.  # noqa: E501

        Number of items per page  # noqa: E501

        :return: The page_size of this MessagesList.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this MessagesList.

        Number of items per page  # noqa: E501

        :param page_size: The page_size of this MessagesList.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def next_page_uri(self):
        """Gets the next_page_uri of this MessagesList.  # noqa: E501

        Uri to retrieve the next page of items  # noqa: E501

        :return: The next_page_uri of this MessagesList.  # noqa: E501
        :rtype: str
        """
        return self._next_page_uri

    @next_page_uri.setter
    def next_page_uri(self, next_page_uri):
        """Sets the next_page_uri of this MessagesList.

        Uri to retrieve the next page of items  # noqa: E501

        :param next_page_uri: The next_page_uri of this MessagesList.  # noqa: E501
        :type: str
        """

        self._next_page_uri = next_page_uri

    @property
    def messages(self):
        """Gets the messages of this MessagesList.  # noqa: E501

        Array of messages  # noqa: E501

        :return: The messages of this MessagesList.  # noqa: E501
        :rtype: list[MessageResult]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this MessagesList.

        Array of messages  # noqa: E501

        :param messages: The messages of this MessagesList.  # noqa: E501
        :type: list[MessageResult]
        """

        self._messages = messages

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
        if not isinstance(other, MessagesList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessagesList):
            return True

        return self.to_dict() != other.to_dict()
