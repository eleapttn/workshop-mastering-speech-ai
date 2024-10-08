# NMT (Neural Machine Translation)

**Neural Machine Translation** is a subfield of machine translation that uses artificial neural networks to translate text from one language to another. This API offers multilingual models that translates the input text from a source language to a target language.

**[AI Endpoints](https://endpoints.ai.cloud.ovh.net/)** makes it easy to use it, with ready-to-use inference APIs. Indeed, the **NMT** API endpoint allows you to translate english written text to another language, in a few seconds.

![NMT](./images/NMT.png)

## How to use the NMT API Endpoint

The NMT API endpoint is based on an NMT model developed by [NVIDIA](https://www.nvidia.com/en-gb/). AI endpoints offers you a wide range of translations options for several languages (English, French, German, Spanish, and Chinese)).

The following example will allow you to translate text from **English** to **German**. It will return the translated text by the model.

```python

# Import the requests and os libraries into your notebook environment, if not already done
import requests
import os

# Specify the headers of your request 
# We will expect a JSON as the input and the output, since the NMT model will receive text, and generate text.
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('OVH_AI_ENDPOINTS_ACCESS_TOKEN')}",
}

# Specify the input data to be sent and translated
data = {
  "model": "en_de_24x6", # en_de allows the use of the English & German NMT model. Input can either be German/English, and the output will be the other one.
  "source_language": "en", # Input language will be English (language code: `en`)
  "target_language": "de", # Output language will be German (language code: `de`)
  "texts": ["This is the sentence I want to translate"]
}

# Send the request to the correct model endpoint and get response 
# We make sure to use the right endpoint, that targets the right model (English to German)
response = requests.post(
    os.getenv("NMT_EN_DE_ENDPOINT"),
    json=data,
    headers=headers
)

# Return translation
if response.status_code == 200:
    response_data = response.json()
    print("Translations:\n", response_data)
else:
    print("Error:", response.status_code)
```

## References

For more information about the NMT model features, please refer to RIVA NMT (documentation)[https://docs.nvidia.com/deeplearning/riva/user-guide/docs/translation/translation-overview.html].