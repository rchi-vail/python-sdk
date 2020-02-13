# Documentation for PerCL

The Performance Command Language (PerCL) defines a set of instructions, written in JSON format, that express telephony actions to be performed in response to an event on the FreeClimb platform. FreeClimb communicates with the application server when events associated with the application occur, so the webserver can instruct FreeClimb how to handle such events using PerCL scripts.

## PerCL example generation

```python
import freeclimb

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
[**Reject**](https://docs.freeclimb.com/reference/calls#reject) | The Reject command blocks an incoming Call.
[**RemoveFromConference**](https://docs.freeclimb.com/reference/conference-participants-1#removefromconference) | Removes a Participant from a Conference
[**Say**](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#say) | Provides Text-To-Speech (TTS) support
[**SendDigits**](https://docs.freeclimb.com/reference/calls#senddigits) | Plays DTMF tones on a live Call
[**SetListen**](https://docs.freeclimb.com/reference/conference-participants-1#setlisten) | Enables or disables the listening ability for a Conference Participant
[**SetTalk**](https://docs.freeclimb.com/reference/conference-participants-1#settalk) | Enables or disables the talking ability for a Conferencwe Participant
[**SMS**](https://docs.freeclimb.com/reference/sms-3#sms-4) | Sends an SMS message
[**StartRecordCall**](https://docs.freeclimb.com/reference/recordings-2#startrecordcall) | Records the current Call and returns the URL of a file containing the audio recording
[**TerminateConference**](https://docs.freeclimb.com/reference/conferences-2#terminateconference) | Terminates an existing Conference

## AddToConference

The AddToConference command adds a Participant to a Conference. If this Participant currently is in another Conference, the Participant is first removed from that Conference. Two Call legs can be bridged together by creating a Conference and adding both Call legs to it via AddToConference.

### Example:

```python
import freeclimb

