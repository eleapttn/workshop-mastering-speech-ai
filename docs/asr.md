# ASR (Automatic Speech Recognition) API - English GB

The **Automatic Speech Recognition** (ASR) API endpoint allows you to recognize and transcribe audio, especially human speech, into text.

## Introduction

**Automatic Speech Recognition** (ASR) is a technology that converts spoken language into written text. It is a complex process that involves several stages, including speech signal
preprocessing, feature extraction, acoustic modeling, language modeling, and speech recognition engine.

AI Endpoints makes it easy, with ready-to-use inference APIs. Discover how to use them...

## Model concept

This ASR model was developed by NVIDIA. It takes audio stream or audio buffer as input and returns one or more text transcripts, along with additional optional metadata.

**Model configuration:**
- Transcription mode: offline
- Language Support: `en-GB`
- Audio type: `.mp3` / `.wav`

## How to?

ASR's AI endpoint offers you a wide range of transcription options for **english** (GB) audios. Learn how to use them with the following examples.

### Example

The first use case deals with a basic example that returns the sentence transcribed by the model.

> :WARNING: **Don't forget to replace <ai_endpoint_token> by yours**

```python
import io
import os
import requests

# headers
headers = headers = {
    'accept': 'application/json',
    "Authorization": f"Bearer <ai_endpoint_token>",
}

# put processed audio file as endpoint input
files = [
    ('audio', open('/workspace/audio_samples/audio_ovhcloud_en_0.wav', 'rb')),
]

# get response from endpoint
response = requests.post(
    "https://nvr-asr-en-gb.endpoints.kepler.ai.cloud.ovh.net/api/v1/asr/recognize", 
    files=files, 
    headers=headers
)

# return complete transcription
if response.status_code == 200:
    response_data = response.json()
    resp=''
    for alternative in response_data:
        resp+=alternative['alternatives'][0]['transcript']
    print("Audio transcription in english:\n", resp)
else:
    print("Error:", response.status_code)
```

## References

For more information about the ASR model features, please refer to RIVA ASR (documentation)[https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html].