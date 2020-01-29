# coding: utf-8

"""
    FreeClimb API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_buy_a_phone_number(self):
        """Test case for buy_a_phone_number

        Buy a Phone Number  # noqa: E501
        """
        pass

    def test_create_a_conference(self):
        """Test case for create_a_conference

        Create a Conference  # noqa: E501
        """
        pass

    def test_create_a_queue(self):
        """Test case for create_a_queue

        Create a Queue  # noqa: E501
        """
        pass

    def test_create_an_application(self):
        """Test case for create_an_application

        Create an application  # noqa: E501
        """
        pass

    def test_delete_a_recording(self):
        """Test case for delete_a_recording

        Delete a Recording  # noqa: E501
        """
        pass

    def test_delete_an_application(self):
        """Test case for delete_an_application

        Delete an application  # noqa: E501
        """
        pass

    def test_delete_an_incoming_number(self):
        """Test case for delete_an_incoming_number

        Delete an Incoming Number  # noqa: E501
        """
        pass

    def test_dequeue_a_member(self):
        """Test case for dequeue_a_member

        Dequeue a Member  # noqa: E501
        """
        pass

    def test_dequeue_head_member(self):
        """Test case for dequeue_head_member

        Dequeue Head Member  # noqa: E501
        """
        pass

    def test_download_a_recording_file(self):
        """Test case for download_a_recording_file

        Download a Recording File  # noqa: E501
        """
        pass

    def test_filter_logs(self):
        """Test case for filter_logs

        Filter Logs  # noqa: E501
        """
        pass

    def test_get_a_call(self):
        """Test case for get_a_call

        Get a Call  # noqa: E501
        """
        pass

    def test_get_a_conference(self):
        """Test case for get_a_conference

        Get a Conference  # noqa: E501
        """
        pass

    def test_get_a_member(self):
        """Test case for get_a_member

        Get a Member  # noqa: E501
        """
        pass

    def test_get_a_participant(self):
        """Test case for get_a_participant

        Get a Participant  # noqa: E501
        """
        pass

    def test_get_a_queue(self):
        """Test case for get_a_queue

        Get a Queue  # noqa: E501
        """
        pass

    def test_get_a_recording(self):
        """Test case for get_a_recording

        Get a Recording  # noqa: E501
        """
        pass

    def test_get_an_account(self):
        """Test case for get_an_account

        Get an Account  # noqa: E501
        """
        pass

    def test_get_an_application(self):
        """Test case for get_an_application

        Get an Application  # noqa: E501
        """
        pass

    def test_get_an_incoming_number(self):
        """Test case for get_an_incoming_number

        Get an Incoming Number  # noqa: E501
        """
        pass

    def test_get_an_sms_message(self):
        """Test case for get_an_sms_message

        Get an SMS Message  # noqa: E501
        """
        pass

    def test_get_head_member(self):
        """Test case for get_head_member

        Get Head Member  # noqa: E501
        """
        pass

    def test_list_active_queues(self):
        """Test case for list_active_queues

        List Active Queues  # noqa: E501
        """
        pass

    def test_list_all_account_logs(self):
        """Test case for list_all_account_logs

        List All Account Logs  # noqa: E501
        """
        pass

    def test_list_an_application(self):
        """Test case for list_an_application

        List applications  # noqa: E501
        """
        pass

    def test_list_available_numbers(self):
        """Test case for list_available_numbers

        List available numbers  # noqa: E501
        """
        pass

    def test_list_call_logs(self):
        """Test case for list_call_logs

        List Call Logs  # noqa: E501
        """
        pass

    def test_list_call_recordings(self):
        """Test case for list_call_recordings

        List Call Recordings  # noqa: E501
        """
        pass

    def test_list_calls(self):
        """Test case for list_calls

        List Calls  # noqa: E501
        """
        pass

    def test_list_conferences(self):
        """Test case for list_conferences

        List Conferences  # noqa: E501
        """
        pass

    def test_list_incoming_numbers(self):
        """Test case for list_incoming_numbers

        List Incoming Numbers  # noqa: E501
        """
        pass

    def test_list_members(self):
        """Test case for list_members

        List Members  # noqa: E501
        """
        pass

    def test_list_participants(self):
        """Test case for list_participants

        List Participants  # noqa: E501
        """
        pass

    def test_list_recordings(self):
        """Test case for list_recordings

        List Recordings  # noqa: E501
        """
        pass

    def test_list_sms_messages(self):
        """Test case for list_sms_messages

        List SMS Messages  # noqa: E501
        """
        pass

    def test_make_a_call(self):
        """Test case for make_a_call

        Make a Call  # noqa: E501
        """
        pass

    def test_remove_a_participant(self):
        """Test case for remove_a_participant

        Remove a Participant  # noqa: E501
        """
        pass

    def test_send_an_sms_message(self):
        """Test case for send_an_sms_message

        Send an SMS Message  # noqa: E501
        """
        pass

    def test_stream_a_recording_file(self):
        """Test case for stream_a_recording_file

        Stream a Recording File  # noqa: E501
        """
        pass

    def test_update_a_conference(self):
        """Test case for update_a_conference

        Update a Conference  # noqa: E501
        """
        pass

    def test_update_a_live_call(self):
        """Test case for update_a_live_call

        Update a Live Call  # noqa: E501
        """
        pass

    def test_update_a_participant(self):
        """Test case for update_a_participant

        Update a Participant  # noqa: E501
        """
        pass

    def test_update_a_queue(self):
        """Test case for update_a_queue

        Update a Queue  # noqa: E501
        """
        pass

    def test_update_an_account(self):
        """Test case for update_an_account

        Manage an account  # noqa: E501
        """
        pass

    def test_update_an_application(self):
        """Test case for update_an_application

        Update an application  # noqa: E501
        """
        pass

    def test_update_an_incoming_number(self):
        """Test case for update_an_incoming_number

        Update an Incoming Number  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()