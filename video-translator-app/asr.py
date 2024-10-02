# import dependencies
import os
import requests
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv('/workspace/.env')

# ASR function
def transcribe_audio(audio_input):

    # put audio file as endpoint input
    audio_file = [
        ('audio', open(audio_input, 'rb')),
    ]
    
    # get response from endpoint
    response = requests.post(
        os.environ.get('ASR_ENDPOINT'), 
        files=audio_file, 
        headers= {
            'accept': 'application/json',
            "Authorization": f"Bearer {os.environ.get('OVH_AI_ENDPOINTS_ACCESS_TOKEN')}",
        }
    )
    
    # return complete transcription
    output_asr = []
    if response.status_code == 200:
        
        for resp in response.json():
            
            output_sentence = []
    
            result = resp['alternatives'][0]
            output_sentence.append(result['transcript'])
            
            # extract sentence information
            for word in range(len(result['words'])):
                start_sentence = result['words'][0]['start_time']
                end_sentence = result['words'][word]['end_time']
            
            # add sart time and stop time of the sentence
            output_sentence.extend([start_sentence, end_sentence])
            output_asr.append(output_sentence)
    else:
        print("Error:", response.status_code)

    return output_asr