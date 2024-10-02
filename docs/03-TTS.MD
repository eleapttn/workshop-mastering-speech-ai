# TTS (Text-to-Speech)

**Text-to-Speech** is a subfield of Artificial Intelligence (AI) that converts written text into spoken words. This TTS API operates as a two-stage pipeline, with a first model generating a mel spectrogram, then a second model using this mel spectrogram to generate speech. This speech synthesis system enables you to synthesize natural speech from raw transcriptions without any additional information.

**[AI Endpoints](https://endpoints.ai.cloud.ovh.net/)** makes it easy to use it, with ready-to-use inference APIs. Indeed, the **(TTS)** API endpoint takes text as input and returns an audio file, in a few seconds.

![TTS](../images/TTS.png)

## How to use the TTS API Endpoint

The TTS API endpoint is based on an TTS model, developed by [NVIDIA](https://www.nvidia.com/en-gb/). AI endpoints offers you a wide range of speech generation options for several languages (English, German, Italian, Spanish, and Chinese). 

The following example will allow you to generate **english** speech audio files from english texts. We will then play the audio file in another cell code.

> :WARNING: **Don't forget to replace <ai_endpoint_token> by yours**
> **Make also sure to replace the `text_to_convert_to_speech` variable by the text you want to generate speech from!**

```python

# Import the requests library into your notebook environment if not already done
import requests

# Replace the default <YOUR_TOKEN> value by your AI Endpoints token.
ai_endpoint_token = "<ai_endpoint_token>"

# Specify the headers of your request 
# We will expect a JSON as the input since it is a text
# The output will be an application/octet-stream since the endpoint generates audio files (binary data format that can be read as a stream) 
headers = {
    "accept": "application/octet-stream",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ai_endpoint_token}",
}

# Specify the input data to be sent and converted to speech
data = {
    "text": "<text_to_convert_to_speech>", # text you want to generate speech from
    "language_code": "en-US", # language code of the generated speech (en-US for English)
    "encoding": 1,
    "sample_rate_hz": 16000,
    "voice_name": "English-US.Female-1" # or "English-US.male-1" for man voice
}

# Send the request to the correct model endpoint and get response 
# Here we use the "en-us" version, which is meant for generating English audio files.
response = requests.post(
    "https://nvr-tts-en-us.endpoints.kepler.ai.cloud.ovh.net/api/v1/tts/text_to_audio",
    json=data,
    headers=headers
)

# Get response from request 
if response.status_code == 200:
    response_data = response.content
else:
    print("Error:", response.status_code)

## How to read your generated audio file in a Media Player

Then, create another code cell to play your generated audio file:
    
```python
import IPython.display as ipd

# Show an audio player
ipd.Audio(response_data)
```
    

## References

For more information about the TTS model features, please refer to RIVA TTS (documentation)[https://docs.nvidia.com/deeplearning/riva/user-guide/docs/tts/tts-overview.html].