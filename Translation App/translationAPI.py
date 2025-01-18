import requests, uuid, json
import os
from dotenv import load_dotenv 

class Translate:

    def __init__(self):
        load_dotenv()

        self.key = os.getenv("TRANSLATOR_API_KEY")
        self.location = os.getenv("TRANSLATOR_REGION", "canadacentral")  # Defaults to "canadacentral" if not set in .env file
        self.endpoint = "https://api.cognitive.microsofttranslator.com"
        self.path = '/translate'
        self.constructed_url = self.endpoint + self.path
        self.chosen_lang = ''

        self.params = {
        'api-version': '3.0',
        'from': 'en',
        'to': self.chosen_lang
        }   

        self.headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def set_language(self, lang):
        '''
        Sets the language to translate to

        @param lang: the language to translate to
        @return: None
        '''
        languages = {'English' : 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Greek': 'el', 'Tagalog': 'fil'}

        self.chosen_lang = languages[lang]
        self.params['to'] = self.chosen_lang

    def translate_text(self, text):
        '''
        Translates the text to the chosen language

        @param text: the text to translate
        @return: the translated text
        '''
        #self.params['to'] = [self.languages[self.chosen_lang]]
        body = [{'text': text}] 
        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=body)
        response = request.json()
        to_return = (json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
        parsed_data = json.loads(to_return)
        return parsed_data[0]['translations'][0]['text']
    
    def get_languages(self):
        '''
        Gets the languages that can be translated to
        
        @param: None
        @return: the languages that can be translated to
        '''
        return self.languages.keys()
