# FreeClimb
FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 4.0.5
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.freeclimb.com/support/](https://www.freeclimb.com/support/)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://https://github.com/freeclimbapi/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://https://github.com/freeclimbapi/python-sdk.git`)

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

### Running Tests
Ensure the test dependencies have been installed

```sh
pip install -r test-requirements.txt
```

Run tests with command:
```sh
pytest
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import freeclimb
from pprint import pprint
from freeclimb.api.default_api import DefaultApi

from freeclimb.model.buy_incoming_number_request import BuyIncomingNumberRequest


# Defining the host is optional and defaults to https://www.freeclimb.com/apiserver
# See configuration.py for a list of all supported configuration parameters.
configuration = freeclimb.Configuration(
    host = "https://www.freeclimb.com/apiserver"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: fc
configuration = freeclimb.Configuration(
    username = 'ACCOUNT_ID',
    password = 'API_KEY'
)


# Enter a context with an instance of the API client
with freeclimb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = DefaultApi(api_client)
    buy_incoming_number_request = BuyIncomingNumberRequest(
        phone_number="phone_number_example",
        alias="alias_example",
        application_id="application_id_example",
    ) # BuyIncomingNumberRequest | Incoming Number transaction details
    

    try:
        # Buy a Phone Number
        api_response = api_instance.buy_a_phone_number(buy_incoming_number_request)
        pprint(api_response)
    except freeclimb.ApiException as e:
        print("Exception when calling DefaultApi->buy_a_phone_number: %s\n" % e)
```

## Documentation for PerCL

The Performance Command Language (PerCL) defines a set of instructions, written in JSON format, that express telephony actions to be performed in response to an event on the FreeClimb platform. FreeClimb communicates with the application server when events associated with the application occur, so the webserver can instruct FreeClimb how to handle such events using PerCL scripts.
PerCL commands are a part of the model schema and can be serialized into JSON like so:

```python
import freeclimb

say = freeclimb.Say(text='Hello, World')
play = freeclimb.Play(file='Example File')
get_digits = freeclimb.GetDigits(
    action_url='Example Action URL', prompts=[play, say])
percl_script = freeclimb.PerclScript(commands=[get_digits])

print(percl_script.to_json())
```

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
*DefaultApi* | [**list_applications**](docs/DefaultApi.md#list_applications) | **GET** /Accounts/{accountId}/Applications | List applications
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


## Documentation For Models

 - [AccountRequest](docs/AccountRequest.md)
 - [AccountResult](docs/AccountResult.md)
 - [AccountResultAllOf](docs/AccountResultAllOf.md)
 - [AddToConference](docs/AddToConference.md)
 - [AddToConferenceAllOf](docs/AddToConferenceAllOf.md)
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
 - [Capabilities](docs/Capabilities.md)
 - [ConferenceList](docs/ConferenceList.md)
 - [ConferenceListAllOf](docs/ConferenceListAllOf.md)
 - [ConferenceParticipantList](docs/ConferenceParticipantList.md)
 - [ConferenceParticipantListAllOf](docs/ConferenceParticipantListAllOf.md)
 - [ConferenceParticipantResult](docs/ConferenceParticipantResult.md)
 - [ConferenceParticipantResultAllOf](docs/ConferenceParticipantResultAllOf.md)
 - [ConferenceResult](docs/ConferenceResult.md)
 - [ConferenceResultAllOf](docs/ConferenceResultAllOf.md)
 - [CreateConference](docs/CreateConference.md)
 - [CreateConferenceAllOf](docs/CreateConferenceAllOf.md)
 - [CreateConferenceRequest](docs/CreateConferenceRequest.md)
 - [Dequeue](docs/Dequeue.md)
 - [Enqueue](docs/Enqueue.md)
 - [EnqueueAllOf](docs/EnqueueAllOf.md)
 - [FilterLogsRequest](docs/FilterLogsRequest.md)
 - [GetDigits](docs/GetDigits.md)
 - [GetDigitsAllOf](docs/GetDigitsAllOf.md)
 - [GetSpeech](docs/GetSpeech.md)
 - [GetSpeechAllOf](docs/GetSpeechAllOf.md)
 - [Hangup](docs/Hangup.md)
 - [HangupAllOf](docs/HangupAllOf.md)
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
 - [OutDial](docs/OutDial.md)
 - [OutDialAllOf](docs/OutDialAllOf.md)
 - [PaginationModel](docs/PaginationModel.md)
 - [Park](docs/Park.md)
 - [ParkAllOf](docs/ParkAllOf.md)
 - [Pause](docs/Pause.md)
 - [PauseAllOf](docs/PauseAllOf.md)
 - [PerclCommand](docs/PerclCommand.md)
 - [PerclScript](docs/PerclScript.md)
 - [Play](docs/Play.md)
 - [PlayAllOf](docs/PlayAllOf.md)
 - [PlayEarlyMedia](docs/PlayEarlyMedia.md)
 - [PlayEarlyMediaAllOf](docs/PlayEarlyMediaAllOf.md)
 - [QueueList](docs/QueueList.md)
 - [QueueListAllOf](docs/QueueListAllOf.md)
 - [QueueMember](docs/QueueMember.md)
 - [QueueMemberList](docs/QueueMemberList.md)
 - [QueueMemberListAllOf](docs/QueueMemberListAllOf.md)
 - [QueueRequest](docs/QueueRequest.md)
 - [QueueResult](docs/QueueResult.md)
 - [QueueResultAllOf](docs/QueueResultAllOf.md)
 - [RecordUtterance](docs/RecordUtterance.md)
 - [RecordUtteranceAllOf](docs/RecordUtteranceAllOf.md)
 - [RecordingList](docs/RecordingList.md)
 - [RecordingListAllOf](docs/RecordingListAllOf.md)
 - [RecordingResult](docs/RecordingResult.md)
 - [RecordingResultAllOf](docs/RecordingResultAllOf.md)
 - [Redirect](docs/Redirect.md)
 - [RedirectAllOf](docs/RedirectAllOf.md)
 - [Reject](docs/Reject.md)
 - [RejectAllOf](docs/RejectAllOf.md)
 - [RemoveFromConference](docs/RemoveFromConference.md)
 - [RemoveFromConferenceAllOf](docs/RemoveFromConferenceAllOf.md)
 - [Say](docs/Say.md)
 - [SayAllOf](docs/SayAllOf.md)
 - [SendDigits](docs/SendDigits.md)
 - [SendDigitsAllOf](docs/SendDigitsAllOf.md)
 - [SetListen](docs/SetListen.md)
 - [SetListenAllOf](docs/SetListenAllOf.md)
 - [SetTalk](docs/SetTalk.md)
 - [SetTalkAllOf](docs/SetTalkAllOf.md)
 - [Sms](docs/Sms.md)
 - [SmsAllOf](docs/SmsAllOf.md)
 - [StartRecordCall](docs/StartRecordCall.md)
 - [TerminateConference](docs/TerminateConference.md)
 - [TerminateConferenceAllOf](docs/TerminateConferenceAllOf.md)
 - [Unpark](docs/Unpark.md)
 - [UpdateCallRequest](docs/UpdateCallRequest.md)
 - [UpdateConferenceParticipantRequest](docs/UpdateConferenceParticipantRequest.md)
 - [UpdateConferenceRequest](docs/UpdateConferenceRequest.md)


## Documentation For Authorization


## fc

- **Type**: HTTP basic authentication


## Author

support@freeclimb.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in freeclimb.apis and freeclimb.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from freeclimb.api.default_api import DefaultApi`
- `from freeclimb.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import freeclimb
from freeclimb.apis import *
from freeclimb.models import *
```

