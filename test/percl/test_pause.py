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
from freeclimb.percl.pause import Pause  # noqa: E501
from freeclimb.rest import ApiException


class TestPause(unittest.TestCase):
    """Pause unit test stubs"""
    length=200

    def setUp(self):
        self.pause = Pause(length=self.length)

    def tearDown(self):
        pass

    def testPause(self):
        """Test Pause"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.Pause()  # noqa: E501
        self.assertTrue(isinstance(self.pause, Pause))
        self.assertEqual(self.length, self.pause.length)

    def testToDict(self):
        """Test Pause to dictionary"""
        self.assertTrue(isinstance(self.pause.to_dict(), dict))
        self.assertEqual(list(self.pause.to_dict().keys())[0], self.pause.__class__.__name__)


if __name__ == '__main__':
    unittest.main()