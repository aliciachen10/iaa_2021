
import json
import requests
import datetime
import pyjokes

if __name__ == "__main__":
    
    your_name = 'Dan Zaratsian'
    joke = pyjokes.get_joke()
    datetimestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    payload = {"name": your_name, "joke":joke, "datetimestamp":datetimestamp}
    
    r = requests.post('https://us-east1-zproject201807.cloudfunctions.net/iaa-cf',
        headers={'content-type': 'application/json'},
        data=json.dumps(payload))
    
    if r.status_code == 200:
        print('[ INFO ] Success! {}'.format(r.content))
        print('[ INFO ] Payload passed to Google Cloud Functions: {}'.format(payload))
    else:
        print('[ ERROR ] Status Code: {}. {}'.format(r.status_code, r.content))

#ZEND
