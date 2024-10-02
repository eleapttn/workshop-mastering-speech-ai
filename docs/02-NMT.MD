# NMT (Neural Machine Translation)

**Neural Machine Translation** is a subfield of machine translation that uses artificial neural networks to translate text from one language to another. This API offers multilingual models that translates the input text from a source language to a target language.

**[AI Endpoints](https://endpoints.ai.cloud.ovh.net/)** makes it easy to use it, with ready-to-use inference APIs. Indeed, the **NMT** API endpoint allows you to translate english written text to another language, in a few seconds.

![NMT](../images/NMT.png)

## How to use the NMT API Endpoint

The NMT API endpoint is based on an NMT model developed by [NVIDIA](https://www.nvidia.com/en-gb/). AI endpoints offers you a wide range of translations options for several languages (English to {French, German, Spanish, and Chinese}).

The following example will allow you to translate text from **english** to **German**. It will return the translated text by the model.

> :WARNING: **Don't forget to replace <ai_endpoint_token> by yours**

```python

# Import the requests library into your notebook environment if not already done
import requests

# Replace the default <YOUR_TOKEN> value by your AI Endpoints token.
ai_endpoint_token = "<ai_endpoint_token>"

# Specify the headers of your request 
# We will expect a JSON as the input and the output, since the NMT model will receive text, and generate text.
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ai_endpoint_token}",
}

# Specify the input data to be sent and translated
data = {
  "model": "en_fr_24x6", # en_de allows the use of the English to French NMT model
  "source_language": "en", # Input language will be English (language code: `en`)
  "target_language": "fr", # Input language will be French (language code: `fr`)
  "texts": ["This is the sentence I want to translate"]
}

# Send the request to the correct model endpoint and get response 
# We make sure to use the right endpoint, that targets the right model (English to French)
response = requests.post(
    "https://nvr-nmt-en-fr.endpoints.kepler.ai.cloud.ovh.net/api/v1/nmt/translate_text", 
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