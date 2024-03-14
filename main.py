import logging
import os
import requests

logging.basicConfig(
    filename='status.log', 
    encoding='utf-8', 
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

try:
    SOME_SECRET = os.environ['SOME_SECRET']
except KeyError:
    SOME_SECRET = 'Token not available!'

if __name__ == '__main__':
    logging.info(f'Token value: {SOME_SECRET}')

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=USA')
    if r.status_code == 200:
        data = r.json()
        temperature = data['forecast']['temp']
        logging.info(f'Weather in Berlin: {temperature}')
