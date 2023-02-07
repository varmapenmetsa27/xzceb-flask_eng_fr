import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from dotenv import dotenv_values

config = dotenv_values(".env")

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

######
## Function To Translate English to French
#######

def english_to_french(english_text):
    ###write the code here
    translation = language_translator.translate(
    text=english_text,
    source='en',target='fr'
    ).get_result()
    return translation['translations'][0]['translation']
TEXT = "Hello"
print(english_to_french(TEXT))

######
## Function To Translate French to Text
#######

def french_to_english(french_text):
    ###write the code here
    translation = language_translator.translate(
    text=french_text,
    source='fr',target='en'
    ).get_result()
    return translation['translations'][0]['translation']
TEXT = "Bonjour"
print(french_to_english(TEXT))