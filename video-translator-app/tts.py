# import dependencies
import os
import requests
from dotenv import load_dotenv
from moviepy.editor import *
from pydub import AudioSegment

# load environment variables from .env file
load_dotenv('/workspace/.env')

inputs_path = "/workspace/inputs"
outputs_path = "/workspace/outputs"

# voice dubbing in the new language
def add_audio_on_video(translated_audio, video_input, video_title):

    videoclip = VideoFileClip(video_input)
    audioclip = AudioFileClip(translated_audio)

    new_audioclip = CompositeAudioClip([audioclip])
    new_videoclip = f"{outputs_path}/videos/{video_title}.mp4"
    
    videoclip.audio = new_audioclip
    videoclip.write_videofile(new_videoclip)
    
    return new_videoclip


# TTS function
def synthetize_speech(output_nmt, video_input, video_title, voice_type):

    output_audio = 0
    output_audio_file = f"{outputs_path}/audios/{video_title}.wav"
    for sentence in range(len(output_nmt)):
        
        # add silence between audio sample
        if sentence==0:
            duration_silence = output_nmt[sentence][1]
        else:
            duration_silence = output_nmt[sentence][1] - output_nmt[sentence-1][2]
        silent_segment = AudioSegment.silent(duration = duration_silence)
        output_audio += silent_segment
        
        # create tts transcription
        data = {
            "encoding": 1,
            "language_code": "en-US",
            "sample_rate_hz": 16000,
            "text": output_nmt[sentence][0],
            "voice_name": f"English-US.{voice_type}"
        }
        
        # get response from endpoint
        response = requests.post(
            os.environ.get('TTS_ENDPOINT'), 
            json=data, 
            headers= {
                'accept': 'application/json',
                "Authorization": f"Bearer {os.environ.get('OVH_AI_ENDPOINTS_ACCESS_TOKEN')}",
            }
        )

        if response.status_code == 200:
            output_audio += AudioSegment(
            response.content,
            sample_width=2,
            frame_rate=16000,
            channels=1,
        )
        else:
            print("Error:", response.status_code)

    # export new audio as wav file
    output_audio.export(output_audio_file, format="wav")
    
    # add new voice on final video
    voice_dubbing = add_audio_on_video(output_audio_file, video_input, video_title)
    
    return voice_dubbing