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
from freeclimb.percl.get_digits import GetDigits  # noqa: E501
from freeclimb.rest import ApiException


class TestGetDigits(unittest.TestCase):
    """GetDigits unit test stubs"""
    action_url='http://example.com'

    def setUp(self):
        self.get_digits = GetDigits(action_url=self.action_url)

    def tearDown(self):
        pass

    def testGetDigits(self):
        """Test GetDigits"""
        # construct object with mandatory attributes with example values
        # percl = freeclimb.percl.GetDigits()  # noqa: E501
        self.assertTrue(isinstance(self.get_digits, GetDigits))
        self.assertEqual(self.action_url, self.get_digits.action_url)
        self.assertTrue(hasattr(self.get_digits, 'initial_max_digits_ms'))
        self.assertTrue(hasattr(self.get_digits, 'finish_on_key'))
        self.assertTrue(hasattr(self.get_digits, 'digit_max_digits_ms'))
        self.assertTrue(hasattr(self.get_digits, 'min_digits'))
        self.assertTrue(hasattr(self.get_digits, 'max_digits'))
        self.assertTrue(hasattr(self.get_digits, 'flush_buffer'))
        self.assertTrue(hasattr(self.get_digits, 'prompts'))

    def testAddFinishOnKey(self):
        """Add FinishOnKey to conference"""
        finish_on_key_symbol = '*'
        self.get_digits.finish_on_key = finish_on_key_symbol
        self.assertEqual(self.get_digits.finish_on_key, finish_on_key_symbol)

    def testAddFinishOnKeyFail(self):
        """Fail to Add FinishOnKey to conference"""
        with self.assertRaises(ValueError):
            self.get_digits.finish_on_key = 'NotValidValue'

    def testToDict(self):
        """Test GetDigits to dictionary"""
        self.assertTrue(isinstance(self.get_digits.to_dict(), dict))
        self.assertEqual(list(self.get_digits.to_dict().keys())[0], self.get_digits.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
