# FreeClimb

The FreeClimb Python SDK will allow you to easily use the FreeClimb API in a Python application.

## Requirements

Python 3.4+

## Installation & Usage

### pip install

```sh
pip install git+https://gitlab.vailsys.com/vail-cloud-services/fc-boilerplates/python-sdk.git
```

Then import the package:

```python
import freeclimb
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import freeclimb
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import freeclimb
from freeclimb.rest import ApiException
from pprint import pprint

configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = 'ACCOUNT_ID'
configuration.password = 'AUTH_TOKEN'

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"
# Create an instance of the API class
api_instance = freeclimb.DefaultApi(freeclimb.ApiClient(configuration))
buy_incoming_number_request = freeclimb.BuyIncomingNumberRequest() # BuyIncomingNumberRequest | Incoming Number transaction details (optional)

try:
    # Buy a Phone Number
    api_response = api_instance.buy_a_phone_number(buy_incoming_number_request=buy_incoming_number_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->buy_a_phone_number: %s\n" % e)

```

## Tests

Run tests with command:
```python -m unittest test```

## Documentation for API Endpoints

All URIs are relative to *https://www.freeclimb.com/apiserver*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**buy_a_phone_number**](docs/DefaultApi.md#buy_a_phone_number) | **POST** /Accounts/{accountId}/IncomingPhoneNumbers | Buy a Phone Number
*DefaultApi* | [**create_a_conference**](docs/DefaultApi.md#create_a_conference) | **POST** /Accounts/{accountId}/Conferences | Create a Conference
*DefaultApi* | [**create_a_queue**](docs/DefaultApi.md#create_a_queue) | **POST** /Accounts/{accountId}/Queues | Create a Queue
*DefaultApi* | [**create_an_application**](docs/DefaultApi.md#create_an_application) | **POST** /Accounts/{accountId}/Applications | Create an application
*DefaultApi* | [**delete_a_recording**](docs/DefaultApi.md#delete_a_recording) | **DELETE** /Accounts/{accountId}/Recordings/{recordingId} | Delete a Recording
*DefaultApi* | [**delete_an_application**](docs/DefaultApi.md#delete_an_application) | **DELETE** /Accounts/{accountId}/Applications/{applicationId} | Delete an application
*DefaultApi* | [**delete_an_incoming_number**](docs/DefaultApi.md#delete_an_incoming_number) | **DELETE** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Delete an Incoming Number
*DefaultApi* | [**dequeue_a_member**](docs/DefaultApi.md#dequeue_a_member) | **POST** /Accounts/{accountId}/Queues/{queueId}/Members/{callId} | Dequeue a Member
*DefaultApi* | [**dequeue_head_member**](docs/DefaultApi.md#dequeue_head_member) | **POST** /Accounts/{accountId}/Queues/{queueId}/Members/Front | Dequeue Head Member
*DefaultApi* | [**download_a_recording_file**](docs/DefaultApi.md#download_a_recording_file) | **GET** /Accounts/{accountId}/Recordings/{recordingId}/Download | Download a Recording File
*DefaultApi* | [**filter_logs**](docs/DefaultApi.md#filter_logs) | **POST** /Accounts/{accountId}/Logs | Filter Logs
*DefaultApi* | [**get_a_call**](docs/DefaultApi.md#get_a_call) | **GET** /Accounts/{accountId}/Calls/{callId} | Get a Call
*DefaultApi* | [**get_a_conference**](docs/DefaultApi.md#get_a_conference) | **GET** /Accounts/{accountId}/Conferences/{conferenceId} | Get a Conference
*DefaultApi* | [**get_a_member**](docs/DefaultApi.md#get_a_member) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members/{callId} | Get a Member
*DefaultApi* | [**get_a_participant**](docs/DefaultApi.md#get_a_participant) | **GET** /Accounts/{accountId}/Conferences/{conferenceId}/Participants/{callId} | Get a Participant
*DefaultApi* | [**get_a_queue**](docs/DefaultApi.md#get_a_queue) | **GET** /Accounts/{accountId}/Queues/{queueId} | Get a Queue
*DefaultApi* | [**get_a_recording**](docs/DefaultApi.md#get_a_recording) | **GET** /Accounts/{accountId}/Recordings/{recordingId} | Get a Recording
*DefaultApi* | [**get_an_account**](docs/DefaultApi.md#get_an_account) | **GET** /Accounts/{accountId} | Get an Account
*DefaultApi* | [**get_an_application**](docs/DefaultApi.md#get_an_application) | **GET** /Accounts/{accountId}/Applications/{applicationId} | Get an Application
*DefaultApi* | [**get_an_incoming_number**](docs/DefaultApi.md#get_an_incoming_number) | **GET** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Get an Incoming Number
*DefaultApi* | [**get_an_sms_message**](docs/DefaultApi.md#get_an_sms_message) | **GET** /Accounts/{accountId}/Messages/{messageId} | Get an SMS Message
*DefaultApi* | [**get_head_member**](docs/DefaultApi.md#get_head_member) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members/Front | Get Head Member
*DefaultApi* | [**list_active_queues**](docs/DefaultApi.md#list_active_queues) | **GET** /Accounts/{accountId}/Queues | List Active Queues
*DefaultApi* | [**list_all_account_logs**](docs/DefaultApi.md#list_all_account_logs) | **GET** /Accounts/{accountId}/Logs | List All Account Logs
*DefaultApi* | [**list_an_application**](docs/DefaultApi.md#list_an_application) | **GET** /Accounts/{accountId}/Applications | List applications
*DefaultApi* | [**list_available_numbers**](docs/DefaultApi.md#list_available_numbers) | **GET** /AvailablePhoneNumbers | List available numbers
*DefaultApi* | [**list_call_logs**](docs/DefaultApi.md#list_call_logs) | **GET** /Accounts/{accountId}/Calls/{callId}/Logs | List Call Logs
*DefaultApi* | [**list_call_recordings**](docs/DefaultApi.md#list_call_recordings) | **GET** /Accounts/{accountId}/Calls/{callId}/Recordings | List Call Recordings
*DefaultApi* | [**list_calls**](docs/DefaultApi.md#list_calls) | **GET** /Accounts/{accountId}/Calls | List Calls
*DefaultApi* | [**list_conferences**](docs/DefaultApi.md#list_conferences) | **GET** /Accounts/{accountId}/Conferences | List Conferences
*DefaultApi* | [**list_incoming_numbers**](docs/DefaultApi.md#list_incoming_numbers) | **GET** /Accounts/{accountId}/IncomingPhoneNumbers | List Incoming Numbers
*DefaultApi* | [**list_members**](docs/DefaultApi.md#list_members) | **GET** /Accounts/{accountId}/Queues/{queueId}/Members | List Members
*DefaultApi* | [**list_participants**](docs/DefaultApi.md#list_participants) | **GET** /Accounts/{accountId}/Conferences/{conferenceId}/Participants | List Participants
*DefaultApi* | [**list_recordings**](docs/DefaultApi.md#list_recordings) | **GET** /Accounts/{accountId}/Recordings | List Recordings
*DefaultApi* | [**list_sms_messages**](docs/DefaultApi.md#list_sms_messages) | **GET** /Accounts/{accountId}/Messages | List SMS Messages
*DefaultApi* | [**make_a_call**](docs/DefaultApi.md#make_a_call) | **POST** /Accounts/{accountId}/Calls | Make a Call
*DefaultApi* | [**remove_a_participant**](docs/DefaultApi.md#remove_a_participant) | **DELETE** /Accounts/{accountId}/Conferences/{conferenceId}/Participants/{callId} | Remove a Participant
*DefaultApi* | [**send_an_sms_message**](docs/DefaultApi.md#send_an_sms_message) | **POST** /Accounts/{accountId}/Messages | Send an SMS Message
*DefaultApi* | [**stream_a_recording_file**](docs/DefaultApi.md#stream_a_recording_file) | **GET** /Accounts/{accountId}/Recordings/{recordingId}/Stream | Stream a Recording File
*DefaultApi* | [**update_a_conference**](docs/DefaultApi.md#update_a_conference) | **POST** /Accounts/{accountId}/Conferences/{conferenceId} | Update a Conference
*DefaultApi* | [**update_a_live_call**](docs/DefaultApi.md#update_a_live_call) | **POST** /Accounts/{accountId}/Calls/{callId} | Update a Live Call
*DefaultApi* | [**update_a_participant**](docs/DefaultApi.md#update_a_participant) | **POST** /Accounts/{accountId}/Conferences/{conferenceId}/Participants/{callId} | Update a Participant
*DefaultApi* | [**update_a_queue**](docs/DefaultApi.md#update_a_queue) | **POST** /Accounts/{accountId}/Queues/{queueId} | Update a Queue
*DefaultApi* | [**update_an_account**](docs/DefaultApi.md#update_an_account) | **POST** /Accounts/{accountId} | Manage an account
*DefaultApi* | [**update_an_application**](docs/DefaultApi.md#update_an_application) | **POST** /Accounts/{accountId}/Applications/{applicationId} | Update an application
*DefaultApi* | [**update_an_incoming_number**](docs/DefaultApi.md#update_an_incoming_number) | **POST** /Accounts/{accountId}/IncomingPhoneNumbers/{phoneNumberId} | Update an Incoming Number

## Documentation for PerCL

The Performance Command Language (PerCL) defines a set of instructions, written in JSON format, that express telephony actions to be performed in response to an event on the FreeClimb platform. FreeClimb communicates with the application server when events associated with the application occur, so the webserver can instruct FreeClimb how to handle such events using PerCL scripts.

PerCL example:

```python
say = freeclimb.Say(text="Hello! This is a message sent using FreeClimb's Python SDK.")
return freeclimb.PerCLCommand.to_json(say.to_dict())
```

The JSON object below represents the PerCL object generated by the commands above.

```json
[
    {
        "Say" : {
            "text" : "Hello! This is a message sent using FreeClimb's Python SDK."
        }
    }
]
```

Class | Description
------------ | -------------
[**AddToConference**](https://docs.freeclimb.com/reference/conference-participants-1#addtoconference) | Add a Participant to a Conference
[**CreateConference**](https://docs.freeclimb.com/reference/conferences-2#createconference) | Creates a new conference with no Participants
[**Dequeue**](https://docs.freeclimb.com/reference/queue-members-1#dequeue) | Dequeue a Call that is in a Queue so the waiting Caller exits Queue
[**Enqueue**](https://docs.freeclimb.com/reference/queue-members-1#enqueue-1) | Adds a Call to a call Queue
[**GetDigits**](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#getdigits-1) | Collects DTMF inputs from the Caller
[**GetSpeech**](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#getspeech-1) | Allows the Caller to respond to the application using a supported language
[**Hangup**](https://docs.freeclimb.com/reference/calls#hangup) | Terminates a Call
[**OutDial**](https://docs.freeclimb.com/reference/calls#outdial-1) | Begin a Call to a phone number
[**Pause**](https://docs.freeclimb.com/reference/calls#pause) | Delays execution of PerCL script to create a Pause in the scenario
[**PlayEarlyMedia**](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#playearlymedia) | Plays an audio file before attempting to connect the Call
[**Play**](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#play) | Plays an audio file back to the Caller
[**RecordUtterance**](https://docs.freeclimb.com/reference/recordings-2#recordutterance) | Records the Caller's voice and returns the URL of a file containing the audio recording
[**Redirect**](https://docs.freeclimb.com/reference/calls#redirect-1) | Transfers Call to a different URL
[**RemoveFromConference**](https://docs.freeclimb.com/reference/conference-participants-1#removefromconference) | Removes a Participant from a Conference
[**Say**](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#say) | Provides Text-To-Speech (TTS) support
[**SendDigits**](https://docs.freeclimb.com/reference/calls#senddigits) | Plays DTMF tones on a live Call
[**SetListen**](https://docs.freeclimb.com/reference/conference-participants-1#setlisten) | Enables or disables the listening ability for a Conference Participant
[**SetTalk**](https://docs.freeclimb.com/reference/conference-participants-1#settalk) | Enables or disables the talking ability for a Conferencwe Participant
[**SMS**](https://docs.freeclimb.com/reference/sms-3#sms-4) | Sends an SMS message
[**StartRecordCall**](https://docs.freeclimb.com/reference/recordings-2#startrecordcall) | Records the current Call and returns the URL of a file containing the audio recording
[**TerminateConference**](https://docs.freeclimb.com/reference/conferences-2#terminateconference) | Terminates an existing Conference

## Documentation For Models

 - [AccountRequest](docs/AccountRequest.md)
 - [AccountResult](docs/AccountResult.md)
 - [AccountResultAllOf](docs/AccountResultAllOf.md)
 - [ApplicationList](docs/ApplicationList.md)
 - [ApplicationListAllOf](docs/ApplicationListAllOf.md)
 - [ApplicationRequest](docs/ApplicationRequest.md)
 - [ApplicationResult](docs/ApplicationResult.md)
 - [ApplicationResultAllOf](docs/ApplicationResultAllOf.md)
 - [AvailableNumber](docs/AvailableNumber.md)
 - [AvailableNumberList](docs/AvailableNumberList.md)
 - [AvailableNumberListAllOf](docs/AvailableNumberListAllOf.md)
 - [BuyIncomingNumberRequest](docs/BuyIncomingNumberRequest.md)
 - [CallList](docs/CallList.md)
 - [CallListAllOf](docs/CallListAllOf.md)
 - [CallResult](docs/CallResult.md)
 - [CallResultAllOf](docs/CallResultAllOf.md)
 - [ConferenceList](docs/ConferenceList.md)
 - [ConferenceListAllOf](docs/ConferenceListAllOf.md)
 - [ConferenceParticipantList](docs/ConferenceParticipantList.md)
 - [ConferenceParticipantListAllOf](docs/ConferenceParticipantListAllOf.md)
 - [ConferenceParticipantResult](docs/ConferenceParticipantResult.md)
 - [ConferenceParticipantResultAllOf](docs/ConferenceParticipantResultAllOf.md)
 - [ConferenceResult](docs/ConferenceResult.md)
 - [ConferenceResultAllOf](docs/ConferenceResultAllOf.md)
 - [CreateConferenceRequest](docs/CreateConferenceRequest.md)
 - [DequeueMemberRequest](docs/DequeueMemberRequest.md)
 - [FilterLogsRequest](docs/FilterLogsRequest.md)
 - [IncomingNumberList](docs/IncomingNumberList.md)
 - [IncomingNumberListAllOf](docs/IncomingNumberListAllOf.md)
 - [IncomingNumberRequest](docs/IncomingNumberRequest.md)
 - [IncomingNumberResult](docs/IncomingNumberResult.md)
 - [IncomingNumberResultAllOf](docs/IncomingNumberResultAllOf.md)
 - [LogList](docs/LogList.md)
 - [LogListAllOf](docs/LogListAllOf.md)
 - [LogResult](docs/LogResult.md)
 - [MakeCallRequest](docs/MakeCallRequest.md)
 - [MessageRequest](docs/MessageRequest.md)
 - [MessageRequestAllOf](docs/MessageRequestAllOf.md)
 - [MessageResult](docs/MessageResult.md)
 - [MessageResultAllOf](docs/MessageResultAllOf.md)
 - [MessagesList](docs/MessagesList.md)
 - [MessagesListAllOf](docs/MessagesListAllOf.md)
 - [MutableResourceModel](docs/MutableResourceModel.md)
 - [PaginationModel](docs/PaginationModel.md)
 - [QueueList](docs/QueueList.md)
 - [QueueListAllOf](docs/QueueListAllOf.md)
 - [QueueMember](docs/QueueMember.md)
 - [QueueMemberList](docs/QueueMemberList.md)
 - [QueueMemberListAllOf](docs/QueueMemberListAllOf.md)
 - [QueueRequest](docs/QueueRequest.md)
 - [QueueResult](docs/QueueResult.md)
 - [QueueResultAllOf](docs/QueueResultAllOf.md)
 - [RecordingList](docs/RecordingList.md)
 - [RecordingListAllOf](docs/RecordingListAllOf.md)
 - [RecordingResult](docs/RecordingResult.md)
 - [RecordingResultAllOf](docs/RecordingResultAllOf.md)
 - [UpdateCallRequest](docs/UpdateCallRequest.md)
 - [UpdateConferenceParticipantRequest](docs/UpdateConferenceParticipantRequest.md)
 - [UpdateConferenceRequest](docs/UpdateConferenceRequest.md)


## Documentation For Authorization


## fc

- **Type**: HTTP basic authentication


## Author