addToConference = freeclimb.AddToConference(conference_id='CF_your_conference_id', call_id='CA_your_call_id')
return freeclimb.PerCLCommand.to_json(addToConference.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
conference_id | string | ID of the Conference to which to add the Participant (Call leg). Conference must exist or an error will result. | Required
call_id | string | ID of the Call that will be added to the specified Conference. The Call must be in progress or an error will result. | Required
start_conf_on_enter | boolean | Flag that indicates whether a Conference starts upon entry of this particular Participant. | Optional
talk | boolean | If true, the Participant joins the Conference with talk privileges. | Optional
listen | boolean | If true, the Participant joins the Conference with listen privileges. This may be modified later via the REST API or SetListen PerCL command. | Optional
allow_call_control | boolean | If true, Call control will be enabled for this Participant's Call leg. | Optional
call_control_sequence | string | Defines a sequence of digits that, when entered by this caller, invokes the call_control_url. Only digits plus '*', and '#' may be used. | Required only when allow_call_control is set to true
call_control_url | absolute URL | URL to be invoked when this Participant enters the digit sequence defined in the callControlSequence attribute. | Required only when allow_call_control is set to true
leave_conference_url | absolute URL | URL to be invoked when the Participant leaves the Conference via any of the following methods: RemoveFromConference,TerminateConference, Conference Participant API DELETE request, Conference API POST request with status=empty, Conference API POST request with status=terminated, Participant hangs up | optional
notification_url | absolute URL | When the Participant enters the Conference, this URL will be invoked using an HTTP POST request with the standard request parameters. |optional

## CreateConference

The CreateConference command does exactly what its name implies — it creates an unpopulated Conference (one without any Participants). Once created, a Conference remains in FreeClimb until explicitly terminated by a customer. Once a Conference has been terminated, it can no longer be used.

CreateConference is a terminal command (any actions following it are never executed). When the Conference is successfully created, FreeClimb invokes the provided actionUrl using an HTTP POST with a createConference Webhook as the body. After this request, control picks up using the PerCL code received in the response.

### Example:

```python
import freeclimb

conference = freeclimb.CreateConference(action_url='http://example.com/action', status_callback_url='http://example.com/status')
return freeclimb.PerCLCommand.to_json(conference.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
action_url | absolute URL | This URL is invoked once the Conference is successfully created. | Required
alias | string | Descriptive name for the Conference. | Optional
play_beep | **always**, **never**, **entryOnly**, or **exitOnly** | Indicates whether to play a beep when a Participant enters or leaves the Conference. | Optional
record | boolean | When set to true, the entire Conference is recorded. The statusCallbackUrl of the Conference will receive a conferenceRecordingEnded Webhook when the Conference transitions from the inProgress to empty state. | Optional
wait_url | absolute URL | If specified, this URL provides the custom hold music for the Conference when it is in the populated state. | Optional
status_callback_url | This URL is invoked when the status of the Conference changes or when a recording of the Conference has become available. | Optional

## Dequeue

The Dequeue command transfers control of a Call that is in a Queue so that the waiting caller exits the Queue. Execution continues with the first command in the PerCL script returned by the actionUrl specified in the Enqueue command.

### Example:

```python
import freeclimb

dequeue = freeclimb.Dequeue()
return freeclimb.PerCLCommand.to_json(dequeue.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
Dequeue does not support any attributes

## Enqueue

The Enqueue command adds the current Call to a call Queue. If the specified Queue does not exist, it is created and then the Call is added to it. The default maximum length of the queue is 100. This can be modified using the REST API.

### Example:

```python
import freeclimb

enqueue = freeclimb.Enqueue(queue_id='QU_your_queue_id', wait_url='http://example.com/wait', action_url='http://example.com/action')
return freeclimb.PerCLCommand.to_json(enqueue.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
queue_id | string | ID of the Queue to which to add the Call. If the Queue does not exist, it will be created. | Optional
action_url | absolute URL | A request is made to this URL when the Call leaves the Queue, which can occur if enqueue of the Call fails or when the call is dequeued via the Dequeue command, the REST API (POST to Queue Member resource), or the caller hangs up | Required
wait_url | absolute URL | Specifies a URL pointing to a PerCL script containing actions to be executed while the caller is waiting in the Queue. | Required
notification_url | absolute URL | URL to be invoked when the call enters the queue. | Optional

## GetDigits

### Example:

```python
import freeclimb

get_digits = freeclimb.GetDigits(action_url='http://example.com', max_digits=1, min_digits=1, flush_buffer=True)
return freeclimb.PerCLCommand.to_json(get_digits.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
action_url | absolute URL | | Required
initial_timeout_ms | integer > 0 | Maximum time in milliseconds that FreeClimb will wait for the Caller to press the first digit | Optional
digit_timeout_ms | integer > 0 | Maximum time in milliseconds that FreeClimb will wait for the Caller to press any digit after the last digit entered | Optional
finish_on_key | any digit, #, * | Digit that causes the input sequence to be deemed complete. | Optional
min_digits | integer >= 0 | Minimum number of digits expected in the input. | Optional
max_digits | integer >= 0 | Maximum number of digits expected in the input. | Optional
flush_buffer | boolean | If true, the FreeClimb platform starts with an empty DTMF buffer to store the digits entered by the caller. If false, FreeClimb will append the user inputs to the end of the existing digits buffer and will return digits from the start of the digits buffer. | Optional
prompts | PerCL command array | JSON array of PerCL commands to nest within the GetDigits command. | Optional
enforcePCI | boolean | Parameter enforcePCI obscures the result as required by PCI compliance. | Optional

## GetSpeech

The GetSpeech command enables the Caller to respond to the application using a supported language. Unlike DTMF entry, which implicitly restricts the user to using the available buttons on the phone key pad, speech input allows for flexible audio inputs based on grammar. FreeClimb supports grammars written using GRXML compatible with the Microsoft Speech Platform.

### Example:

```python
import freeclimb

get_speech = freeclimb.GetSpeech(action_url='http://example.com/action', grammar_type='BUILTIN', grammar_file='VERSAY_YESNO')
return freeclimb.PerCLCommand.to_json(get_speech.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
action_url | absolute URL | When the caller has finished speaking or the command has timed out, FreeClimb will make a POST request to this URL. | Required
grammar_type | **URL** or **BUILTIN** | The grammar file type to use for speech recognition. | optional
grammar_file | absolute URL or built-in grammar file | The grammar file to use for speech recognition. | Required
grammar_rule | string | The grammar rule within the specified grammar file to use for speech recognition. | Optional
play_beep | boolean | Indicates whether a beep should be played just before speech recognition is initiated so that the speaker can start to speak. | Optional
prompts | PerCL command array | The JSON array of PerCL commands to nest within the GetSpeech command. | Optional
no_input_timeout_ms | integer > 0 | When recognition is started and there is no speech detected for noInputTimeoutMs milliseconds, the recognizer will terminate the recognition operation. | Optional
recognition_timeout_ms | integer > 0 | When playback of prompts ends and there is no match for recognitionTimeoutMs milliseconds, the recognizer will terminate the recognition operation. | Optional
confidence_threshold | float range 0.0-1.0 | When a recognition resource recognizes a spoken phrase, it associates a confidence level with that match. Parameter confidenceThreshold specifies what confidence level is considered a successful match. | Optional
sensitivity_level | float range 0.0-1.0 | The speech recognizer supports a variable level of sound sensitivity. | Optional
speech_complete_timeout_ms | integer > 0 | Specifies the length of silence required following user speech before the speech recognizer finalizes a result. | optional
speech_incomplete_timeout_ms | integer > 0 | Specifies the length of silence following user speech after which a recognizer finalizes a result. | optional
enforcePCI | boolean | Parameter enforcePCI will not log the 'text' as required by PCI compliance. | optional

## Hangup

The Hangup command terminates a Call. If Hangup is used as the first action in a PerCL response, it does not prevent FreeClimb from answering the Call and billing your account. See the Reject command to hang up at no charge.

### Example:

```python
import freeclimb

hangup = freeclimb.Hangup()
return freeclimb.PerCLCommand.to_json(hangup.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
call_id | string | The ID of the Call leg to hang up. If not specified, the Call leg corresponding to the current PerCL execution context hangs up. | Optional
reason | string | The user defined reason for the hangup. In general, applications should use a set of enumerated values that are predefined to cover all exit points of the Call flows for the given application. | Optional

## OutDial

The OutDial command is used to call a phone number.

### Example:

```python
import freeclimb

outdial = freeclimb.OutDial(action_url='http://example.com/action', call_connect_url='http://example.com/action', calling_number='+1XXXXXXXXXX', destination='+1XXXXXXXXXX')
return freeclimb.PerCLCommand.to_json(outdial.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
action_url | absolute URL | URL to which FreeClimb sends an HTTP POST request (an outDialStart Webhook immediately when the OutDial command executes. | Required
call_connect_url | absolute URL | URL to which FreeClimb makes an HTTP POST request informing the result of the OutDial. | Required
calling_number | E.164 phone number | The caller ID to show to the called party when FreeClimb calls. | Required
destination | E.164 phone number | E.164 representation of the phone number to Call. | Required
if_machine | `redirect` or `hangup` | Specifies how FreeClimb should handle this OutDial if an answering machine answers the Call. | Optional
if_machine_url | absolute URL | When the ifMachine flag is set to redirect, this attribute specifies a URL to which FreeClimb makes a POST request when an answering machine or a fax machine is detected. | Optional
send_digits | digits 0-9, # or * | DTMF tones to play to the outdialed Call. This is typically used to dial a number and then dial an extension. | Optional
status_callback_url | absolute URL | When the outdialed Call leg terminates, FreeClimb sends a callStatus Webhook to the statusCallbackUrl. | Optional
timeout | integer > 0 | Maximum time in seconds the OutDial command waits for the called party to answer the Call. | Optional

## Pause

The Pause command halts execution of the current PerCL script for a specified number of milliseconds.

### Example:

```python
import freeclimb

pause = freeclimb.Pause(length=3500)
return freeclimb.PerCLCommand.to_json(pause.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
length | integer > 0 | Length in ***milliseconds*** FreeClimb will wait silently before continuing on.

## PlayEarlyMedia

PlayEarlyMedia is relevant only when present as the very first command in the PerCL script returned for an incoming Call. In such cases, the command is executed before FreeClimb attempts to connect the call. The audio file it uses can be stored in any location that is accessible via URL.

### Example:

```python
import freeclimb

play_early_media = freeclimb.PlayEarlyMedia(file='http://example.com/greeting.wav')
return freeclimb.PerCLCommand.to_json(play_early_media.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
file | string | URL of the audio file to be played to the caller. The URL can be the recordingUrl generated from the RecordUtterance or StartRecordCall PerCL commands or any accessible URL. | required

## Play

The Play command plays an audio file back to the caller. The audio file may be located at any location accessible via a URL. Play can exist as a stand-alone command or as a nested command. It does not allow barge-in unless nested within a GetSpeech command. The file will always be played to completion unless nested.

### Example:

```python
import freeclimb

play = freeclimb.Play(file='http://example.com/greeting.wav')
return freeclimb.PerCLCommand.to_json(play.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
file | string | URL of the audio file to be played to the caller. The URL can be the recordingUrl generated from the RecordUtterance or StartRecordCall PerCL commands or any accessible URL. | Required
loop | integer >=0 | Number of times the audio file is played. Specifying '0' causes the Play action to loop until the Call is hung up. | Optional
conference_id | ID of the Conference the audio should be rendered to.

## RecordUtterance

The RecordUtterance command records the caller's voice and returns the URL of a file containing the audio recording.

### Example:

```python
import freeclimb

record_utterance = freeclimb.RecordUtterance(action_url='http://example.com', play_beep=True, finish_on_key='1')
return freeclimb.PerCLCommand.to_json(record_utterance.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
action_url | absolute URL | URL to which information on the completed recording is submitted. | Required
silence_timeout_ms | integer > 0 | Interval of silence that should elapse before ending the recording. | Optional
finish_on_key | any digit, #, * | Key that triggers the end of the recording. | Optional
max_length_sec | integer > 1 | Maximum length for the command execution in seconds. | Optional
play_beep | boolean | Indicates whether to play a beep sound before the start of the recording. | Optional
auto_start | boolean | If false, recording begins immediately after the RecordUtterance command is processed. If true, recording begins when audio is present and if audio begins before the max_length_sec timeout. | Optional

## Redirect

The Redirect command transfers control of a Call to the PerCL at a different URL.

### Example:

```python
import freeclimb

redirect = freeclimb.Redirect(action_url='http://example.com')
return freeclimb.PerCLCommand.to_json(redirect.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
action_url | absolute URL | URL to request a new PerCL script to continue with the current Call's processing. | Required

## Reject

The Reject command blocks an incoming Call.

### Example:

```python
import freeclimb

reject = freeclimb.Reject()
return freeclimb.PerCLCommand.to_json(reject.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
reason | string | Reason for the rejection. | Optional

## RemoveFromConference

The RemoveFromConference command removes a Participant from a Conference but does not hang up.

### Example:

```python
import freeclimb

remove_from_conference = freeclimb.RemoveFromConference(call_id='CA_your_call_id')
return freeclimb.PerCLCommand.to_json(remove_from_conference.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
call_id | string | ID of the Call leg to be removed from the Conference. The Call must be in a Conference or an error will be triggered. | Required

## Say

The Say command provides Text-To-Speech (TTS) support. It converts text to speech and then renders it in a female voice back to the caller. Say is useful in cases where it's difficult to pre-record a prompt for any reason. Say does not allow barge-in unless nested within a GetSpeech command. The file will always be played to completion unless nested.

### Example:

```python
import freeclimb

say = freeclimb.Say(text="Hello! This is a message sent using FreeClimb's Python SDK.")
return freeclimb.PerCLCommand.to_json(say.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
text | string | The message to be played to the caller using TTS. | Required
loop | integer >=0 | Number of times the text is said. Specifying '0' causes the Say action to loop until the Call is hung up. | Optional
language |[See table for list of options](https://docs.freeclimb.com/reference/interactive-voice-response-ivr#say)| Language and (by implication) the locale to use. This implies the accent and pronunciations to be used for the TTS. Default is `en-ES` for English (United States) | Optional
conference_id | string | ID of the Conference the speech should be rendered to. | Optional
enforcePCI | boolean | Parameter enforcePCI will not log the 'text' as required by PCI compliance. | Optional

## SendDigits

The SendDigits command plays DTMF tones on a live Call.

### Example:

```python
import freeclimb

send_digits = freeclimb.SendDigits(digits='1234#')
return freeclimb.PerCLCommand.to_json(send_digits.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
digits | string | String containing the digits to be played. | Required
pause_ms | integer 100-1000 | Pause between digits in milliseconds. | Optional

## SetListen

The SetListen command enables or disables the listen privilege for a Conference Participant provided both calls are in the same conference. The Participant can hear what the other participants are saying only if this privilege is enabled.

### Example:

```python
import freeclimb

set_listen = freeclimb.SetListen(call_id='CA-call-id', set_listen=False)
return freeclimb.PerCLCommand.to_json(set_listen.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
call_id | string | ID of the call leg that is to be assigned the listen privilege. The Call must be in a Conference or an error will be triggered. | Required
listen | boolean | Specifying false will silence the Conference for this Participant. Default `True` | Optional

## SetTalk

The SetTalk command enables or disables the talk privilege for a Conference Participant provided both calls are in the same conference. If `False`, no audio from that Participant is shared with the other Participants of the Conference.

### Example:

```python
import freeclimb

set_talk = freeclimb.SetTalk(call_id='CA-call-id', set_talk=False)
return freeclimb.PerCLCommand.to_json(set_talk.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
call_id | string | ID of the call leg that is to be assigned the talk privilege. The Call must be in a Conference or an error will be triggered. | Required
talk | boolean | Specifying `False` mutes this Participant. | Optional

## Sms

The Sms command can be used to send an SMS message to a phone number during a phone call.

### Example:

```python
import freeclimb

sms = freeclimb.Sms(to='+1XXXXXXXXXX', from_number='+1XXXXXXXXXX', text='Hello! This is a message sent using FreeClimb's Python SDK.', notification_url='http://example.com/notificationUrl')
return freeclimb.PerCLCommand.to_json(sms.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
to_number | string | E.164 representation of the phone number to which the message will be sent. Must be within FreeClimb's service area | Required
from_number | string | E.164 representation of the phone number to use as the sender. This must be an incoming phone number you have purchased from FreeClimb. | Required
text | string | Text contained in the message (maximum 160 characters). | Required
notification_url | absolute URL | When the message changes status, this URL will be invoked using HTTP POST with the messageStatus parameters. | Optional

## StartRecordCall

The StartRecordCall command records the current call and returns the URL of a file containing the audio recording when recording completes.

### Example:

```python
import freeclimb

start_record_call = freeclimb.StartRecordCall()
return freeclimb.PerCLCommand.to_json(start_record_call.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
StartRecordCall does not support any attributes

## TerminateConference

The TerminateConference command terminates an existing Conference. Any active participants are hung up on by FreeClimb. If this is not the desired behavior, use the RemoveFromConference command to unbridge Calls that should not be hung up.

### Example:

```python
import freeclimb

terminate_conference = freeclimb.TerminateConference(conference_id='CF-your-conference-id')
return freeclimb.PerCLCommand.to_json(terminate_conference.to_dict())
```

### Attributes:

Name | Type | Description | Required
------------ | ------------- | ------------- | -------------
conference_id | string | ID of the conference to terminate. | Required