# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import freeclimb
from freeclimb.percl.reject import Reject  # noqa: E501
from freeclimb.rest import ApiException


class TestReject(unittest.TestCase):
    """Reject unit test stubs"""

    def setUp(self):
        self.reject = Reject()

    def tearDown(self):
        pass

    def testReject(self):
        """Test Reject"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.Reject()  # noqa: E501
        self.assertTrue(isinstance(self.reject, Reject))
        self.assertTrue(hasattr(self.reject, 'reason'))

if __name__ == '__main__':
    unittest.main()