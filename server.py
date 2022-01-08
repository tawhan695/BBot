import requests
import re

URL = 'laravelapp.url'

session = requests.session()

front = session.get(URL)
csrf_token = re.findall(r'<input type="hidden" name="_token" value="(.*)"', 
front.text)[0]

cookies = session.cookies

payload = {
    'email': 'email@example.com',
    'password': 'testtest',
    '_token': csrf_token,
}

r = requests.post(URL + '/login', data=payload, cookies=cookies)

print(r.text)


class API():

    def __init__(self):
        super().__init__
        self.URL = ''