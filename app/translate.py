import requests
from flask import current_app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return 'Error: the translation service is not configured.'
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
            'Ocp-Apim-Subscription-Region': 'westeurope'}

    data = [
        {"Text": text}
    ]
    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(
                         source_language, dest_language),
                     headers=auth, json=data)
    if r.status_code != 200:
        return 'Error: the translation service failed.'
    data = r.json()
    return data[0]['translations'][0]['text']



