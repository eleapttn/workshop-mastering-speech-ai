# Making API Requests to Speech AI Models

This first documentation is intended to give you all the elements you will need to make HTTP requests to the models we are going to use (ASR, NMT, TTS).

## Import libraries

To interact with the `ASR`, `NMT`, and `TTS` endpoints, you will need to import the `requests` and `os` libraries, which allows us to make `HTTP` requests and use environment variables:

```python
import requests
import os
```

You can copy and paste these first lines of code into an empty cell of the notebook.

## Define the headers of your request

The headers provide metadata about the **request**, **response**, and **message** being exchanged.

These headers will look like the following block code:

```python
headers = {
    "Content-Type": "application/json",
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ.get('OVH_AI_ENDPOINTS_ACCESS_TOKEN')}",
}
```

It is composed of 3 elements which are:
- `Content-Type` It describes the format of the input we will send to the model. Input data is model-dependent (ASR will expect an audio file as its input, while NMT a text).
- `accept` describes the format of the desired response content. Its **value will change** on the model we will use (`application/json` if we expect classic data, or `application/octet-stream` for generating audio files ...).
- `Authorization` allows to specify your AI Endpoints token, to authenticate your request. This token is already set in your AI Notebook so you won't have to change anything there.

Do not worry, you will find all the information you will need in the next documentations! 

## Send your request to the AI Model Endpoint

> :WARNING: **You will need to replace `MODEL_ENDPOINT_URL with the endpoint URL specific to the model you plan to use (ASR, NMT, TTS). These endpoints URL will be given in the next documentations.**

```python
response = requests.post(
    "MODEL_ENDPOINT_URL", 
    json=data,
    headers=headers
)
```

## Print the response of your request (model output):

```python
if response.status_code == 200:
    response_data = response.json()
    print("Response:", response_data)
else:
    print("Error:", response.status_code)
```

By following these steps, you should now be able to make your first requests to the Speech AI models! 

You can now go back to the `/notebooks/0_SPEECH_AI_BASICS.ipynb` file to start your discovery of Speech AI APIs! 