# OVHcloud SPEECH AI WORKSHOP

*Master Speech AI APIs to enhance your applications!*

This workshop allows you to to **master Speech AI** by creating a **Video Translator** web app with [AI Endpoints](https://endpoints.ai.cloud.ovh.net/).

## Concept

By the end of this Hands-On Lab, you'll be able to:

    - Master Speech AI APIs, including Automatic Speech Recognition (ASR), Neural Machine Translation (NMT), and Text-to-Speech (TTS).
    - Transcribe audio or video recordings using ASR.
    - Translate transcribed text into another language using NMT.
    - Synthesize translated text using TTS to modify the spoken language of the original video.
    - Build a powerful web app that combines these steps, so you can subtitle and dub voices of any video !

![image](notebooks/images/speech-ai-puzzle.png)

## Get started with Speech AI

To get started with the workshop, open the `notebooks/0_SPEECH_AI_BASICS.ipynb` notebook to learn about Speech AI basics and see examples of how to use ASR, NMT, and TTS endpoints.

## Focus on key features

Once you've learned the basics of Speech AI, you'll learn about some key features that make it even more powerful. You will learn how to:

- Generate SRT files from ASR model output.
- Take silences into account during translation using the NMT model.
- Synthesize the translated text to voice dub the original video, using the TTS model.

## Build a video translator web app

Now it's time to put this knowledge into practice by building a **Video Translator web app**, which will integrate ASR, NMT, and TTS endpoints to enable you to transcribe, translate, and dub videos in real-time.

![image](notebooks/images/translator-web-app-archi.png)

- create the `.env` file:

```
ASR_ENDPOINT=https://nvr-asr-fr-fr.endpoints.kepler.ai.cloud.ovh.net/api/v1/asr/recognize
NMT_ENDPOINT=https://nvr-nmt-en-fr.endpoints.kepler.ai.cloud.ovh.net/api/v1/nmt/translate_text
TTS_ENDPOINT=https://nvr-tts-en-us.endpoints.kepler.ai.cloud.ovh.net/api/v1/tts/text_to_audio
OVH_AI_ENDPOINTS_ACCESS_TOKEN=<ai-endpoints-api-token>
```

## Deploy the app with OVHcloud AI Deploy

> Don't forget to add your environment file `.env` in your Path before building the Docker Image.

### 1. Create the Dockerfile

Create the `Dockerfile` as follow:

```
FROM python:3.11

WORKDIR /workspace
ADD . /workspace

RUN apt-get update && apt-get install -y ffmpeg libsndfile1-dev
RUN pip install -r requirements.txt

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace
CMD [ "python3" , "/workspace/main.py" ]
```

### 2. Build the Docker image:

Build the Docker image:

`docker build . -t speech-ai-video-translator-app:v1.0.0`

Tag and push the Docker image on Docker Hub:

`docker tag speech-ai-video-translator-app:v1.0.0 eleapttn/speech-ai-video-translator-app:v1.0.0`
`docker push eleapttn/speech-ai-video-translator-app:v1.0.0`

## 3. Launch Video Translator app

```
ovhai app run \                                    
    --name VideoTranslatorApp \
    --cpu 12 \
    --default-http-port 8000 \
    --volume standalone:/tmp/gradio:rw \
    --unsecure-http \
    eleapttn/speech-ai-video-translator-app:v1.0.0
```


