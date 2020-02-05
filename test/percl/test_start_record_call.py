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
from freeclimb.percl.start_record_call import StartRecordCall  # noqa: E501
from freeclimb.rest import ApiException


class TestStartRecordCall(unittest.TestCase):
    """StartRecordCall unit test stubs"""

    def setUp(self):
        self.start_record_call = StartRecordCall()

    def tearDown(self):
        pass

    def testStartRecordCall(self):
        """Test StartRecordCall"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.start_record_call()  # noqa: E501
        self.assertTrue(isinstance(self.start_record_call, StartRecordCall))

    def testToDict(self):
        """Test StartRecordCall to dictionary"""
        self.assertTrue(isinstance(self.start_record_call.to_dict(), dict))
        self.assertEqual(list(self.start_record_call.to_dict().keys())[0], self.start_record_call.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
