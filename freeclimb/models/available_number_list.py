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


class AvailableNumberList(object):
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
        'available_phone_numbers': 'list[AvailableNumber]'
    }

    attribute_map = {
        'total': 'total',
        'start': 'start',
        'end': 'end',
        'page': 'page',
        'num_pages': 'numPages',
        'page_size': 'pageSize',
        'next_page_uri': 'nextPageUri',
        'available_phone_numbers': 'availablePhoneNumbers'
    }

    def __init__(self, total=None, start=None, end=None, page=None, num_pages=None, page_size=None, next_page_uri=None, available_phone_numbers=None, local_vars_configuration=None):  # noqa: E501
        """AvailableNumberList - a model defined in OpenAPI"""  # noqa: E501
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
        self._available_phone_numbers = None
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
        if available_phone_numbers is not None:
            self.available_phone_numbers = available_phone_numbers

    @property
    def total(self):
        """Gets the total of this AvailableNumberList.  # noqa: E501

        Total amount of requested resource.  # noqa: E501

        :return: The total of this AvailableNumberList.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AvailableNumberList.

        Total amount of requested resource.  # noqa: E501

        :param total: The total of this AvailableNumberList.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def start(self):
        """Gets the start of this AvailableNumberList.  # noqa: E501

        Resource index at start of current page  # noqa: E501

        :return: The start of this AvailableNumberList.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AvailableNumberList.

        Resource index at start of current page  # noqa: E501

        :param start: The start of this AvailableNumberList.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this AvailableNumberList.  # noqa: E501

        Resource index at end of current page  # noqa: E501

        :return: The end of this AvailableNumberList.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this AvailableNumberList.

        Resource index at end of current page  # noqa: E501

        :param end: The end of this AvailableNumberList.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def page(self):
        """Gets the page of this AvailableNumberList.  # noqa: E501

        Current page  # noqa: E501

        :return: The page of this AvailableNumberList.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AvailableNumberList.

        Current page  # noqa: E501

        :param page: The page of this AvailableNumberList.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def num_pages(self):
        """Gets the num_pages of this AvailableNumberList.  # noqa: E501

        Total number of pages  # noqa: E501

        :return: The num_pages of this AvailableNumberList.  # noqa: E501
        :rtype: int
        """
        return self._num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        """Sets the num_pages of this AvailableNumberList.

        Total number of pages  # noqa: E501

        :param num_pages: The num_pages of this AvailableNumberList.  # noqa: E501
        :type: int
        """

        self._num_pages = num_pages

    @property
    def page_size(self):
        """Gets the page_size of this AvailableNumberList.  # noqa: E501

        Number of items per page  # noqa: E501

        :return: The page_size of this AvailableNumberList.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AvailableNumberList.

        Number of items per page  # noqa: E501

        :param page_size: The page_size of this AvailableNumberList.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def next_page_uri(self):
        """Gets the next_page_uri of this AvailableNumberList.  # noqa: E501

        Uri to retrieve the next page of items  # noqa: E501

        :return: The next_page_uri of this AvailableNumberList.  # noqa: E501
        :rtype: str
        """
        return self._next_page_uri

    @next_page_uri.setter
    def next_page_uri(self, next_page_uri):
        """Sets the next_page_uri of this AvailableNumberList.

        Uri to retrieve the next page of items  # noqa: E501

        :param next_page_uri: The next_page_uri of this AvailableNumberList.  # noqa: E501
        :type: str
        """

        self._next_page_uri = next_page_uri

    @property
    def available_phone_numbers(self):
        """Gets the available_phone_numbers of this AvailableNumberList.  # noqa: E501


        :return: The available_phone_numbers of this AvailableNumberList.  # noqa: E501
        :rtype: list[AvailableNumber]
        """
        return self._available_phone_numbers

    @available_phone_numbers.setter
    def available_phone_numbers(self, available_phone_numbers):
        """Sets the available_phone_numbers of this AvailableNumberList.


        :param available_phone_numbers: The available_phone_numbers of this AvailableNumberList.  # noqa: E501
        :type: list[AvailableNumber]
        """

        self._available_phone_numbers = available_phone_numbers

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
        if not isinstance(other, AvailableNumberList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AvailableNumberList):
            return True

        return self.to_dict() != other.to_dict()
