# import dependencies
import os
import requests

# NMT function
def translate_text(output_asr):
    
    output_nmt = []
    for sentence in range(len(output_asr)):

        # put asr output as nmt input
        output_nmt.append(output_asr[sentence])
        data = {
            "model": "fr_en_24x6",
            "source_language": "fr",
            "target_language": "en",
            "texts": [output_asr[sentence][0]]
        }

       # get response from endpoint
        response = requests.post(
            os.environ.get('NMT_EN_FR_ENDPOINT'), 
            json=data, 
            headers= {
                'accept': 'application/json',
                "Authorization": f"Bearer {os.environ.get('OVH_AI_ENDPOINTS_ACCESS_TOKEN')}",
            }
        )
        if response.status_code == 200:
            output_nmt[sentence][0]=response.json()[0]['text']
        else:
            print("Error:", response.status_code)

        
    # return response
    return output_nmt